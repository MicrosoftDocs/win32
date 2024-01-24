---
title: Windows Media Player DSP Plug-ins
description: Windows Media Player DSP Plug-ins
ms.assetid: 1c7202c4-ca66-491d-9a5f-26032cad1dcc
keywords:
- Windows Media Player,plug-ins
- Windows Media Player,DSP plug-ins
- Windows Media Player plug-ins,digital signal processing (DSP)
- plug-ins,digital signal processing (DSP)
- digital signal processing plug-ins,about
- DSP plug-ins,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Windows Media Player DSP Plug-ins

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Microsoft Windows Media Player provides an architecture that enables the user to install and activate plug-in programs that add digital signal processing (DSP) functionality. A DSP plug-in is a Microsoft DirectX Media Object (DMO) or a Media Foundation Transform (MFT) that connects to the Player by using COM interfaces. A typical DSP plug-in might be an audio equalizer or a video tint control. This section of the SDK provides the programming information you need to create your own DSP plug-in.

The DSP plug-in documentation is divided into the following three sections.



| Section                                                                      | Description                                                                                                                                     |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [About DSP Plug-ins](about-dsp-plug-ins.md)                                 | Provides an overview of the architecture used for DSP plug-ins. Read this section to learn the general concepts involved with this technology.  |
| [DSP Plug-ins Programming Guide](dsp-plug-ins-programming-guide.md)         | Explains what you need to do to create a DSP plug-in. This section contains example code and step-by-step procedures.                           |
| [DSP Plug-ins Programming Reference](dsp-plug-ins-programming-reference.md) | Provides a detailed reference for the COM interfaces, methods, and enumerated types supported by the Windows Media Player SDK for DSP plug-ins. |



 

## Related topics

<dl> <dt>

[**Windows Media Player Plug-ins**](windows-media-player-plug-ins.md)
</dt> </dl>

 

 




