---
title: Adding a Per Interface Rule
description: This example adds a per interface rule using the Windows Firewall with Advanced Security APIs.C++ /\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ ++ THIS CODE AND INFORMATION IS PROVIDED \ 0034;AS IS \ 0034; WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE. Copyright (C) Microsoft. All Rights Reserved. Abstract This C++ file includes sample code that adds a rule per interface for the currently active profiles using the Microsoft Windows Firewall APIs. --\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ / \ include windows.h \ include stdio.h \ include comdef.h \ include netfw.h // Forward declarations HRESULT WFCOMInitialize(INetFwPolicy2\ \ ppNetFwPolicy2); int \_\_cdecl main() HRESULT hrComInit S\_OK; HRESULT hr S\_OK; variant\_t vtInterfaceName( \ 0034;Local Area Connection \ 0034;), vtInterface; long index 0; SAFEARRAY \ pSa NULL; INetFwPolicy2 \ pNetFwPolicy2 NULL; INetFwRules \ pFwRules NULL; INetFwRule \ pFwRule NULL; long CurrentProfilesBitMask 0; BSTR bstrRuleName SysAllocString(L \ 0034;PER\_INTERFACE\_RULE \ 0034;); BSTR bstrRuleDescription SysAllocString(L \ 0034;Add a PER\_INTERFACE rule \ 0034;); BSTR bstrRuleGroup SysAllocString(L \ 0034;Sample Rule Group \ 0034;); BSTR bstrRuleLPorts SysAllocString(L \ 0034;2300 \ 0034;); // Initialize COM. hrComInit CoInitializeEx( 0, COINIT\_APARTMENTTHREADED ); // Ignore RPC\_E\_CHANGED\_MODE; this just means that COM has already been // initialized with a different mode. Since we don't care what the mode is, // we'll just use the existing mode. if (hrComInit RPC\_E\_CHANGED\_MODE) if (FAILED(hrComInit)) printf( \ 0034;CoInitializeEx failed 0x 08lx\\n \ 0034;, hrComInit); goto Cleanup; // Retrieve INetFwPolicy2 hr WFCOMInitialize( pNetFwPolicy2); if (FAILED(hr)) goto Cleanup; // Retrieve INetFwRules hr pNetFwPolicy2- get\_Rules( pFwRules); if (FAILED(hr)) printf( \ 0034;get\_Rules failed 0x 08lx\\n \ 0034;, hr); goto Cleanup; // Retrieve Current Profiles bitmask hr pNetFwPolicy2- get\_CurrentProfileTypes( CurrentProfilesBitMask); if (FAILED(hr)) printf( \ 0034;get\_CurrentProfileTypes failed 0x 08lx\\n \ 0034;, hr); goto Cleanup; // When possible we avoid adding firewall rules to the Public profile. // If Public is currently active and it is not the only active profile, we remove it from the bitmask if ((CurrentProfilesBitMask NET\_FW\_PROFILE2\_PUBLIC) (CurrentProfilesBitMask NET\_FW\_PROFILE2\_PUBLIC)) CurrentProfilesBitMask ^ NET\_FW\_PROFILE2\_PUBLIC; // Retrieve Local Interface pSa SafeArrayCreateVector(VT\_VARIANT, 0, 1); if ( pSa) \_com\_issue\_error(E\_OUTOFMEMORY); else hr SafeArrayPutElement(pSa, index, vtInterfaceName); if FAILED(hr) \_com\_issue\_error(hr); vtInterface.vt VT\_ARRAY \ VT\_VARIANT; vtInterface.parray pSa; // Create a new Firewall Rule object. hr CoCreateInstance( \_\_uuidof(NetFwRule), NULL, CLSCTX\_INPROC\_SERVER, \_\_uuidof(INetFwRule), (void\ \ ) pFwRule); if (FAILED(hr)) printf( \ 0034;CoCreateInstance for Firewall Rule failed 0x 08lx\\n \ 0034;, hr); goto Cleanup; // Populate the Firewall Rule object pFwRule- put\_Name(bstrRuleName); pFwRule- put\_Description(bstrRuleDescription); pFwRule- put\_Enabled(VARIANT\_TRUE); pFwRule- put\_Profiles(CurrentProfilesBitMask); pFwRule- put\_Grouping(bstrRuleGroup); pFwRule- put\_Interfaces(vtInterface); pFwRule- put\_Protocol(NET\_FW\_IP\_PROTOCOL\_TCP); pFwRule- put\_LocalPorts(bstrRuleLPorts); pFwRule- put\_Action(NET\_FW\_ACTION\_ALLOW); // Add the Firewall Rule hr pFwRules- Add(pFwRule); if (FAILED(hr)) printf( \ 0034;Firewall Rule Add failed 0x 08lx\\n \ 0034;, hr); goto Cleanup; Cleanup // Free BSTR's SysFreeString(bstrRuleName); SysFreeString(bstrRuleDescription); SysFreeString(bstrRuleGroup); SysFreeString(bstrRuleLPorts); // Release the INetFwRule object if (pFwRule NULL) pFwRule- Release(); // Release the INetFwRules object if (pFwRules NULL) pFwRules- Release(); // Release the INetFwPolicy2 object if (pNetFwPolicy2 NULL) pNetFwPolicy2- Release(); // Uninitialize COM. if (SUCCEEDED(hrComInit)) CoUninitialize(); return 0; // Instantiate INetFwPolicy2 HRESULT WFCOMInitialize(INetFwPolicy2\ \ ppNetFwPolicy2) HRESULT hr S\_OK; hr CoCreateInstance( \_\_uuidof(NetFwPolicy2), NULL, CLSCTX\_INPROC\_SERVER, \_\_uuidof(INetFwPolicy2), (void\ \ )ppNetFwPolicy2); if (FAILED(hr)) printf( \ 0034;CoCreateInstance for INetFwPolicy2 failed 0x 08lx\\n \ 0034;, hr); goto Cleanup; Cleanup return hr;
ms.assetid: 96ab7d3c-5960-47f9-8ab3-3e4fe0303c19
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Adding a Per Interface Rule

