---
title: PLAYLIST.itemCount
description: The itemCount attribute retrieves the number of items currently displayed in the PLAYLIST element.
ms.assetid: d090d95c-e3c3-41bc-951e-ffeb0a314a0c
keywords:
- PLAYLIST.itemCount Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.itemCount
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PLAYLIST.itemCount

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **itemCount** attribute retrieves the number of items currently displayed in the **PLAYLIST** element.

``` syntax
        elementID.itemCount
```

## Possible Values

This attribute is a read-only **Number** (**long**).

## Remarks

The **itemCount** property will count the total number of expanded items. For example, if there are two playlists that contain three media items each, **itemCount** will return 2 if the playlists are not expanded. If only the first playlist is expanded, **itemCount** will return 4. If both playlists are expanded, **itemCount** will return 6.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> </dl>

 

 





