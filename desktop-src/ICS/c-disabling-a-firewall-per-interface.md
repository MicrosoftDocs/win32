---
title: Disabling a Firewall Per Interface
description: This example disables a firewall per interface using the Windows Firewall with Advanced Security APIs.C++ /\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ ++ THIS CODE AND INFORMATION IS PROVIDED \ 0034;AS IS \ 0034; WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE. Copyright (C) Microsoft. All Rights Reserved. Abstract This C++ file includes sample code for disabling Windows Firewall per Interface. --\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ / \ include windows.h \ include stdio.h \ include comdef.h \ include netfw.h // Forward declarations HRESULT WFCOMInitialize(INetFwPolicy2\ \ ppNetFwPolicy2); int \_\_cdecl main() HRESULT hrComInit S\_OK; HRESULT hr S\_OK; INetFwPolicy2 \ pNetFwPolicy2 NULL; variant\_t vtInterfaceName( \ 0034;Local Area Connection \ 0034;), vtInterface; long index 0; SAFEARRAY \ pSa NULL; // Initialize COM. hrComInit CoInitializeEx( 0, COINIT\_APARTMENTTHREADED ); // Ignore RPC\_E\_CHANGED\_MODE; this just means that COM has already been // initialized with a different mode. Since we dont care what the mode is, // well just use the existing mode. if (hrComInit RPC\_E\_CHANGED\_MODE) if (FAILED(hrComInit)) printf( \ 0034;CoInitializeEx failed 0x 08lx\\n \ 0034;, hrComInit); goto Cleanup; // Retrieve INetFwPolicy2 hr WFCOMInitialize( pNetFwPolicy2); if (FAILED(hr)) goto Cleanup; // Retrieve Local Interface pSa SafeArrayCreateVector(VT\_VARIANT, 0, 1); if ( pSa) \_com\_issue\_error(E\_OUTOFMEMORY); else hr SafeArrayPutElement(pSa, index, vtInterfaceName); if FAILED(hr) \_com\_issue\_error(hr); vtInterface.vt VT\_ARRAY \ VT\_VARIANT; vtInterface.parray pSa; // Disable Windows Firewall for the local interface (Public profile) hr pNetFwPolicy2- put\_ExcludedInterfaces(NET\_FW\_PROFILE2\_PRIVATE, vtInterface); if (FAILED(hr)) printf( \ 0034;put\_ExcludedInterfaces failed 0x 08lx\\n \ 0034;, hr); goto Cleanup; Cleanup // Release the INetFwPolicy2 object if (pNetFwPolicy2 NULL) pNetFwPolicy2- Release(); // Uninitialize COM. if (SUCCEEDED(hrComInit)) CoUninitialize(); return 0; // Instantiate INetFwPolicy2 HRESULT WFCOMInitialize(INetFwPolicy2\ \ ppNetFwPolicy2) HRESULT hr S\_OK; hr CoCreateInstance( \_\_uuidof(NetFwPolicy2), NULL, CLSCTX\_INPROC\_SERVER, \_\_uuidof(INetFwPolicy2), (void\ \ )ppNetFwPolicy2); if (FAILED(hr)) printf( \ 0034;CoCreateInstance for INetFwPolicy2 failed 0x 08lx\\n \ 0034;, hr); goto Cleanup; Cleanup return hr;
ms.assetid: 35dd2c3e-2738-4a27-816c-66d5d8da7f86
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Disabling a Firewall Per Interface

This example disables a firewall per interface using the Windows Firewall with Advanced Security APIs.


```C++
 
/********************************************************************++
THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft. All Rights Reserved.

Abstract:
    This C++ file includes sample code for disabling Windows Firewall per
    Interface.

--********************************************************************/

#include <windows.h>
#include <stdio.h>
#include <comdef.h>
#include <netfw.h>


// Forward declarations
HRESULT     WFCOMInitialize(INetFwPolicy2** ppNetFwPolicy2);


int __cdecl main()
{
    HRESULT hrComInit = S_OK;
    HRESULT hr = S_OK;

    INetFwPolicy2 *pNetFwPolicy2 = NULL;

    variant_t      vtInterfaceName("Local Area Connection"), vtInterface;
    long           index = 0;
    SAFEARRAY      *pSa = NULL;

    // Initialize COM.
    hrComInit = CoInitializeEx(
                    0,
                    COINIT_APARTMENTTHREADED
                    );

    // Ignore RPC_E_CHANGED_MODE; this just means that COM has already been
    // initialized with a different mode. Since we don't care what the mode is,
    // we'll just use the existing mode.
    if (hrComInit != RPC_E_CHANGED_MODE)
    {
        if (FAILED(hrComInit))
        {
            printf("CoInitializeEx failed: 0x%08lx\n", hrComInit);
            goto Cleanup;
        }
    }

    // Retrieve INetFwPolicy2
    hr = WFCOMInitialize(&amp;pNetFwPolicy2);
    if (FAILED(hr))
    {
        goto Cleanup;
    }

    // Retrieve Local Interface
    pSa = SafeArrayCreateVector(VT_VARIANT, 0, 1);
    if (!pSa)
        _com_issue_error(E_OUTOFMEMORY);
    else
    {
        hr = SafeArrayPutElement(pSa, &amp;index, &amp;vtInterfaceName);
        if FAILED(hr)
            _com_issue_error(hr);
        vtInterface.vt = VT_ARRAY | VT_VARIANT;
        vtInterface.parray = pSa;
    }

    // Disable Windows Firewall for the local interface (Public profile)
    hr = pNetFwPolicy2->put_ExcludedInterfaces(NET_FW_PROFILE2_PRIVATE, vtInterface);
    if (FAILED(hr))
    {
        printf("put_ExcludedInterfaces failed: 0x%08lx\n", hr);
        goto Cleanup;
    }

Cleanup:

    // Release the INetFwPolicy2 object
    if (pNetFwPolicy2 != NULL)
    {
        pNetFwPolicy2->Release();
    }

    // Uninitialize COM.
    if (SUCCEEDED(hrComInit))
    {
        CoUninitialize();
    }
   
    return 0;
}


// Instantiate INetFwPolicy2
HRESULT WFCOMInitialize(INetFwPolicy2** ppNetFwPolicy2)
{
    HRESULT hr = S_OK;

    hr = CoCreateInstance(
        __uuidof(NetFwPolicy2), 
        NULL, 
        CLSCTX_INPROC_SERVER, 
        __uuidof(INetFwPolicy2), 
        (void**)ppNetFwPolicy2);

    if (FAILED(hr))
    {
        printf("CoCreateInstance for INetFwPolicy2 failed: 0x%08lx\n", hr);
        goto Cleanup;        
    }

Cleanup:
    return hr;
}


```



 

 




