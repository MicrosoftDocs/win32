---
Description: The debug version of the XAudio2 engine validates parameters, and provides detailed warning and error messages.
ms.assetid: a7aaebf9-98d4-e96c-993d-b0d0b7074788
title: XAudio2 Debugging Facilities
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# XAudio2 Debugging Facilities

The debug version of the XAudio2 engine validates parameters, and provides detailed warning and error messages.

## Setting the Debug Logging Level at Run Time

You can set the level of debugging information shown by XAudio2 at any time by filling out an [**XAUDIO2\_DEBUG\_CONFIGURATION**](/windows/win32/xaudio2/ns-xaudio2-xaudio2_debug_configuration?branch=master) structure with the flags for the desired logging level, and then pass the structure to the [**IXAudio2::SetDebugConfiguration**](ixaudio2-interface-setdebugconfiguration.md) method. Values passed to the **IXAudio2::SetDebugConfiguration** method always override any default values that were set in the Windows registry.

## Debug Support

The debugging facilities are always availlabe for XAUDIO2 in Windows 8.

For the DirectX SDK versions of XAUDIO2, you must use **XAUDIO2\_DEBUG\_ENGINE** when creating the XAUDIO2 object with [**XAudio2Create**](/windows/win32/xaudio2/nf-xaudio2-xaudio2create?branch=master) and the system must have the DirectX SDK Developer Runtime installed for debugging to be supported.

## Related topics

<dl> <dt>

[Debugging Facilities](debugging-facilities.md)
</dt> <dt>

[XAudio2 Programming Reference](programming-reference.md)
</dt> </dl>

 

 



