---
title: PLAYLIST.playlist
description: The playlist attribute specifies or retrieves the Playlist object that the PLAYLIST element provides an interface to.
ms.assetid: 4cfbf9d1-8381-4f59-8e6f-9b07f5642c39
keywords:
- PLAYLIST.playlist Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.playlist
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PLAYLIST.playlist

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **playlist** attribute specifies or retrieves the **Playlist** object that the **PLAYLIST** element provides an interface to.

``` syntax
        elementID.playlist
```

## Possible Values

This attribute is a read/write **Playlist** object with no default value.

## Remarks

If the playlist specified is invalid or if no value is specified, the **PLAYLIST** element displays the currently playing media item.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> <dt>

[**Playlist Object**](playlist-object.md)
</dt> </dl>

 

 





