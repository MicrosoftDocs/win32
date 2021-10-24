---
description: The debug version of the XAudio2 engine validates parameters, and provides detailed warning and error messages.
ms.assetid: a7aaebf9-98d4-e96c-993d-b0d0b7074788
title: XAudio2 Debugging Facilities
ms.topic: article
ms.date: 05/31/2018
---

# XAudio2 Debugging Facilities

The debug version of the XAudio2 engine validates parameters, and provides detailed warning and error messages.

## Setting the Debug Logging Level at Run Time

You can set the level of debugging information shown by XAudio2 at any time by filling out an [**XAUDIO2\_DEBUG\_CONFIGURATION**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_debug_configuration) structure with the flags for the desired logging level, and then pass the structure to the [**IXAudio2::SetDebugConfiguration**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-setdebugconfiguration) method. Values passed to the **IXAudio2::SetDebugConfiguration** method always override any default values that were set in the Windows registry.

## Debug Support

The debugging facilities are always available for XAUDIO2 in Windows 8.x, Windows 10, Windows 11, and when using the [XAudio2Redist](https://aka.ms/xaudio2redist) package.

> For the legacy DirectX SDK versions of XAUDIO2, you must use **XAUDIO2\_DEBUG\_ENGINE** when creating the XAUDIO2 object with [**XAudio2Create**](/windows/desktop/api/xaudio2/nf-xaudio2-xaudio2create) and the system must have the DirectX SDK Developer Runtime installed for debugging to be supported.

## Enabling Event Tracing for Windows (ETW) for XAudio2

With XAudio 2.8 or later, all debugging information is logged via ETW. To enable logging of these events, use the following steps:

1. Search for "Event Viewer" on your local system and run this application.
2. Select View on the menu bar, and set the check-mark on _Show Analytic and Debug Logs_.
3. Using the tree view, select Applications and Services Logs / Microsoft / Windows / XAudio2.
4. Right-click on *Microsoft Windows XAudio2 debug logging* and select "Properties".
5. Click the check-box on "Enable Log", and hit "OK". You can optionally change the log location which defaults to ``%SystemRoot%\System32\Winevt\Logs\Microsoft-Windows-XAudio2%4Debug.etl``.

Run your scenarios as normal and when you want to see the recent activity, open the ETL log file and look for events. There are a number of tools you can use, including the **Event Viewer** via "Open Saved Log..." in the actions pane.

For more information, see [Event Tracing](/windows/win32/etw/event-tracing-portal).

## Related topics

<dl> <dt>

[Debugging Facilities](debugging-facilities.md)
</dt> <dt>

[XAudio2 Programming Reference](programming-reference.md)
</dt> </dl>

 

 
