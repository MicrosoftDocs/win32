---
title: Getting Firewall Settings
description: This example gets firewall settings using the Windows Firewall with Advanced Security APIs.C++ /\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ ++ THIS CODE AND INFORMATION IS PROVIDED \ 0034;AS IS \ 0034; WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE. Copyright (C) Microsoft. All Rights Reserved. Abstract This C++ file includes sample code for reading Windows Firewall Settings per profile using the Microsoft Windows Firewall APIs. --\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ / \ include windows.h \ include stdio.h \ include netfw.h \ pragma comment( lib, \ 0034;ole32.lib \ 0034; ) // Forward declarations void Get\_FirewallSettings\_PerProfileType(NET\_FW\_PROFILE\_TYPE2 ProfileTypePassed, INetFwPolicy2\ pNetFwPolicy2); HRESULT WFCOMInitialize(INetFwPolicy2\ \ ppNetFwPolicy2); int \_\_cdecl main() HRESULT hrComInit S\_OK; HRESULT hr S\_OK; INetFwPolicy2 \ pNetFwPolicy2 NULL; // Initialize COM. hrComInit CoInitializeEx( 0, COINIT\_APARTMENTTHREADED ); // Ignore RPC\_E\_CHANGED\_MODE; this just means that COM has already been // initialized with a different mode. Since we don't care what the mode is, // we'll just use the existing mode. if (hrComInit RPC\_E\_CHANGED\_MODE) if (FAILED(hrComInit)) printf( \ 0034;CoInitializeEx failed 0x 08lx\\n \ 0034;, hrComInit); goto Cleanup; // Retrieve INetFwPolicy2 hr WFCOMInitialize( pNetFwPolicy2); if (FAILED(hr)) goto Cleanup; printf( \ 0034;Settings for the firewall domain profile \\n \ 0034;); Get\_FirewallSettings\_PerProfileType(NET\_FW\_PROFILE2\_DOMAIN, pNetFwPolicy2); printf( \ 0034;Settings for the firewall private profile \\n \ 0034;); Get\_FirewallSettings\_PerProfileType(NET\_FW\_PROFILE2\_PRIVATE, pNetFwPolicy2); printf( \ 0034;Settings for the firewall public profile \\n \ 0034;); Get\_FirewallSettings\_PerProfileType(NET\_FW\_PROFILE2\_PUBLIC, pNetFwPolicy2); Cleanup // Release INetFwPolicy2 if (pNetFwPolicy2 NULL) pNetFwPolicy2- Release(); // Uninitialize COM. if (SUCCEEDED(hrComInit)) CoUninitialize(); return 0; void Get\_FirewallSettings\_PerProfileType(NET\_FW\_PROFILE\_TYPE2 ProfileTypePassed, INetFwPolicy2\ pNetFwPolicy2) VARIANT\_BOOL bIsEnabled FALSE; NET\_FW\_ACTION action; printf( \ 0034;\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \\n \ 0034;); if(SUCCEEDED(pNetFwPolicy2- get\_FirewallEnabled(ProfileTypePassed, bIsEnabled))) printf ( \ 0034;Firewall is s\\n \ 0034;, bIsEnabled \ 0034;enabled \ 0034; \ 0034;disabled \ 0034;); if(SUCCEEDED(pNetFwPolicy2- get\_BlockAllInboundTraffic(ProfileTypePassed, bIsEnabled))) printf ( \ 0034;Block all inbound traffic is s\\n \ 0034;, bIsEnabled \ 0034;enabled \ 0034; \ 0034;disabled \ 0034;); if(SUCCEEDED(pNetFwPolicy2- get\_NotificationsDisabled(ProfileTypePassed, bIsEnabled))) printf ( \ 0034;Notifications are s\\n \ 0034;, bIsEnabled \ 0034;disabled \ 0034; \ 0034;enabled \ 0034;); if(SUCCEEDED(pNetFwPolicy2- get\_UnicastResponsesToMulticastBroadcastDisabled(ProfileTypePassed, bIsEnabled))) printf ( \ 0034;UnicastResponsesToMulticastBroadcast is s\\n \ 0034;, bIsEnabled \ 0034;disabled \ 0034; \ 0034;enabled \ 0034;); if(SUCCEEDED(pNetFwPolicy2- get\_DefaultInboundAction(ProfileTypePassed, action))) printf ( \ 0034;Default inbound action is s\\n \ 0034;, action NET\_FW\_ACTION\_BLOCK \ 0034;Allow \ 0034; \ 0034;Block \ 0034;); if(SUCCEEDED(pNetFwPolicy2- get\_DefaultOutboundAction(ProfileTypePassed, action))) printf ( \ 0034;Default outbound action is s\\n \ 0034;, action NET\_FW\_ACTION\_BLOCK \ 0034;Allow \ 0034; \ 0034;Block \ 0034;); printf( \ 0034;\\n \ 0034;); // Instantiate INetFwPolicy2 HRESULT WFCOMInitialize(INetFwPolicy2\ \ ppNetFwPolicy2) HRESULT hr S\_OK; hr CoCreateInstance( \_\_uuidof(NetFwPolicy2), NULL, CLSCTX\_INPROC\_SERVER, \_\_uuidof(INetFwPolicy2), (void\ \ )ppNetFwPolicy2); if (FAILED(hr)) printf( \ 0034;CoCreateInstance for INetFwPolicy2 failed 0x 08lx\\n \ 0034;, hr); goto Cleanup; Cleanup return hr;
ms.assetid: 4281d260-c182-4e59-9a4b-cc13dd63d730
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Getting Firewall Settings

