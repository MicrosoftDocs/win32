---
title: Adding an Application Rule to Allow Dynamic Edge Traversal
description: This example adds an application rule to allow dynamic edge traversal using the Windows Firewall with Advanced Security APIs.In order for Windows Firewall to dynamically allow edge traversal traffic, the following two items must be done The application must use the IPV6\_PROTECTION\_LEVEL socket option on the listening socket and set it to PROTECTION\_LEVEL\_UNRESTRICTED when the application wants to allow edge traffic. The Windows Firewall rule added for the application must set edge traversal option to NET\_FW\_EDGE\_TRAVERSAL\_TYPE\_DEFER\_TO\_APP. This sample only illustrates one of the edge traversal option values. For more information on these values, see NET\_FW\_EDGE\_TRAVERSAL\_TYPE.C++/\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Copyright (C) Microsoft. All Rights Reserved. Abstract This C++ file includes sample code that adds a firewall rule with EdgeTraversalOptions (one of the EdgeTraversalOptions values). \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ / \ include windows.h \ include stdio.h \ include netfw.h \ include strsafe.h \ pragma comment(lib, \ 0034;ole32.lib \ 0034;) \ pragma comment(lib, \ 0034;oleaut32.lib \ 0034;) \ define STRING\_BUFFER\_SIZE 500 // Forward declarations HRESULT WFCOMInitialize(INetFwPolicy2\ \ ppNetFwPolicy2); void WFCOMCleanup(INetFwPolicy2\ pNetFwPolicy2); HRESULT AddFirewallRuleWithEdgeTraversal(\_\_in INetFwPolicy2 \ pNetFwPolicy2); int \_\_cdecl wmain() HRESULT hrComInit S\_OK; HRESULT hr S\_OK; INetFwPolicy2 \ pNetFwPolicy2 NULL; // Initialize COM. hrComInit CoInitializeEx( 0, COINIT\_APARTMENTTHREADED ); // Ignore RPC\_E\_CHANGED\_MODE; this just means that COM has already been // initialized with a different mode. Since we don't care what the mode is, // we'll just use the existing mode. if (hrComInit RPC\_E\_CHANGED\_MODE) if (FAILED(hrComInit)) wprintf(L \ 0034;CoInitializeEx failed 0x 08lx\\n \ 0034;, hrComInit); goto Cleanup; // Retrieve INetFwPolicy2 hr WFCOMInitialize( pNetFwPolicy2); if (FAILED(hr)) goto Cleanup; // Add firewall rule with EdgeTraversalOption DeferApp (Windows7+) if available // else add with Edge True (Vista and Server 2008). AddFirewallRuleWithEdgeTraversal(pNetFwPolicy2); Cleanup // Release INetFwPolicy2 WFCOMCleanup(pNetFwPolicy2); // Uninitialize COM. if (SUCCEEDED(hrComInit)) CoUninitialize(); return 0; // Add firewall rule with EdgeTraversalOption DeferApp (Windows7+) if available // else add with Edge True (Vista and Server 2008). HRESULT AddFirewallRuleWithEdgeTraversal(\_\_in INetFwPolicy2 \ pNetFwPolicy2) HRESULT hr S\_OK; INetFwRules \ pNetFwRules NULL; INetFwRule \ pNetFwRule NULL; INetFwRule2 \ pNetFwRule2 NULL; WCHAR pwszTemp\ STRING\_BUFFER\_SIZE\ L \ 0034; \ 0034;; BSTR RuleName NULL; BSTR RuleGroupName NULL; BSTR RuleDescription NULL; BSTR RuleAppPath NULL; // For localization purposes, the rule name, description, and group can be // provided as indirect strings. These indirect strings can be defined in an rc file. // Examples of the indirect string definitions in the rc file - // 127 \ 0034;EdgeTraversalOptions Sample Application \ 0034; // 128 \ 0034;Allow inbound TCP traffic to application EdgeTraversalOptions.exe \ 0034; // 129 \ 0034;Allow EdgeTraversalOptions.exe to receive inbound traffic for TCP protocol // from remote machines located within your network as well as from // the Internet (i.e from outside of your Edge device like Firewall or NAT \ 0034; // Examples of using indirect strings - // hr StringCchPrintfW(pwszTemp, STRING\_BUFFER\_SIZE, L \ 0034; EdgeTraversalOptions.exe,-128 \ 0034;); hr StringCchPrintfW(pwszTemp, STRING\_BUFFER\_SIZE, L \ 0034;Allow inbound TCP traffic to application EdgeTraversalOptions.exe \ 0034;); if (FAILED(hr)) wprintf(L \ 0034;Failed to compose a resource identifier string 0x 08lx\\n \ 0034;, hr); goto Cleanup; RuleName SysAllocString(pwszTemp); if (NULL RuleName) wprintf(L \ 0034;\\nERROR Insufficient memory\\n \ 0034;); goto Cleanup; // Examples of using indirect strings - // hr StringCchPrintfW(pwszTemp, STRING\_BUFFER\_SIZE, L \ 0034; EdgeTraversalOptions.exe,-127 \ 0034;); hr StringCchPrintfW(pwszTemp, STRING\_BUFFER\_SIZE, L \ 0034;EdgeTraversalOptions Sample Application \ 0034;); if (FAILED(hr)) wprintf(L \ 0034;Failed to compose a resource identifier string 0x 08lx\\n \ 0034;, hr); goto Cleanup; RuleGroupName SysAllocString(pwszTemp); // Used for grouping together multiple rules if (NULL RuleGroupName) wprintf(L \ 0034;\\nERROR Insufficient memory\\n \ 0034;); goto Cleanup; // Examples of using indirect strings - // hr StringCchPrintfW(pwszTemp, STRING\_BUFFER\_SIZE, L \ 0034; EdgeTraversalOptions.exe,-129 \ 0034;); hr StringCchPrintfW(pwszTemp, STRING\_BUFFER\_SIZE, L \ 0034;Allow EdgeTraversalOptions.exe to receive \\ inbound traffic for TCP protocol from remote machines located within your network as well as \\ from the Internet (i.e from outside of your Edge device like Firewall or NAT) \ 0034;); if (FAILED(hr)) wprintf(L \ 0034;Failed to compose a resource identifier string 0x 08lx\\n \ 0034;, hr); goto Cleanup; RuleDescription SysAllocString(pwszTemp); if (NULL RuleDescription) wprintf(L \ 0034;\\nERROR Insufficient memory\\n \ 0034;); goto Cleanup; RuleAppPath SysAllocString(L \ 0034; ProgramFiles \\\\EdgeTraversalOptions\\\\EdgeTraversalOptions.exe \ 0034;); if (NULL RuleAppPath) wprintf(L \ 0034;\\nERROR Insufficient memory\\n \ 0034;); goto Cleanup; hr pNetFwPolicy2- get\_Rules( pNetFwRules); if (FAILED(hr)) wprintf(L \ 0034;Failed to retrieve firewall rules collection 0x 08lx\\n \ 0034;, hr); goto Cleanup; hr CoCreateInstance( \_\_uuidof(NetFwRule), //CLSID of the class whose object is to be created NULL, CLSCTX\_INPROC\_SERVER, \_\_uuidof(INetFwRule), // Identifier of the Interface used for communicating with the object (void\ \ ) pNetFwRule); if (FAILED(hr)) wprintf(L \ 0034;CoCreateInstance for INetFwRule failed 0x 08lx\\n \ 0034;, hr); goto Cleanup; hr pNetFwRule- put\_Name(RuleName); if ( FAILED(hr) ) wprintf(L \ 0034;Failed INetFwRule put\_Name failed with error 0x x.\\n \ 0034;, hr); goto Cleanup; hr pNetFwRule- put\_Grouping(RuleGroupName); if ( FAILED(hr) ) wprintf(L \ 0034;Failed INetFwRule put\_Grouping failed with error 0x x.\\n \ 0034;, hr); goto Cleanup; hr pNetFwRule- put\_Description(RuleDescription); if ( FAILED(hr) ) wprintf(L \ 0034;Failed INetFwRule put\_Description failed with error 0x x.\\n \ 0034;, hr); goto Cleanup; hr pNetFwRule- put\_Direction(NET\_FW\_RULE\_DIR\_IN); if ( FAILED(hr) ) wprintf(L \ 0034;Failed INetFwRule put\_Direction failed with error 0x x.\\n \ 0034;, hr); goto Cleanup; hr pNetFwRule- put\_Action(NET\_FW\_ACTION\_ALLOW); if ( FAILED(hr) ) wprintf(L \ 0034;Failed INetFwRule put\_Action failed with error 0x x.\\n \ 0034;, hr); goto Cleanup; hr pNetFwRule- put\_ApplicationName(RuleAppPath); if ( FAILED(hr) ) wprintf(L \ 0034;Failed INetFwRule put\_ApplicationName failed with error 0x x.\\n \ 0034;, hr); goto Cleanup; hr pNetFwRule- put\_Protocol(6); // TCP if ( FAILED(hr) ) wprintf(L \ 0034;Failed INetFwRule put\_Protocol failed with error 0x x.\\n \ 0034;, hr); goto Cleanup; hr pNetFwRule- put\_Profiles(NET\_FW\_PROFILE2\_DOMAIN \ NET\_FW\_PROFILE2\_PRIVATE); if ( FAILED(hr) ) wprintf(L \ 0034;Failed INetFwRule put\_Profiles failed with error 0x x.\\n \ 0034;, hr); goto Cleanup; hr pNetFwRule- put\_Enabled(VARIANT\_TRUE); if ( FAILED(hr) ) wprintf(L \ 0034;Failed INetFwRule put\_Enabled failed with error 0x x.\\n \ 0034;, hr); goto Cleanup; // Check if INetFwRule2 interface is available (i.e Windows7+) // If supported, then use EdgeTraversalOptions // Else use the EdgeTraversal boolean flag. if (SUCCEEDED(pNetFwRule- QueryInterface(\_\_uuidof(INetFwRule2), (void\ \ ) pNetFwRule2))) hr pNetFwRule2- put\_EdgeTraversalOptions(NET\_FW\_EDGE\_TRAVERSAL\_TYPE\_DEFER\_TO\_APP); if ( FAILED(hr) ) wprintf(L \ 0034;Failed INetFwRule put\_EdgeTraversalOptions failed with error 0x x.\\n \ 0034;, hr); goto Cleanup; else hr pNetFwRule- put\_EdgeTraversal(VARIANT\_TRUE); if ( FAILED(hr) ) wprintf(L \ 0034;Failed INetFwRule put\_EdgeTraversal failed with error 0x x.\\n \ 0034;, hr); goto Cleanup; hr pNetFwRules- Add(pNetFwRule); if (FAILED(hr)) wprintf(L \ 0034;Failed to add firewall rule to the firewall rules collection 0x 08lx\\n \ 0034;, hr); goto Cleanup; wprintf(L \ 0034;Successfully added firewall rule \\n \ 0034;); Cleanup SysFreeString(RuleName); SysFreeString(RuleGroupName); SysFreeString(RuleDescription); SysFreeString(RuleAppPath); if (pNetFwRule2 NULL) pNetFwRule2- Release(); if (pNetFwRule NULL) pNetFwRule- Release(); if (pNetFwRules NULL) pNetFwRules- Release(); return hr; // Instantiate INetFwPolicy2 HRESULT WFCOMInitialize(INetFwPolicy2\ \ ppNetFwPolicy2) HRESULT hr S\_OK; hr CoCreateInstance( \_\_uuidof(NetFwPolicy2), NULL, CLSCTX\_INPROC\_SERVER, \_\_uuidof(INetFwPolicy2), (void\ \ )ppNetFwPolicy2); if (FAILED(hr)) wprintf(L \ 0034;CoCreateInstance for INetFwPolicy2 failed 0x 08lx\\n \ 0034;, hr); goto Cleanup; Cleanup return hr; // Release INetFwPolicy2 void WFCOMCleanup(INetFwPolicy2\ pNetFwPolicy2) // Release the INetFwPolicy2 object (Vista+) if (pNetFwPolicy2 NULL) pNetFwPolicy2- Release();
ms.assetid: e79085ba-9e29-4293-8fb2-51bfa663fd07
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Adding an Application Rule to Allow Dynamic Edge Traversal

