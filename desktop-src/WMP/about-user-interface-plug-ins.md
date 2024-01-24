---
title: About User Interface Plug-ins
description: About User Interface Plug-ins
ms.assetid: 2f683876-02b3-48c8-a487-4f665ab7cf91
keywords:
- Windows Media Player,plug-ins
- Windows Media Player,user interface plug-ins
- Windows Media Player plug-ins,user interface
- plug-ins,user interface
- user interface plug-ins,about
- UI plug-ins,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About User Interface Plug-ins

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Windows Media Player provides a variety of control panels that allow the user to modify various aspects of the player such as the video and graphic equalizer settings. These control panels can enhance the multimedia experience provided by Windows Media Player, but they do not necessarily provide all the functionality that the user may be looking for.

Skins are one way to provide additional functionality, but they require the developer to recreate the entire user interface (UI). As an alternative, Windows Media Player allows the creation of custom UI plug-ins that display in the full mode of the player. This functionality is provided through a programming interface that follows standard Microsoft Component Object Model (COM) guidelines. You can implement this interface in Microsoft Visual C++ by using the Windows Media Player Plug-in Wizard to help you get started.

UI plug-ins are described in greater detail in the following topics.



| Topic                                              | Description                                                   |
|----------------------------------------------------|---------------------------------------------------------------|
| [UI Plug-in Overview](ui-plug-in-overview.md)     | Provides an overview of UI plug-ins.                          |
| [Building a UI Plug-in](building-a-ui-plug-in.md) | Provides the technical details needed to create a UI plug-in. |



 

## Related topics

<dl> <dt>

[**Windows Media Player User Interface Plug-ins**](windows-media-player-user-interface-plug-ins.md)
</dt> </dl>

 

 




