---
title: DSP Plug-in Enumeration Types
description: DSP Plug-in Enumeration Types
ms.assetid: 7b1b74e6-19de-450a-be89-41277c1cb823
keywords:
- Windows Media Player plug-ins,DSP enumeration types
- Windows Media Player plug-ins,enumeration types
- plug-ins,DSP enumeration types
- plug-ins,enumeration types
- digital signal processing plug-ins,enumeration types
- DSP plug-ins,enumeration types
- enumerations,DSP plug-ins
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DSP Plug-in Enumeration Types

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Windows Media Player SDK implements the following enumeration type for creating DSP plug-ins.



| Enumeration Type                                        | Description                                                                                    |
|---------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [WMPPlugin\_Caps](/previous-versions/windows/desktop/api/wmpservices/ne-wmpservices-wmpplugin_caps)                   | Used with **IWMPPlugin::GetCaps** to indicate whether the plug-in can convert between formats. |
| [WMPServices\_StreamState](/previous-versions/windows/desktop/api/wmpservices/ne-wmpservices-wmpservices_streamstate) | Indicates the whether the stream is currently stopped, paused, or playing.                     |



 

## Related topics

<dl> <dt>

[**DSP Plug-ins Programming Reference**](dsp-plug-ins-programming-reference.md)
</dt> </dl>

 

 




