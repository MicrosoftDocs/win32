---
title: Composing SPNs for an RpcNs Service
description: The following code example composes the service principal names (SPNs) for an RPC service that has an entry in the RpcServices container in the directory. An RPC service uses the RpcNsBindingExport function to create its RpcServices entry.
ms.assetid: 4fd585b3-3f9b-4f7f-bc1b-22879587a590
ms.tgt_platform: multiple
keywords:
- Composing SPNs for an RpcNs Service AD
ms.topic: article
ms.date: 05/31/2018
---

# Composing SPNs for an RpcNs Service

The following code example composes the service principal names (SPNs) for an RPC service that has an entry in the RpcServices container in the directory. An RPC service uses the [**RpcNsBindingExport**](/windows/desktop/api/rpcnsi/nf-rpcnsi-rpcnsbindingexporta) function to create its RpcServices entry.

An RPC service uses this code example to build the SPN or SPNs that identify an instance of the service. The service uses this routine to perform the following tasks:

-   To register or unregister the SPNs in the directory, when the service is installed or removed. For more information and a code example, see [Registering the SPNs for a Service](registering-the-spns-for-a-service.md).
-   Register itself with the RPC authentication service when the service starts. For more information, see [Mutual Authentication in RPC Applications](mutual-authentication-in-rpc-applications.md).

This code example uses the distinguished name of the service's RpcServices entry to compose the SPN. Before calling this code, call the [**RpcNsBindingExport**](/windows/desktop/api/rpcnsi/nf-rpcnsi-rpcnsbindingexporta) function to create the service's RpcServices entry.

This code example calls the [**DsGetSpn**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsgetspna) function to build an SPN. The SPN is composed from service class name and the distinguished name of the service RpcServices entry.


```C++
/**********

    SpnCompose()

    Composes a service principal name from a service name and class.

    Parameters:

    pszServiceName - Contains a null-terminated string that contains 
    the name of the service.

    pszServiceClass - Contains a null-terminated string that contains 
    the name of the service class.

    pspn - Pointer to an LPTSTR array that receives the array of 
    SPNs. This array must freed with the DsFreeSpnArray function when 
    it is no longer required.

    pulSpn - Pointer to a unsigned long that receives the number of 
    elements in the pspn array.

***********/

HRESULT SpnCompose(LPTSTR pszServiceName, 
                   LPTSTR pszServiceClass, 
                   LPTSTR **pspn, 
                   unsigned long *pulSpn) 
{
    HRESULT hr;
    CComPtr<IADs> spRoot;

    // Get the defaultNamingContext for the local domain.
    hr = ADsGetObject(L"LDAP://RootDSE",
                      IID_IADs,
                      (void**)&spRoot);
    if(FAILED(hr))
    {
        return hr;
    }

    // Get the distinguished name of the current domain.
    CComVariant svarDSRoot;
    hr = spRoot->Get(CComBSTR("defaultNamingContext"), &svarDSRoot);
     
    /*
    Compose the DN of the service's entry in the RpcServices 
    container, created by a call to RpcNsBindingExport. The entry 
    for an RPC service is in the System/RpcServices container in the 
    defaultNamingContext of the local domain.
    */
    
    CComBSTR sbstrDsEntryName = "CN=";
    sbstrDsEntryName += pszServiceName;
    sbstrDsEntryName += ",CN=RpcServices,CN=System,";
    sbstrDsEntryName += svarDSRoot.bstrVal;

    USES_CONVERSION;  // Required for the W2T() macro.
    DWORD status;

    /*
    Build the SPN for this service using the DN and the service 
    class.
    */
    status = DsGetSpn(
        DS_SPN_SERVICE, // Type of SPN to create.
        pszServiceClass, // Service class - a name in this case.
        W2T(sbstrDsEntryName), // DN of the RpcServices for 
                               // this RPC service.
        0, // Use the default instance port.
        0, // Number of additional instance names.
        NULL, // No additional instance names.
        NULL, // No additional instance ports.
        pulSpn, // Size of SPN array.
        pspn // Returned SPN(s).
        );
     
    return HRESULT_FROM_WIN32(status);
}
```



 

 