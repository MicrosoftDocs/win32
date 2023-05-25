---
title: PLAYLIST.playlistItemsVisible
description: The playlistItemsVisible attribute specifies or retrieves a value indicating whether the Playlist items area is visible.
ms.assetid: 9335bd64-c692-4d11-9912-c611208fbc34
keywords:
- PLAYLIST.playlistItemsVisible Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.playlistItemsVisible
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PLAYLIST.playlistItemsVisible

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **playlistItemsVisible** attribute specifies or retrieves a value indicating whether the Playlist items area is visible.

``` syntax
        elementID.playlistItemsVisible
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                              |
|-------|------------------------------------------|
| true  | Default. Playlist items area is visible. |
| false | Playlist items area is not visible.      |



 

## Remarks

The Playlist items area includes the column headers, the contents of the columns, and the scrollbars (if present).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> </dl>

 

 





