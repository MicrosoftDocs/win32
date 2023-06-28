---
title: Windows Media Metafile Guide
description: Windows Media Metafile Guide
ms.assetid: d2360a63-f073-44b0-8637-1f22b577f51a
keywords:
- Windows Media metafiles,about
- Windows Media Player,metafiles
- Windows Media Player,Windows Media metafiles
- metafiles,about
- Windows Media,metafiles
- Windows Media metafile playlists,about
- playlists,about
- metafile playlists,about
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Windows Media Metafile Guide

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A Windows Media metafile can be as simple or complex as you need it to be. The most basic Windows Media metafile contains only the Uniform Resource Locator (URL) of some multimedia content on a server. The client, Windows Media Player, parses this information and then opens the media file or stream defined in the Windows Media metafile. A complex metafile can contain multiple files or streams arranged in a playlist, instructions on how to play the files or streams, text and graphic elements such as title, author, and copyright text, personalized ad insertion into a live stream, hyperlinks associated with elements on the Windows Media Player interface, and more.

The following sections provide detailed information on how to create and use Windows Media metafile playlists.



| Section                                                            | Description                                                                         |
|--------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [Types of Playlists](types-of-playlists.md)                       | Lists available file name extensions.                                               |
| [Creating Metafile Playlists](creating-metafile-playlists.md)     | Describes how to create Windows Media metafile playlists.                           |
| [Metafile Playlists](metafile-playlists.md)                       | Describes metafile playlist usage, scripting, metadata, and processing.             |
| [Metafile Extension Guidelines](metafile-extension-guidelines.md) | Describes the preferred use of file name extensions for streaming media files.      |
| [Order of Precedence](order-of-precedence.md)                     | Describes how metafile playlist elements override other metafile playlist elements. |



 

## Related topics

<dl> <dt>

[**Windows Media Metafile Elements Reference**](windows-media-metafile-elements-reference.md)
</dt> <dt>

[**Windows Media Metafiles**](windows-media-metafiles.md)
</dt> </dl>

 

 