This example gets firewall settings using the Windows Firewall with Advanced Security APIs.


```C++
 
/********************************************************************++
THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft. All Rights Reserved.

Abstract:
    This C++ file includes sample code for reading Windows Firewall 
    Settings per profile using the Microsoft Windows Firewall APIs.

--********************************************************************/

#include <windows.h>
#include <stdio.h>
#include <netfw.h>

#pragma comment( lib, "ole32.lib" )


// Forward declarations
void        Get_FirewallSettings_PerProfileType(NET_FW_PROFILE_TYPE2 ProfileTypePassed, INetFwPolicy2* pNetFwPolicy2);
HRESULT     WFCOMInitialize(INetFwPolicy2** ppNetFwPolicy2);


int __cdecl main()
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

    printf("Settings for the firewall domain profile:\n");
    Get_FirewallSettings_PerProfileType(NET_FW_PROFILE2_DOMAIN, pNetFwPolicy2);

    printf("Settings for the firewall private profile:\n");
    Get_FirewallSettings_PerProfileType(NET_FW_PROFILE2_PRIVATE, pNetFwPolicy2);

    printf("Settings for the firewall public profile:\n");
    Get_FirewallSettings_PerProfileType(NET_FW_PROFILE2_PUBLIC, pNetFwPolicy2);

Cleanup:

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

void Get_FirewallSettings_PerProfileType(NET_FW_PROFILE_TYPE2 ProfileTypePassed, INetFwPolicy2* pNetFwPolicy2)
{
    VARIANT_BOOL bIsEnabled = FALSE;
    NET_FW_ACTION action;

    printf("******************************************\n");   

    if(SUCCEEDED(pNetFwPolicy2->get_FirewallEnabled(ProfileTypePassed, &amp;bIsEnabled)))
    {
        printf ("Firewall is %s\n", bIsEnabled ? "enabled" : "disabled");
    }

    if(SUCCEEDED(pNetFwPolicy2->get_BlockAllInboundTraffic(ProfileTypePassed, &amp;bIsEnabled)))
    {
        printf ("Block all inbound traffic is %s\n", bIsEnabled ? "enabled" : "disabled");
    }

    if(SUCCEEDED(pNetFwPolicy2->get_NotificationsDisabled(ProfileTypePassed, &amp;bIsEnabled)))
    {
        printf ("Notifications are %s\n", bIsEnabled ? "disabled" : "enabled");
    }

    if(SUCCEEDED(pNetFwPolicy2->get_UnicastResponsesToMulticastBroadcastDisabled(ProfileTypePassed, &amp;bIsEnabled)))
    {
        printf ("UnicastResponsesToMulticastBroadcast is %s\n", bIsEnabled ? "disabled" : "enabled");
    }

    if(SUCCEEDED(pNetFwPolicy2->get_DefaultInboundAction(ProfileTypePassed, &amp;action)))
    {
        printf ("Default inbound action is %s\n", action != NET_FW_ACTION_BLOCK ? "Allow" : "Block");
    }

    if(SUCCEEDED(pNetFwPolicy2->get_DefaultOutboundAction(ProfileTypePassed, &amp;action)))
    {
        printf ("Default outbound action is %s\n", action != NET_FW_ACTION_BLOCK ? "Allow" : "Block");
    }

    printf("\n");
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



 

 




