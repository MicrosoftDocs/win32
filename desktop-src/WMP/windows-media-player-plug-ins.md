---
title: Windows Media Player Plug-ins
description: Windows Media Player Plug-ins
ms.assetid: 6265084b-e1ff-455b-aca8-dc008d94ed43
keywords:
- Windows Media Player,plug-ins
- Windows Media Player plug-ins,about
- plug-ins,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Windows Media Player Plug-ins

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Microsoft Windows Media Player exposes interfaces that allow you to extend functionality in several ways. The following sections describe the supported plug-in architectures and the process of building a plug-in:



| Section                                                                                                         | Description                                                                                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Building a Plug-in](building-a-plug-in.md)                                                                    | You can build several types of plug-ins by using Visual Studio and the Windows Media Player plug-in wizard.                                                                                                                                                                                             |
| [Windows Media Player Custom Visualizations](windows-media-player-custom-visualizations.md)                    | Windows Media Player visualizations are Component Object Model (COM) objects used to display visual imagery that is synchronized to the audio portion of the media playback of the player. Custom visualizations can be created using Microsoft Visual C++.                                             |
| [Windows Media Player User Interface Plug-ins](windows-media-player-user-interface-plug-ins.md)                | Windows Media Player user interface plug-ins add new functionality to the **Now Playing** pane of the full mode Player. You can create plug-ins that use the visualization area, a separate window, the settings area, the metadata area, or background plug-ins that expose no visible user interface. |
| [Windows Media Player DSP Plug-ins](windows-media-player-dsp-plug-ins.md)                                      | Windows Media Player DSP plug-ins modify or process audio and video data before it is rendered by the Player. DSP plug-ins are DirectX Media Objects (DMO) that connect to the Player through COM interfaces.                                                                                           |
| [Windows Media Player Rendering Plug-ins (deprecated)](/previous-versions/windows/desktop/legacy/dd564683(v=vs.85)) | Windows Media Player rendering plug-ins decode (if necessary) and render custom data contained in a Windows Media format stream. Rendering plug-ins are DirectX Media Objects (DMO) that connect to the Player through COM interfaces.                                                                  |
| [Windows Media Player Conversion Plug-ins](windows-media-player-conversion-plug-ins.md)                        | Windows Media Player conversion plug-ins convert digital media files that are created using technologies not provided by Microsoft, into Advanced Systems Format (ASF).                                                                                                                                 |



 

## Related topics

<dl> <dt>

[**Windows Media Player SDK**](windows-media-player-sdk.md)
</dt> </dl>

 

 