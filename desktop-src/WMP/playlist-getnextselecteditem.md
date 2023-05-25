---
title: PLAYLIST.getNextSelectedItem
description: The getNextSelectedItem method retrieves the index of the next selected item in the playlist following the specified index.
ms.assetid: d46d3a65-8863-4a2f-9add-0701c8283a6b
keywords:
- PLAYLIST.getNextSelectedItem Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.getNextSelectedItem
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# PLAYLIST.getNextSelectedItem

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getNextSelectedItem** method retrieves the index of the next selected item in the playlist following the specified index.

``` syntax
        elementID.getNextSelectedItem(item)
```

## Parameters

<dl> <dt>

<span id="item"></span><span id="ITEM"></span>*item*
</dt> <dd>

**Number** (**long**) indicating the index of the item to search after.

</dd> </dl>

## Return Value

This method returns a **Number** (**long**).

## Remarks

When there are no further selected items, this method returns  1.

This method has been replaced by **getNextSelectedItem2**, which supports nested playlists.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> <dt>

[**PLAYLIST.getNextSelectedItem2**](playlist-getnextselecteditem2.md)
</dt> </dl>

 

 