This example adds a per interface rule using the Windows Firewall with Advanced Security APIs.


```C++
 
/********************************************************************++
THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft. All Rights Reserved.

Abstract:
    This C++ file includes sample code that adds a rule per interface
    for the currently active profiles using the Microsoft Windows 
    Firewall APIs.

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

    variant_t      vtInterfaceName("Local Area Connection"), vtInterface;
    long           index = 0;
    SAFEARRAY      *pSa = NULL;

    INetFwPolicy2 *pNetFwPolicy2 = NULL;
    INetFwRules *pFwRules = NULL;
    INetFwRule *pFwRule = NULL;

    long CurrentProfilesBitMask = 0;

    BSTR bstrRuleName = SysAllocString(L"PER_INTERFACE_RULE");
    BSTR bstrRuleDescription = SysAllocString(L"Add a PER_INTERFACE rule");
    BSTR bstrRuleGroup = SysAllocString(L"Sample Rule Group");
    BSTR bstrRuleLPorts = SysAllocString(L"2300");

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

    // Retrieve INetFwRules
    hr = pNetFwPolicy2->get_Rules(&amp;pFwRules);
    if (FAILED(hr))
    {
        printf("get_Rules failed: 0x%08lx\n", hr);
        goto Cleanup;
    }

    // Retrieve Current Profiles bitmask
    hr = pNetFwPolicy2->get_CurrentProfileTypes(&amp;CurrentProfilesBitMask);
    if (FAILED(hr))
    {
        printf("get_CurrentProfileTypes failed: 0x%08lx\n", hr);
        goto Cleanup;
    }

    // When possible we avoid adding firewall rules to the Public profile.
    // If Public is currently active and it is not the only active profile, we remove it from the bitmask
    if ((CurrentProfilesBitMask & NET_FW_PROFILE2_PUBLIC) &amp;&amp;
        (CurrentProfilesBitMask != NET_FW_PROFILE2_PUBLIC))
    {
        CurrentProfilesBitMask ^= NET_FW_PROFILE2_PUBLIC;
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

    // Create a new Firewall Rule object.
    hr = CoCreateInstance(
                __uuidof(NetFwRule),
                NULL,
                CLSCTX_INPROC_SERVER,
                __uuidof(INetFwRule),
                (void**)&amp;pFwRule);
    if (FAILED(hr))
    {
        printf("CoCreateInstance for Firewall Rule failed: 0x%08lx\n", hr);
        goto Cleanup;
    }

    // Populate the Firewall Rule object
    pFwRule->put_Name(bstrRuleName);
    pFwRule->put_Description(bstrRuleDescription);
    pFwRule->put_Enabled(VARIANT_TRUE);
    pFwRule->put_Profiles(CurrentProfilesBitMask);
    pFwRule->put_Grouping(bstrRuleGroup);
    pFwRule->put_Interfaces(vtInterface);
    pFwRule->put_Protocol(NET_FW_IP_PROTOCOL_TCP);
    pFwRule->put_LocalPorts(bstrRuleLPorts);
    pFwRule->put_Action(NET_FW_ACTION_ALLOW);

    // Add the Firewall Rule
    hr = pFwRules->Add(pFwRule);
    if (FAILED(hr))
    {
        printf("Firewall Rule Add failed: 0x%08lx\n", hr);
        goto Cleanup;
    }

Cleanup:

    // Free BSTR's
    SysFreeString(bstrRuleName);
    SysFreeString(bstrRuleDescription);
    SysFreeString(bstrRuleGroup);
    SysFreeString(bstrRuleLPorts);

    // Release the INetFwRule object
    if (pFwRule != NULL)
    {
        pFwRule->Release();
    }

    // Release the INetFwRules object
    if (pFwRules != NULL)
    {
        pFwRules->Release();
    }

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



 

 




