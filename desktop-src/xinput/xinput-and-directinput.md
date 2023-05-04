---
title: Comparison of XInput and DirectInput features
description: Compares XInput and DirectInput APIs and features.
ms.assetid: 0f29a47b-24ed-c0fa-e9e9-8a061619845c
ms.topic: article
ms.date: 11/24/2021
ms.custom: seo-windows-dev
---

# Comparison of XInput and DirectInput features

> [!IMPORTANT]  
> See [GameInput API](/gaming/gdk/_content/gc/input/overviews/input-overview) for details on the next-generation input API supported on PC and Xbox through the [Microsoft Game Development Kit (GDK)](/gaming/gdk/).

This document compares XInput and [DirectInput](/previous-versions/windows/desktop/ee416842(v=vs.85)) implementations of the Xbox Controller and how to support both XInput devices and legacy DirectInput devices.

**Windows Store apps do not support [DirectInput](/previous-versions/windows/desktop/ee416842(v=vs.85)).**

## Overview

XInput enables applications to receive input from the Xbox Controller for Windows. The APIs are available through the DirectX SDK, and the driver is available through Windows Update.

There are several advantages to using XInput over [DirectInput](/previous-versions/windows/desktop/ee416842(v=vs.85)):

-   XInput is easier to use and requires less setup than [DirectInput](/previous-versions/windows/desktop/ee416842(v=vs.85))
-   Both Xbox and Windows programming will use the same sets of core APIs, allowing programming to translate cross-platform much easier
-   There will be a large installed base of Xbox controllers
-   XInput devices (that is, the Xbox controllers) will have vibration functionality only when using XInput APIs
-   Future controllers released for the Xbox console (that is, steering wheels) will also work on Windows

### Using the Xbox Controller with DirectInput

The Xbox Controller is properly enumerated on [DirectInput](/previous-versions/windows/desktop/ee416842(v=vs.85)), and can be used with the DirectInputAPIs. However, some functionality provided by XInput will be missing from the DirectInput implementation:

-   The left and right trigger buttons will act as a single button, not independently
-   The vibration effects will not be available
-   Querying for headset devices will not be available

The combination of the left and right triggers in [DirectInput](/previous-versions/windows/desktop/ee416842(v=vs.85)) is by design. Games have always assumed that DirectInput device axes are centered when there is no user interaction with the device. However, the Xbox controller was designed to register minimum value, not center, when the triggers are not being held. Older games would therefore assume user interaction.

The solution was to combine the triggers, setting one trigger to a positive direction and the other to a negative direction, so no user interaction is indicative to [DirectInput](/previous-versions/windows/desktop/ee416842(v=vs.85)) of the "control" being at center.

In order to test the trigger values separately, you must use XInput.

## XInput and DirectInput Side by Side

By supporting XInput only, your game will not work with legacy [DirectInput](/previous-versions/windows/desktop/ee416842(v=vs.85)) devices. XInput will not recognize these devices.

If you want your game to support legacy [DirectInput](/previous-versions/windows/desktop/ee416842(v=vs.85)) devices, you may use DirectInput and XInput side by side. When enumerating your DirectInput devices, all DirectInput devices will enumerate correctly. All XInput devices will show up as both XInput and DirectInput devices, but they should not be handled through DirectInput. You will need to determine which of your DirectInput devices are legacy devices, and which are XInput devices, and remove them from the enumeration of DirectInput devices.

To do this, insert this code into your DirectInput enumeration callback:

