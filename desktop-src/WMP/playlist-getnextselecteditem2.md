---
title: PLAYLIST.getNextSelectedItem2
description: The getNextSelectedItem2 method retrieves the index of the next selected item in the playlist following the specified index.
ms.assetid: 18acf95c-ab79-4b5c-b904-e13ef9a034dc
keywords:
- PLAYLIST.getNextSelectedItem2 Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.getNextSelectedItem2
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# PLAYLIST.getNextSelectedItem2

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getNextSelectedItem2** method retrieves the index of the next selected item in the playlist following the specified index.

``` syntax
        elementID.getNextSelectedItem2(item)
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

This method can work with nested playlists and replaces the **getNextSelectedItem** method, which cannot. Pass  1 in the *item* parameter to find the first selected item. When there are no further selected items, -1 is returned.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> <dt>

[**PLAYLIST.getNextSelectedItem**](playlist-getnextselecteditem.md)
</dt> </dl>

 

 





