---
title: Enabling Service Account to Access SCP Properties
description: The following code example sets a pair of Access Control Entries (ACEs) on a service connection point (SCP) object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 663dcf55-5f0d-49af-8b51-4c1e35b79ef1
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Enabling Service Account to Access SCP Properties AD
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Enabling Service Account to Access SCP Properties

The following code example sets a pair of Access Control Entries (ACEs) on a service connection point (SCP) object. The ACEs grant read/write access to the user or computer account under which the service instance will be running. The service installer uses code similar to the following to ensure that the service can update its properties at run time. If ACEs similar to these these are not set, the service will not have access to the properties of the SCP.

Typically, a service installer will set these ACEs after creating the SCP object. For more information, and a code example that creates an SCP and calls this function, see [How Clients Find and Use a Service Connection Point](how-clients-find-and-use-a-service-connection-point.md). If the service is reconfigured to run under a different account, the ACEs must be updated. To run successfully, this code example must be run in the security context of a domain administrator.

The first parameter of the sample function specifies the name of the user account to be granted access. The function assumes the name is in *Domain***\\***UserName* format. If no account is specified, the function assumes the service uses the LocalSystem account. This means the function must grant access to the computer account of the host server on which the service is running. To do this, the code example calls the [**GetComputerObjectName**](https://msdn.microsoft.com/library/windows/desktop/ms724304) function to obtain the domain and user name of the local computer.

The following code example can be modified to grant the service full access to the SCP object, but the best practice is to grant only the specific access rights that the service requires at run time. In this case, the function grants access to two properties.



| Property                                                              | Description                                                          |
|-----------------------------------------------------------------------|----------------------------------------------------------------------|
| [**serviceDNSName**](https://msdn.microsoft.com/library/ms679782)                       | The name of the host server on which the service is running.         |
| [**serviceBindingInformation**](https://msdn.microsoft.com/library/ms679778) | Private binding information that the service updates when it starts. |



 

Each property is identified by the **schemaIDGUID** of the property's **attributeSchema** class. Every property in the schema has its own unique **schemaIDGUID**. The following code example uses strings to specify the GUIDs. The GUID strings have the following format where each "X" is replaced by a hexadecimal digit: {XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}.

Refer to the Active Directory Schema reference pages for the **schemaIDGUID** values assigned to the properties to grant or deny access to.

The following code example uses the [**IADsSecurityDescriptor**](https://msdn.microsoft.com/library/aa706128), [**IADsAccessControlList**](https://msdn.microsoft.com/library/aa705953), and [**IADsAccessControlEntry**](https://msdn.microsoft.com/library/aa705951) interfaces to perform the following operations.

1.  Obtain the security descriptor of the SCP object.
2.  Set the appropriate ACEs in the discretionary access control list (DACL) of the security descriptor.
3.  Modify the security descriptor of the SCP object.


```C++
#include <atlbase.h>

//******************************
//
//  AllowAccessToScpProperties()
//
//******************************

HRESULT AllowAccessToScpProperties(
    LPWSTR wszAccountSAM,   // Service account to allow access.
    IADs *pSCPObject)       // IADs pointer to the SCP object.
{
    HRESULT hr = E_FAIL;
    IADsAccessControlList *pACL = NULL;
    IADsSecurityDescriptor *pSD = NULL;
    IDispatch *pDisp = NULL;
    IADsAccessControlEntry *pACE1 = NULL;
    IADsAccessControlEntry *pACE2 = NULL;
    IDispatch *pDispACE = NULL;
    long lFlags = 0L;
    CComBSTR sbstrTrustee;
    CComBSTR sbstrSecurityDescriptor = L"nTSecurityDescriptor";
    VARIANT varSD;

    if(NULL == pSCPObject)
    {
        return E_INVALIDARG;
    }
    
    VariantInit(&amp;varSD);
     
    /*
    If no service account is specified, service runs under 
    LocalSystem. Allow access to the computer account of the 
    service's host.
    */
    if (wszAccountSAM) 
    {
        sbstrTrustee = wszAccountSAM;
    }
    else
    {
        LPWSTR pwszComputerName;
        DWORD dwLen;
        
        // Get the size required for the SAM account name.
        dwLen = 0;
        GetComputerObjectNameW(NameSamCompatible, 
            NULL, &amp;dwLen);
        
        pwszComputerName = new WCHAR[dwLen + 1];
        if(NULL == pwszComputerName)
        {
            hr = E_OUTOFMEMORY;
            goto cleanup;
        }

        /*
        Get the SAM account name of the computer object for 
        the server.
        */
        if(!GetComputerObjectNameW(NameSamCompatible,
            pwszComputerName, &amp;dwLen))
        {
            delete pwszComputerName;
            
            hr = HRESULT_FROM_WIN32(GetLastError());
            goto cleanup;
        }

        sbstrTrustee = pwszComputerName;
        wprintf(L"GetComputerObjectName: %s\n", pwszComputerName);
        delete pwszComputerName;
    } 

    // Get the nTSecurityDescriptor.
    hr = pSCPObject->Get(sbstrSecurityDescriptor, &amp;varSD);
    if (FAILED(hr) || (varSD.vt != VT_DISPATCH)) 
    {
        _tprintf(TEXT("Get nTSecurityDescriptor failed: 0x%x\n"), hr);
        goto cleanup;
    } 
     
    /*
    Use the V_DISPATCH macro to get the IDispatch pointer from 
    VARIANT structure and QueryInterface for an 
    IADsSecurityDescriptor pointer.
    */
    hr = V_DISPATCH( &amp;varSD )->QueryInterface(
        IID_IADsSecurityDescriptor,
        (void**)&amp;pSD);
    if (FAILED(hr)) 
    {
        _tprintf(
            TEXT("Cannot get IADsSecurityDescriptor: 0x%x\n"), 
            hr);
        goto cleanup;
    } 
     
    /*
    Get an IADsAccessControlList pointer to the security 
    descriptor's DACL.
    */
    hr = pSD->get_DiscretionaryAcl(&amp;pDisp);
    if (SUCCEEDED(hr))
    {
        hr = pDisp->QueryInterface(
            IID_IADsAccessControlList,
            (void**)&amp;pACL);
    }
    if (FAILED(hr)) 
    {
        _tprintf(TEXT("Cannot get DACL: 0x%x\n"), hr);
        goto cleanup;
    } 
     
    // Create the COM object for the first ACE.
    hr = CoCreateInstance(CLSID_AccessControlEntry,
                        NULL,
                        CLSCTX_INPROC_SERVER,
                        IID_IADsAccessControlEntry,
                        (void **)&amp;pACE1);
     
    // Create the COM object for the second ACE.
    if (SUCCEEDED(hr))
    {
        hr = CoCreateInstance(CLSID_AccessControlEntry,
                        NULL,
                        CLSCTX_INPROC_SERVER,
                        IID_IADsAccessControlEntry,
                        (void **)&amp;pACE2);
    }
    if (FAILED(hr)) 
    {
        _tprintf(TEXT("Cannot create ACEs: 0x%x\n"), hr);
        goto cleanup;
    } 
     
    // Set the properties of the two ACEs.
                                
    // Allow read and write access to the property.
    hr = pACE1->put_AccessMask(
        ADS_RIGHT_DS_READ_PROP | ADS_RIGHT_DS_WRITE_PROP);
    hr = pACE2->put_AccessMask( 
        ADS_RIGHT_DS_READ_PROP | ADS_RIGHT_DS_WRITE_PROP);
                                
    // Set the trustee, which is either the service account or the 
    // host computer account.
    hr = pACE1->put_Trustee( sbstrTrustee );
    hr = pACE2->put_Trustee( sbstrTrustee );
                                
    // Set the ACE type.
    hr = pACE1->put_AceType( ADS_ACETYPE_ACCESS_ALLOWED_OBJECT );
    hr = pACE2->put_AceType( ADS_ACETYPE_ACCESS_ALLOWED_OBJECT );
                                
    // Set AceFlags to zero because ACE is not inheritable.
    hr = pACE1->put_AceFlags( 0 );
    hr = pACE2->put_AceFlags( 0 );
     
    // Set Flags to indicate an ACE that protects a specified object.
    hr = pACE1->put_Flags( ADS_FLAG_OBJECT_TYPE_PRESENT );
    hr = pACE2->put_Flags( ADS_FLAG_OBJECT_TYPE_PRESENT );
     
    // Set ObjectType to the schemaIDGUID of the attribute.
    // serviceDNSName
    hr = pACE1->put_ObjectType( 
        L"{28630eb8-41d5-11d1-a9c1-0000f80367c1}"); 
    // serviceBindingInformation
    hr = pACE2->put_ObjectType( 
        L"{b7b1311c-b82e-11d0-afee-0000f80367c1}"); 
     
    /*
    Add the ACEs to the DACL. Need an IDispatch pointer for 
    each ACE to pass to the AddAce method.
    */
    hr = pACE1->QueryInterface(IID_IDispatch,(void**)&amp;pDispACE);
    if (SUCCEEDED(hr))
    {
        hr = pACL->AddAce(pDispACE);
    }
    if (FAILED(hr)) 
    {
        _tprintf(TEXT("Cannot add first ACE: 0x%x\n"), hr);
        goto cleanup;
    }
    else 
    {
        if (pDispACE)
            pDispACE->Release();
    
        pDispACE = NULL;
    }
     
    // Repeat for the second ACE.
    hr = pACE2->QueryInterface(IID_IDispatch, (void**)&amp;pDispACE);
    if (SUCCEEDED(hr))
    {
        hr = pACL->AddAce(pDispACE);
    }
    if (FAILED(hr)) 
    {
        _tprintf(TEXT("Cannot add second ACE: 0x%x\n"), hr);
        goto cleanup;
    }
     
    // Write the modified DACL back to the security descriptor.
    hr = pSD->put_DiscretionaryAcl(pDisp);
    if (SUCCEEDED(hr))
    {
        /*
        Write the ntSecurityDescriptor property to the 
        property cache.
        */
        hr = pSCPObject->Put(sbstrSecurityDescriptor, varSD);
        if (SUCCEEDED(hr))
        {
            // SetInfo updates the SCP object in the directory.
            hr = pSCPObject->SetInfo();
        }
    }
                                    
    cleanup:
    if (pDispACE)
        pDispACE->Release();
                        
    if (pACE1)
        pACE1->Release();
                    
    if (pACE2)
        pACE2->Release();
                    
    if (pACL)
        pACL->Release();
               
    if (pDisp)
        pDisp->Release();
            
    if (pSD)
        pSD->Release();
 
    VariantClear(&amp;varSD);
 
    return hr;
}
```



 

 




