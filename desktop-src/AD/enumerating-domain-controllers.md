---
title: Enumerating Domain Controllers
description: In earlier versions of Windows, an application could only obtain a single domain controller in a domain by calling DsGetDcName.
ms.assetid: bfc92777-6944-406a-8b93-949a1cf3e2c3
ms.tgt_platform: multiple
keywords:
- Active Directory examples Active Directory , enumerating domain controllers Active Directory
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Domain Controllers

In earlier versions of Windows, an application could only obtain a single domain controller in a domain by calling [**DsGetDcName**](/windows/desktop/api/DsGetDC/nf-dsgetdc-dsgetdcnamea). There was no way to predict which domain controller would be retrieved or to obtain a list of the domain controllers. Windows enables an application to enumerate the domain controllers in a domain by using the [**DsGetDcOpen**](/windows/desktop/api/Dsgetdc/nf-dsgetdc-dsgetdcopena), [**DsGetDcNext**](/windows/desktop/api/Dsgetdc/nf-dsgetdc-dsgetdcnexta), and [**DsGetDcClose**](/windows/desktop/api/Dsgetdc/nf-dsgetdc-dsgetdcclosew) functions.

To enumerate a domain controller, call [**DsGetDcOpen**](/windows/desktop/api/Dsgetdc/nf-dsgetdc-dsgetdcopena). This function takes parameters that define the domain to enumerate and other enumeration options. **DsGetDcOpen** provides a domain enumeration context handle that is used to identify the enumeration operation when [**DsGetDcNext**](/windows/desktop/api/Dsgetdc/nf-dsgetdc-dsgetdcnexta) and [**DsGetDcClose**](/windows/desktop/api/Dsgetdc/nf-dsgetdc-dsgetdcclosew) are called.

The [**DsGetDcNext**](/windows/desktop/api/Dsgetdc/nf-dsgetdc-dsgetdcnexta) function is called with the domain enumeration context handle to retrieve the next domain controller in the enumeration. The first time this function is called, the first domain controller in the enumeration is retrieved. The second time this function is called, the second domain controller in the enumeration is retrieved. This process is repeated until **DsGetDcNext** returns **ERROR\_NO\_MORE\_ITEMS**, that indicates the end of the enumeration.

The [**DsGetDcNext**](/windows/desktop/api/Dsgetdc/nf-dsgetdc-dsgetdcnexta) function will enumerate the domain controllers in two groups. The first group contains the domain controllers that cover the site of the computer where the function is executed and the second group contains the domain controllers that do not cover the site of the computer where the function is executed. If the **DS\_NOTIFY\_AFTER\_SITE\_RECORDS** flag is specified in the *OptionFlags* parameter in [**DsGetDcOpen**](/windows/desktop/api/Dsgetdc/nf-dsgetdc-dsgetdcopena), the **DsGetDcNext** function will return **ERROR\_FILEMARK\_DETECTED** after all of the site-specific domain controllers have been retrieved. **DsGetDcNext** will then begin enumerating the second group, which contains all domain controllers in the domain, including the site-specific domain controllers contained in the first group.

Domain controllers that handle the site of the computer where the function is executed are enumerated first followed by the domain controllers that do not cover the site of the computer where the function is executed. A domain controller is said to cover a site if the domain controller is configured to reside in that site or if the domain controller resides in a site that is nearest to the site in question in terms of the configured inter-site link cost. If there are any domain controllers in both the group of domain controllers that cover and the group of domain controllers that do not cover the computer site, domain controllers are returned within the group in order of their configured priorities and weights that are specified in DNS. Domain controllers that have lower numeric priority are returned within a group first. If within a site-related group there is a subgroup of several domain controllers with the same priority, domain controllers are returned in a weighted random order where domain controllers with higher weight have more probability to be returned first. The sites, priorities, and weights are configured by the domain administrator to achieve effective performance and load balancing among multiple domain controllers available in the domain. Because of this, applications that use the [**DsGetDcOpen**](/windows/desktop/api/Dsgetdc/nf-dsgetdc-dsgetdcopena)/[**DsGetDcNext**](/windows/desktop/api/Dsgetdc/nf-dsgetdc-dsgetdcnexta)/[**DsGetDcClose**](/windows/desktop/api/Dsgetdc/nf-dsgetdc-dsgetdcclosew) functions automatically take advantage of these optimizations.

When the enumeration is complete or is no longer required, the enumeration must be closed by calling [**DsGetDcClose**](/windows/desktop/api/Dsgetdc/nf-dsgetdc-dsgetdcclosew) with the domain enumeration context handle.

To reset the enumeration, it is necessary to close the current enumeration by calling [**DsGetDcClose**](/windows/desktop/api/Dsgetdc/nf-dsgetdc-dsgetdcclosew) and then reopen the enumeration by calling [**DsGetDcOpen**](/windows/desktop/api/Dsgetdc/nf-dsgetdc-dsgetdcopena) again.

## Example

The following code example shows how to use these functions to enumerate the domain controllers in the local domain.


```C++
DWORD dwRet;
PDOMAIN_CONTROLLER_INFO pdcInfo;

// Get a domain controller for the domain this computer is on.
dwRet = DsGetDcName(NULL, NULL, NULL, NULL, 0, &pdcInfo);
if(ERROR_SUCCESS == dwRet)
{
    HANDLE hGetDc;
    
    // Open the enumeration.
    dwRet = DsGetDcOpen(    pdcInfo->DomainName,
                            DS_NOTIFY_AFTER_SITE_RECORDS,
                            NULL,
                            NULL,
                            NULL,
                            0,
                            &hGetDc);
    if(ERROR_SUCCESS == dwRet)
    {
        LPTSTR pszDnsHostName;

        /*
        Enumerate each domain controller and print its name to the 
        debug window.
        */
        while(TRUE)
        {
            ULONG ulSocketCount;
            LPSOCKET_ADDRESS rgSocketAddresses;

            dwRet = DsGetDcNext(
                hGetDc, 
                &ulSocketCount, 
                &rgSocketAddresses, 
                &pszDnsHostName);
            
            if(ERROR_SUCCESS == dwRet)
            {
                OutputDebugString(pszDnsHostName);
                OutputDebugString(TEXT("\n"));
                
                // Free the allocated string.
                NetApiBufferFree(pszDnsHostName);

                // Free the socket address array.
                LocalFree(rgSocketAddresses);
            }
            else if(ERROR_NO_MORE_ITEMS == dwRet)
            {
                // The end of the list has been reached.
                break;
            }
            else if(ERROR_FILEMARK_DETECTED == dwRet)
            {
                /*
                DS_NOTIFY_AFTER_SITE_RECORDS was specified in 
                DsGetDcOpen and the end of the site-specific 
                records was reached.
                */
                OutputDebugString(
                  TEXT("End of site-specific domain controllers\n"));
                continue;
            }
            else
            {
                // Some other error occurred.
                break;
            }
        }
        
        // Close the enumeration.
        DsGetDcClose(hGetDc);
    }
    
    // Free the DOMAIN_CONTROLLER_INFO structure. 
    NetApiBufferFree(pdcInfo);
}
```



 

 




