---
title: Windows Media Playlist Elements Reference
description: Windows Media Playlist Elements Reference
ms.assetid: 3f88d46a-59d3-4200-bf99-a3dddae1b0ac
keywords:
- Windows Media Playlists (WPL)
- WPL (Windows Media Playlists)
- Windows Media,Windows Media Playlists (WPL)
- playlists,Windows Media Playlists (WPL)
- reference for Windows Media Playlists
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Windows Media Playlist Elements Reference

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section contains reference documentation for all Windows Media Playlist elements. Reference entries include definitions of the elements, their attributes and values, and special conditions related to each element.

The following playlist elements are supported.



| Element                                    | Description                                                                                                                                                                                          |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [argument](argument-element.md)           | Contains one portion of a condition string.                                                                                                                                                          |
| [body](body-element.md)                   | Contains the elements that define the contents of a playlist.                                                                                                                                        |
| [filter](filter-element.md)               | Contains elements that limit the size of a playlist, duration of a playlist, or number of media items in a playlist.                                                                                 |
| [fragment](fragment-element.md)           | Specifies one condition of the query that selects items from the library.                                                                                                                            |
| [head](head-element.md)                   | Contains metadata that applies to the entire playlist.                                                                                                                                               |
| [media](media-element.md)                 | Specifies one of the media items in a playlist.                                                                                                                                                      |
| [meta](meta-element.md)                   | Specifies metadata that applies to the entire playlist.                                                                                                                                              |
| [querySet](queryset-element.md)           | Contains elements that define which media items will be selected from the library.                                                                                                                   |
| [seq](seq-element.md)                     | Contains elements that define a static playlist or elements that define a smart playlist.                                                                                                            |
| [smartPlaylist](smartplaylist-element.md) | Contains the dynamically defined portion of a playlist.                                                                                                                                              |
| [smil](smil-element.md)                   | The **smil** element is always the top-level element in a Windows Media Playlist (WPL) file. It specifies that the file uses SMIL (Synchronized Multimedia Integration Language) syntax and grammar. |
| [sourceFilter](sourcefilter-element.md)   | Contains elements that select items from a library.                                                                                                                                                  |
| [title](title-element--wpl.md)            | Specifies a title for the playlist.                                                                                                                                                                  |



 

## Related topics

<dl> <dt>

[**Windows Media Playlists**](windows-media-playlists.md)
</dt> </dl>

 

 