This example adds an application rule to allow dynamic edge traversal using the Windows Firewall with Advanced Security APIs.

In order for Windows Firewall to dynamically allow edge traversal traffic, the following two items must be done:

1.  The application must use the [IPV6\_PROTECTION\_LEVEL](https://msdn.microsoft.com/library/windows/desktop/aa832668) socket option on the listening socket and set it to **PROTECTION\_LEVEL\_UNRESTRICTED** when the application wants to allow edge traffic.
2.  The Windows Firewall rule added for the application must set edge traversal option to **NET\_FW\_EDGE\_TRAVERSAL\_TYPE\_DEFER\_TO\_APP**.

This sample only illustrates one of the edge traversal option values. For more information on these values, see [**NET\_FW\_EDGE\_TRAVERSAL\_TYPE**](/previous-versions/windows/desktop/api/Icftypes/ne-icftypes-net_fw_edge_traversal_type_).


```C++
/********************************************************************
Copyright (C) Microsoft. All Rights Reserved.

Abstract:
    This C++ file includes sample code that adds a firewall rule with
 EdgeTraversalOptions (one of the EdgeTraversalOptions values).

********************************************************************/

#include <windows.h>
#include <stdio.h>
#include <netfw.h>
#include <strsafe.h>

#pragma comment(lib, "ole32.lib")
#pragma comment(lib, "oleaut32.lib")

#define STRING_BUFFER_SIZE  500     


// Forward declarations
HRESULT    WFCOMInitialize(INetFwPolicy2** ppNetFwPolicy2);
void       WFCOMCleanup(INetFwPolicy2* pNetFwPolicy2);
HRESULT    AddFirewallRuleWithEdgeTraversal(__in INetFwPolicy2 *pNetFwPolicy2);


int __cdecl wmain()
{
    HRESULT hrComInit = S_OK;
    HRESULT hr = S_OK;
    INetFwPolicy2 *pNetFwPolicy2 = NULL;

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
            wprintf(L"CoInitializeEx failed: 0x%08lx\n", hrComInit);
            goto Cleanup;
        }
    }

    // Retrieve INetFwPolicy2
    hr = WFCOMInitialize(&amp;pNetFwPolicy2);
    if (FAILED(hr))
    {
        goto Cleanup;
    }

    // Add firewall rule with EdgeTraversalOption=DeferApp (Windows7+) if available 
    //   else add with Edge=True (Vista and Server 2008).
    AddFirewallRuleWithEdgeTraversal(pNetFwPolicy2);

Cleanup:

    // Release INetFwPolicy2
    WFCOMCleanup(pNetFwPolicy2);

    // Uninitialize COM.
    if (SUCCEEDED(hrComInit))
    {
        CoUninitialize();
    }
   
    return 0;
}

// Add firewall rule with EdgeTraversalOption=DeferApp (Windows7+) if available 
//   else add with Edge=True (Vista and Server 2008).
HRESULT    AddFirewallRuleWithEdgeTraversal(__in INetFwPolicy2 *pNetFwPolicy2)
{
    HRESULT hr = S_OK;
    INetFwRules *pNetFwRules = NULL;
    
    INetFwRule  *pNetFwRule = NULL;
    INetFwRule2 *pNetFwRule2 = NULL;

    WCHAR pwszTemp[STRING_BUFFER_SIZE] = L"";

    BSTR RuleName = NULL;
    BSTR RuleGroupName = NULL;
    BSTR RuleDescription = NULL;
    BSTR RuleAppPath = NULL;


    //  For localization purposes, the rule name, description, and group can be 
    //    provided as indirect strings. These indirect strings can be defined in an rc file.
    //  Examples of the indirect string definitions in the rc file -
    //    127                     "EdgeTraversalOptions Sample Application"
    //    128                     "Allow inbound TCP traffic to application EdgeTraversalOptions.exe"
    //    129                     "Allow EdgeTraversalOptions.exe to receive inbound traffic for TCP protocol 
    //                          from remote machines located within your network as well as from 
    //                          the Internet (i.e from outside of your Edge device like Firewall or NAT"

    
    //    Examples of using indirect strings -
    //    hr = StringCchPrintfW(pwszTemp, STRING_BUFFER_SIZE, L"@EdgeTraversalOptions.exe,-128");
    hr = StringCchPrintfW(pwszTemp, STRING_BUFFER_SIZE, L"Allow inbound TCP traffic to application EdgeTraversalOptions.exe");
    if (FAILED(hr))
    {
        wprintf(L"Failed to compose a resource identifier string: 0x%08lx\n", hr);
        goto Cleanup;        
    }
    RuleName = SysAllocString(pwszTemp);
    if (NULL == RuleName)
    {
        wprintf(L"\nERROR: Insufficient memory\n");
        goto Cleanup;
    }
    //    Examples of using indirect strings -
    //    hr = StringCchPrintfW(pwszTemp, STRING_BUFFER_SIZE, L"@EdgeTraversalOptions.exe,-127");
    hr = StringCchPrintfW(pwszTemp, STRING_BUFFER_SIZE, L"EdgeTraversalOptions Sample Application");
    if (FAILED(hr))
    {
        wprintf(L"Failed to compose a resource identifier string: 0x%08lx\n", hr);
        goto Cleanup;        
    }
    RuleGroupName = SysAllocString(pwszTemp);  // Used for grouping together multiple rules
    if (NULL == RuleGroupName)
    {
        wprintf(L"\nERROR: Insufficient memory\n");
        goto Cleanup;
    }
    //    Examples of using indirect strings -
    //    hr = StringCchPrintfW(pwszTemp, STRING_BUFFER_SIZE, L"@EdgeTraversalOptions.exe,-129");
    hr = StringCchPrintfW(pwszTemp, STRING_BUFFER_SIZE, L"Allow EdgeTraversalOptions.exe to receive \
       inbound traffic for TCP protocol from remote machines located within your network as well as \
       from the Internet (i.e from outside of your Edge device like Firewall or NAT)");
    if (FAILED(hr))
    {
        wprintf(L"Failed to compose a resource identifier string: 0x%08lx\n", hr);
        goto Cleanup;        
    }
    RuleDescription = SysAllocString(pwszTemp);
    if (NULL == RuleDescription)
    {
        wprintf(L"\nERROR: Insufficient memory\n");
        goto Cleanup;
    }

    RuleAppPath = SysAllocString(L"%ProgramFiles%\\EdgeTraversalOptions\\EdgeTraversalOptions.exe");
    if (NULL == RuleAppPath)
    {
        wprintf(L"\nERROR: Insufficient memory\n");
        goto Cleanup;
    }

    hr = pNetFwPolicy2->get_Rules(&amp;pNetFwRules);

    if (FAILED(hr))
    {
        wprintf(L"Failed to retrieve firewall rules collection : 0x%08lx\n", hr);
        goto Cleanup;        
    }

    hr = CoCreateInstance(
        __uuidof(NetFwRule),    //CLSID of the class whose object is to be created
        NULL, 
        CLSCTX_INPROC_SERVER, 
        __uuidof(INetFwRule),   // Identifier of the Interface used for communicating with the object
        (void**)&amp;pNetFwRule);

    if (FAILED(hr))
    {
        wprintf(L"CoCreateInstance for INetFwRule failed: 0x%08lx\n", hr);
        goto Cleanup;        
    }

    hr = pNetFwRule->put_Name(RuleName);
    if ( FAILED(hr) )
    {
        wprintf(L"Failed INetFwRule::put_Name failed with error: 0x %x.\n", hr);
        goto Cleanup;
    }

    hr = pNetFwRule->put_Grouping(RuleGroupName);
    if ( FAILED(hr) )
    {
        wprintf(L"Failed INetFwRule::put_Grouping failed with error: 0x %x.\n", hr);
        goto Cleanup;
    }

    hr = pNetFwRule->put_Description(RuleDescription);
    if ( FAILED(hr) )
    {
        wprintf(L"Failed INetFwRule::put_Description failed with error: 0x %x.\n", hr);
        goto Cleanup;
    }

    hr = pNetFwRule->put_Direction(NET_FW_RULE_DIR_IN);
    if ( FAILED(hr) )
    {
        wprintf(L"Failed INetFwRule::put_Direction failed with error: 0x %x.\n", hr);
        goto Cleanup;
    }

    hr = pNetFwRule->put_Action(NET_FW_ACTION_ALLOW);
    if ( FAILED(hr) )
    {
        wprintf(L"Failed INetFwRule::put_Action failed with error: 0x %x.\n", hr);
        goto Cleanup;
    }

    hr = pNetFwRule->put_ApplicationName(RuleAppPath);
    if ( FAILED(hr) )
    {
        wprintf(L"Failed INetFwRule::put_ApplicationName failed with error: 0x %x.\n", hr);
        goto Cleanup;
    }

    hr = pNetFwRule->put_Protocol(6);  // TCP
    if ( FAILED(hr) )
    {
        wprintf(L"Failed INetFwRule::put_Protocol failed with error: 0x %x.\n", hr);
        goto Cleanup;
    }

    hr = pNetFwRule->put_Profiles(NET_FW_PROFILE2_DOMAIN | NET_FW_PROFILE2_PRIVATE);
    if ( FAILED(hr) )
    {
        wprintf(L"Failed INetFwRule::put_Profiles failed with error: 0x %x.\n", hr);
        goto Cleanup;
    }

    hr = pNetFwRule->put_Enabled(VARIANT_TRUE);
    if ( FAILED(hr) )
    {
        wprintf(L"Failed INetFwRule::put_Enabled failed with error: 0x %x.\n", hr);
        goto Cleanup;
    }


    // Check if INetFwRule2 interface is available (i.e Windows7+)
    // If supported, then use EdgeTraversalOptions
    // Else use the EdgeTraversal boolean flag.

    if (SUCCEEDED(pNetFwRule->QueryInterface(__uuidof(INetFwRule2), (void**)&amp;pNetFwRule2)))
    {
        hr = pNetFwRule2->put_EdgeTraversalOptions(NET_FW_EDGE_TRAVERSAL_TYPE_DEFER_TO_APP);
        if ( FAILED(hr) )
        {
            wprintf(L"Failed INetFwRule::put_EdgeTraversalOptions failed with error: 0x %x.\n", hr);
            goto Cleanup;
        }
    }
    else
    {
        hr = pNetFwRule->put_EdgeTraversal(VARIANT_TRUE);
        if ( FAILED(hr) )
        {
            wprintf(L"Failed INetFwRule::put_EdgeTraversal failed with error: 0x %x.\n", hr);
            goto Cleanup;
        }
    }

    hr = pNetFwRules->Add(pNetFwRule);
    if (FAILED(hr))
    {
        wprintf(L"Failed to add firewall rule to the firewall rules collection : 0x%08lx\n", hr);
        goto Cleanup;        
    }

    wprintf(L"Successfully added firewall rule !\n");

Cleanup:
   
    SysFreeString(RuleName);
    SysFreeString(RuleGroupName);
    SysFreeString(RuleDescription);
    SysFreeString(RuleAppPath);

    if (pNetFwRule2 != NULL)
    {
        pNetFwRule2->Release();
    }

    if (pNetFwRule != NULL)
    {
        pNetFwRule->Release();
    }

    if (pNetFwRules != NULL)
    {
        pNetFwRules->Release();
    }

    return hr;
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
        wprintf(L"CoCreateInstance for INetFwPolicy2 failed: 0x%08lx\n", hr);
        goto Cleanup;        
    }

Cleanup:
    return hr;
}


// Release INetFwPolicy2
void WFCOMCleanup(INetFwPolicy2* pNetFwPolicy2)
{
    // Release the INetFwPolicy2 object (Vista+)
    if (pNetFwPolicy2 != NULL)
    {
        pNetFwPolicy2->Release();
    }
}


```



 

 




