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
ms.date: 05/31/2018
api_location: 
---

# PLAYLIST.getNextSelectedItem2

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

 

 





