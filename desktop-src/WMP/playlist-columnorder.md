---
title: PLAYLIST.columnOrder
description: The columnOrder attribute specifies or retrieves the order of the playlist columns.
ms.assetid: 91a2e15b-1993-4666-98ef-b893df2b570c
keywords:
- PLAYLIST.columnOrder Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.columnOrder
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PLAYLIST.columnOrder

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **columnOrder** attribute specifies or retrieves the order of the playlist columns.

``` syntax
        elementID.columnOrder
```

## Possible Values

This attribute is a read/write **String** specifying a semicolon-delimited list of Playlist column indexes. The default value is "0;1;2;3". Leading and trailing semicolons and spaces should not be present.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> </dl>

 

 