```cpp
#include <wbemidl.h>
#include <oleauto.h>

#ifndef SAFE_RELEASE
#define SAFE_RELEASE(p) { if (p) { (p)->Release(); (p) = nullptr; } }
#endif

//-----------------------------------------------------------------------------
// Enum each PNP device using WMI and check each device ID to see if it contains 
// "IG_" (ex. "VID_045E&PID_028E&IG_00").  If it does, then it's an XInput device
// Unfortunately this information can not be found by just using DirectInput 
//-----------------------------------------------------------------------------
BOOL IsXInputDevice( const GUID* pGuidProductFromDirectInput )
{
    IWbemLocator*           pIWbemLocator = nullptr;
    IEnumWbemClassObject*   pEnumDevices = nullptr;
    IWbemClassObject*       pDevices[20] = {};
    IWbemServices*          pIWbemServices = nullptr;
    BSTR                    bstrNamespace = nullptr;
    BSTR                    bstrDeviceID = nullptr;
    BSTR                    bstrClassName = nullptr;
    bool                    bIsXinputDevice = false;
    
    // CoInit if needed
    HRESULT hr = CoInitialize(nullptr);
    bool bCleanupCOM = SUCCEEDED(hr);

    // So we can call VariantClear() later, even if we never had a successful IWbemClassObject::Get().
    VARIANT var = {};
    VariantInit(&var);

    // Create WMI
    hr = CoCreateInstance(__uuidof(WbemLocator),
        nullptr,
        CLSCTX_INPROC_SERVER,
        __uuidof(IWbemLocator),
        (LPVOID*)&pIWbemLocator);
    if (FAILED(hr) || pIWbemLocator == nullptr)
        goto LCleanup;

    bstrNamespace = SysAllocString(L"\\\\.\\root\\cimv2");  if (bstrNamespace == nullptr) goto LCleanup;
    bstrClassName = SysAllocString(L"Win32_PNPEntity");     if (bstrClassName == nullptr) goto LCleanup;
    bstrDeviceID = SysAllocString(L"DeviceID");             if (bstrDeviceID == nullptr)  goto LCleanup;
    
    // Connect to WMI 
    hr = pIWbemLocator->ConnectServer(bstrNamespace, nullptr, nullptr, 0L,
        0L, nullptr, nullptr, &pIWbemServices);
    if (FAILED(hr) || pIWbemServices == nullptr)
        goto LCleanup;

    // Switch security level to IMPERSONATE. 
    hr = CoSetProxyBlanket(pIWbemServices,
        RPC_C_AUTHN_WINNT, RPC_C_AUTHZ_NONE, nullptr,
        RPC_C_AUTHN_LEVEL_CALL, RPC_C_IMP_LEVEL_IMPERSONATE,
        nullptr, EOAC_NONE);
    if ( FAILED(hr) )
        goto LCleanup;

    hr = pIWbemServices->CreateInstanceEnum(bstrClassName, 0, nullptr, &pEnumDevices);
    if (FAILED(hr) || pEnumDevices == nullptr)
        goto LCleanup;

    // Loop over all devices
    for (;;)
    {
        ULONG uReturned = 0;
        hr = pEnumDevices->Next(10000, _countof(pDevices), pDevices, &uReturned);
        if (FAILED(hr))
            goto LCleanup;
        if (uReturned == 0)
            break;

        for (size_t iDevice = 0; iDevice < uReturned; ++iDevice)
        {
            // For each device, get its device ID
            hr = pDevices[iDevice]->Get(bstrDeviceID, 0L, &var, nullptr, nullptr);
            if (SUCCEEDED(hr) && var.vt == VT_BSTR && var.bstrVal != nullptr)
            {
                // Check if the device ID contains "IG_".  If it does, then it's an XInput device
                // This information can not be found from DirectInput 
                if (wcsstr(var.bstrVal, L"IG_"))
                {
                    // If it does, then get the VID/PID from var.bstrVal
                    DWORD dwPid = 0, dwVid = 0;
                    WCHAR* strVid = wcsstr(var.bstrVal, L"VID_");
                    if (strVid && swscanf_s(strVid, L"VID_%4X", &dwVid) != 1)
                        dwVid = 0;
                    WCHAR* strPid = wcsstr(var.bstrVal, L"PID_");
                    if (strPid && swscanf_s(strPid, L"PID_%4X", &dwPid) != 1)
                        dwPid = 0;

                    // Compare the VID/PID to the DInput device
                    DWORD dwVidPid = MAKELONG(dwVid, dwPid);
                    if (dwVidPid == pGuidProductFromDirectInput->Data1)
                    {
                        bIsXinputDevice = true;
                        goto LCleanup;
                    }
                }
            }
            VariantClear(&var);
            SAFE_RELEASE(pDevices[iDevice]);
        }
    }

LCleanup:
    VariantClear(&var);
    
    if(bstrNamespace)
        SysFreeString(bstrNamespace);
    if(bstrDeviceID)
        SysFreeString(bstrDeviceID);
    if(bstrClassName)
        SysFreeString(bstrClassName);
        
    for (size_t iDevice = 0; iDevice < _countof(pDevices); ++iDevice)
        SAFE_RELEASE(pDevices[iDevice]);

    SAFE_RELEASE(pEnumDevices);
    SAFE_RELEASE(pIWbemLocator);
    SAFE_RELEASE(pIWbemServices);

    if(bCleanupCOM)
        CoUninitialize();

    return bIsXinputDevice;
}


//-----------------------------------------------------------------------------
// Name: EnumJoysticksCallback()
// Desc: Called once for each enumerated joystick. If we find one, create a
//       device interface on it so we can play with it.
//-----------------------------------------------------------------------------
BOOL CALLBACK EnumJoysticksCallback( const DIDEVICEINSTANCE* pdidInstance,
                                     VOID* pContext )
{
    if( IsXInputDevice( &pdidInstance->guidProduct ) )
        return DIENUM_CONTINUE;

     // Device is verified not XInput, so add it to the list of DInput devices

     return DIENUM_CONTINUE;    
}
```

> A slightly improved version of this code is in the legacy DirectInput [Joystick](https://github.com/walbourn/directx-sdk-samples/tree/master/DirectInput/Joystick) sample.

## Related topics

[Getting Started With XInput](getting-started-with-xinput.md)

[Programming Reference](programming-reference.md)
