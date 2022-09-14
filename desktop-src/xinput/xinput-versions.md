---
title: XInput Versions
description: XInput is a cross-platform API that has shipped for use on Xbox and Windows.
ms.assetid: e89a6c81-f170-4385-f942-3606f9747244
ms.topic: article
ms.date: 05/31/2018
---

# XInput Versions

XInput is a cross-platform API that has shipped for use on Xbox and Windows. On Xbox, XInput ships as a static library that is compiled into the main game executable. On Windows, XInput is provided as a DLL that is installed into the system folders of the operating system.

There are three current versions of the XInput DLL today. Choose the appropriate version of XInput based on the functionality of XInput you use and the versions of Windows you intend to support.

- XInput 1.4: XInput 1.4 ships as part of Windows 10. Use this version for building UWP apps.
- XInput 9.1.0: XInput 9.1.0 ships as part of Windows Vista, Windows 7, and Windows 8. Use this version if your desktop app is intended to run on these versions of Windows and you are using basic XInput functionality.
- XInput 1.3: XInput 1.3 ships as a redistributable component in the DirectX SDK with support for Windows Vista, Windows 7, and Windows 8. Use this version if your desktop app is intended to run on these versions of Windows and you need functionality that is not supported by XInput 9.1.0.

## XInput 1.4

XInput 1.4 ships today as a system component in Windows 8 as XINPUT1\_4.DLL. It is available “inbox” and does not require redistribution with an application. The Windows Software Development Kit (SDK) contains the header and import library for statically linking against XINPUT1\_4.DLL. To download the Windows 8 SDK, see [Downloads for developing desktop apps](https://developer.microsoft.com/windows/downloads/).

XInput 1.4 has these primary advantages over other versions of XInput:

-   This is the only version that can be used in C++/DirectX Windows Store apps.
-   The new [**XInputGetAudioDeviceIds**](/windows/desktop/api/XInput/nf-xinput-xinputgetaudiodeviceids) function provides an audio device ID string that you can use to open an XAudio2 mastering voice or audio device for a headset attached to an Xbox common controller. The [**XInputGetDSoundAudioDeviceGuids**](/windows/desktop/api/XInput/nf-xinput-xinputgetdsoundaudiodeviceguids) function is not available in this version.
-   Provides improved device capabilities reporting including XINPUT\_CAPS\_WIRELESS, XINPUT\_CAPS\_FFB\_SUPPORTED, XINPUT\_CAPS\_PMD\_SUPPORTED, and XINPUT\_CAPS\_NO\_NAVIGATION flags and more accurate reporting of XINPUT\_CAPS\_VOICE\_SUPPORTED. These flags are combined in the **Flags** member of the [**XINPUT\_CAPABILITIES**](/windows/desktop/api/XInput/ns-xinput-xinput_capabilities) structure. The [**XInputGetCapabilities**](/windows/desktop/api/XInput/nf-xinput-xinputgetcapabilities) function returns **XINPUT\_CAPABILITIES**.

### XInput 9.1.0

Like XInput 1.4, XInput 9.1.0 ships today as a system component in Windows 10, Windows 8.x, Windows 7, and Windows Vista as XINPUT9\_1\_0.DLL. It is maintained primarily for backward compatibility with existing applications. It has a reduced function set so we recommend that you use XInput 1.4, if possible. But it is convenient to use for applications that must run on down-level versions of Windows but don't need the additional audio functionality provided by XInput 1.4 or XInput 1.3.

The Windows SDK contains the header and import library for statically linking against XINPUT9\_1\_0.DLL.

XInput 9.1.0 has these disadvantages over other versions of XInput:

-   For backward compatibility reasons, [**XInputGetCapabilities**](/windows/desktop/api/XInput/nf-xinput-xinputgetcapabilities) in this version of XInput returns fixed capability information. Regardless of Xbox common controller device attached, **XInputGetCapabilities** in XInput 9.1.0 will always report a device subtype of GAMEPAD. It will not return the XINPUT\_CAPS\_WIRELESS capability bit even if a wireless device is connected.
-   You can't determine the headset for a given user ID. The [**XInputGetAudioDeviceIds**](/windows/desktop/api/XInput/nf-xinput-xinputgetaudiodeviceids) function is not available and [**XInputGetDSoundAudioDeviceGuids**](/windows/desktop/api/XInput/nf-xinput-xinputgetdsoundaudiodeviceguids) function will return no results on Windows 8.x or Windows 10.
-   The [**XInputEnable**](/windows/desktop/api/XInput/nf-xinput-xinputenable), [**XInputGetBatteryInformation**](/windows/desktop/api/XInput/nf-xinput-xinputgetbatteryinformation), and [**XInputGetKeystroke**](/windows/desktop/api/XInput/nf-xinput-xinputgetkeystroke) functions are not available.

### XInput 1.3

Some previous versions of XInput have been provided as redistributable DLLs in the DirectX SDK. The first redistributable version of XInput, XInput 1.1, shipped in the April 2006 release of the DirectX SDK. The last version to ship in the DirectX SDK was XInput 1.3, available in the June 2010 release of the legacy DirectX SDK. *The DirectX SDK is no longer available on Microsoft Downloads*.

You can use XInput 1.3 for applications that support down-level versions of Windows and require functionality not provided by XInput 9.1.0 (that is, correct subtype reporting, audio support, explicit battery reporting support, and so on).
