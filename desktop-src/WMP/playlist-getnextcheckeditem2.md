---
title: PLAYLIST.getNextCheckedItem2
description: The getNextCheckedItem2 method retrieves the index of the next checked item in the playlist following the specified index.
ms.assetid: 64e51fd1-eb0f-47e5-8684-96824f4f3194
keywords:
- PLAYLIST.getNextCheckedItem2 Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.getNextCheckedItem2
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# PLAYLIST.getNextCheckedItem2

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getNextCheckedItem2** method retrieves the index of the next checked item in the playlist following the specified index.

``` syntax
        elementID.getNextCheckedItem2(item)
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

This method can work with nested playlists and replaces the **getNextCheckedItem** method, which cannot. Pass  1 in the *item* parameter to find the first checked item. When there are no further checked items, this method returns  1.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> <dt>

[**PLAYLIST.getNextCheckedItem**](playlist-getnextcheckeditem.md)
</dt> </dl>

 

 





