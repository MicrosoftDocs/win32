---
title: PLAYLIST.setSelectedState2
description: The setSelectedState2 method sets the selected state of the item with the specified index in the PLAYLIST element.
ms.assetid: 990b834a-f7ed-45b8-99e1-3efd7f4447f4
keywords:
- PLAYLIST.setSelectedState2 Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.setSelectedState2
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# PLAYLIST.setSelectedState2

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **setSelectedState2** method sets the selected state of the item with the specified index in the **PLAYLIST** element.

``` syntax
        elementID.setSelectedState2(item, selected)
```

## Parameters

<dl> <dt>

<span id="item"></span><span id="ITEM"></span>*item*
</dt> <dd>

**Number** (**long**) indicating the index of an item in the playlist.

</dd> <dt>

<span id="selected"></span><span id="SELECTED"></span>*selected*
</dt> <dd>

**Boolean** indicating whether the specified item is to be selected (true) or unselected (false).

</dd> </dl>

## Return Value

This method does not return a value.

## Remarks

This method can work with nested playlists and replaces the **setSelectedState** method which cannot. You can set all items to the requested state by specifying  1 in the *item* parameter.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> <dt>

[**PLAYLIST.setSelectedState**](playlist-setselectedstate.md)
</dt> </dl>

 

 





