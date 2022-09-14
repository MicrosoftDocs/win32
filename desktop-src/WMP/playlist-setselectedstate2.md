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
ms.date: 05/31/2018
api_location: 
---

# PLAYLIST.setSelectedState2

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

 

 





