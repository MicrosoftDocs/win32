---
title: Display Area Plug-ins (deprecated)
description: Display Area Plug-ins (deprecated)
ms.assetid: 424e6f9b-3ecf-4172-9eb9-cd2ac532b488
keywords:
- Windows Media Player plug-ins,display area
- plug-ins,display area
- user interface plug-ins,display area
- UI plug-ins,display area
- display area plug-ins
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Display Area Plug-ins (deprecated)

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This page documents a feature that may be unavailable in future versions of Windows Media Player and the Windows Media Player SDK.

Display area UI plug-ins are shown in the main area of the **Now Playing** pane, below the artist and track information and to the left of the playlist area. Only one display area plug-in can be enabled at a time. When a display area plug-in is enabled, the Player cannot enter full screen mode.

Display area plug-ins are useful for displaying large amounts of information. For example, a display area plug-in can retrieve information about the currently playing media item and display related articles, interviews, and reviews. A display area plug-in can host a Microsoft Internet Explorer browser window to display this information using HTML.

> [!Note]  
> A hosted browser window can embed the ActiveX version of Windows Media Player, but this is not recommended because the embedded control cannot communicate with the standalone player that contains it.

 

> [!Note]  
> Windows Media Player closes any open display area plug-in when the user plays content that contains video.

 

## Related topics

<dl> <dt>

[**UI Plug-in Overview**](ui-plug-in-overview.md)
</dt> </dl>

 

 




