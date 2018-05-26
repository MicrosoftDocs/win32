---
title: Restricting Service
description: This example restricts service using the Windows Firewall with Advanced Security APIs.C++/\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ ++ Copyright (C) Microsoft.
ms.assetid: 7454ceb9-d4ec-44d1-8245-0f2766a56501
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Restricting Service

This example restricts service using the Windows Firewall with Advanced Security APIs.


```C++
/********************************************************************++
Copyright (C) Microsoft. All Rights Reserved.

Abstract:
    This C++ file includes sample code that restricts a service using
    the Microsoft Windows Firewall APIs.

--********************************************************************/


#include <windows.h>
#include <stdio.h>
#include <netfw.h>

#pragma comment( lib, "ole32.lib" )
#pragma comment( lib, "oleaut32.lib" )


// Forward declarations
HRESULT     WFCOMInitialize(INetFwPolicy2** ppNetFwPolicy2);


int __cdecl main()
{
    HRESULT hrComInit = S_OK;
    HRESULT hr = S_OK;

    INetFwRules *pFwRules = NULL;
    INetFwRule *pFwRule = NULL;

    VARIANT_BOOL isServiceRestricted = FALSE;

    INetFwPolicy2 *pNetFwPolicy2 = NULL;
    INetFwServiceRestriction *pFwServiceRestriction = NULL;

    // The Service and App name to use
    BSTR bstrServiceName = SysAllocString(L"SampleService");   // provide a valid service short name here.
    BSTR bstrAppName = SysAllocString(L"%systemDrive%\\WINDOWS\\system32\\svchost.exe");
    // The rule name, description should be provided as indirect strings '@appfullpath,-resource index' for
    // localization purposes. 
    // Using the strings directly for illustration here.
    BSTR bstrRuleName = SysAllocString(L"Allow TCP 12345 to sampleservice");
    BSTR bstrRuleDescription = SysAllocString(L"Allow only TCP 12345 traffic to sampleservice service, block everything else");
    BSTR bstrRuleLPorts = SysAllocString(L"12345");

    // Error checking for BSTR allocations
    if (NULL == bstrServiceName) { printf("Failed to allocate bstrServiceName\n"); goto Cleanup; }
    if (NULL == bstrAppName) { printf("Failed to allocate bstrAppName\n"); goto Cleanup; }
    if (NULL == bstrRuleName) { printf("Failed to allocate bstrRuleName\n"); goto Cleanup; }
    if (NULL == bstrRuleDescription) { printf("Failed to allocate bstrRuleDescription\n"); goto Cleanup; }
    if (NULL == bstrRuleLPorts) { printf("Failed to allocate bstrRuleLPorts\n"); goto Cleanup; }

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

    // Retrieve INetFwServiceRestriction
    hr = pNetFwPolicy2->get_ServiceRestriction(&amp;pFwServiceRestriction);
    if (FAILED(hr))
    {
        printf("get_ServiceRestriction failed: 0x%08lx\n", hr);
        goto Cleanup;
    }

    // Restrict the sampleservice Service.
    // This will add two WSH rules -
    //    - a default block all inbound traffic to the service
    //    - a default block all outbound traffic from the service
    hr = pFwServiceRestriction->RestrictService(bstrServiceName, bstrAppName, TRUE, FALSE);
    if (FAILED(hr))
    {
        printf("RestrictService failed: 0x%08lx\nMake sure you specified a valid service shortname.\n", hr);
        goto Cleanup;
    }

    // If the service does not send/receive any network traffic then you are done. You can skip adding the allow WSH rules below.

    // If the service requires sending/receiving certain traffic, then add 'allow' WSH rules as follows

    // Get the collections of Windows Service Hardening networking rules first
    hr = pFwServiceRestriction->get_Rules(&amp;pFwRules);
    if (FAILED(hr))
    {
        wprintf(L"get_Rules failed: 0x%08lx\n", hr);
        goto Cleanup;
    }

    // Add inbound WSH allow rule for allowing TCP 12345 to the service
    // Create a new Rule object.
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

    // Populate the Rule Name
    hr = pFwRule->put_Name(bstrRuleName);
    if (FAILED(hr))
    {
        printf("put_Name failed: 0x%08lx\n", hr);
        goto Cleanup;
    }

    // Populate the Rule Description
    hr = pFwRule->put_Description(bstrRuleDescription);
    if (FAILED(hr))
    {
        printf("put_Description failed: 0x%08lx\n", hr);
        goto Cleanup;
    }
    
    // Populate the Application Name
    hr = pFwRule->put_ApplicationName(bstrAppName);
    if (FAILED(hr))
    {
        printf("put_ApplicationName failed: 0x%08lx\n", hr);
        goto Cleanup;
    }

    // Populate the Service Name
    hr = pFwRule->put_ServiceName(bstrServiceName);
    if (FAILED(hr))
    {
        printf("put_ServiceName failed: 0x%08lx\n", hr);
        goto Cleanup;
    }

    // Populate the Protocol
    hr = pFwRule->put_Protocol(NET_FW_IP_PROTOCOL_TCP);
    if (FAILED(hr))
    {
        printf("put_Protocol failed: 0x%08lx\n", hr);
        goto Cleanup;
    }

    // Populate the Local Ports
    hr = pFwRule->put_LocalPorts(bstrRuleLPorts);
    if (FAILED(hr))
    {
        printf("put_LocalPorts failed: 0x%08lx\n", hr);
        goto Cleanup;
    }

    // Populate the rule Action
    hr = pFwRule->put_Action(NET_FW_ACTION_ALLOW);
    if (FAILED(hr))
    {
        printf("put_Action failed: 0x%08lx\n", hr);
        goto Cleanup;
    }

    // Populate the rule Enabled setting
    hr = pFwRule->put_Enabled(VARIANT_TRUE);
    if (FAILED(hr))
    {
        printf("put_Enabled failed: 0x%08lx\n", hr);
        goto Cleanup;
    }

    // Add the Rule to the collection of Windows Service Hardening(WSH) rules
    hr = pFwRules->Add(pFwRule);
    if (FAILED(hr))
    {
        printf("Firewall Rule Add failed: 0x%08lx\n", hr);
        goto Cleanup;
    }

    Sleep(3000);

    // Check to see if the Service is Restricted
    hr = pFwServiceRestriction->ServiceRestricted(bstrServiceName, bstrAppName, &amp;isServiceRestricted);
    if (FAILED(hr))
    {
        printf("ServiceRestricted failed: 0x%08lx\n", hr);
        goto Cleanup;
    }

    if (isServiceRestricted)
    {
        printf ("Service was successfully restricted in WSH.\nExcept for TCP 12345 inbound traffic and its responses, all other inbound and outbound connections to and from the service will be blocked.\n");
    }
    else
    {
        printf ("The Service could not be properly restricted.\n");
    }


Cleanup:

    // Free BSTR's
    SysFreeString(bstrServiceName);
    SysFreeString(bstrAppName);
    SysFreeString(bstrRuleName);
    SysFreeString(bstrRuleDescription);
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

    // Release INetFwPolicy2
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



 

 




