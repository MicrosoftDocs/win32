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
ms.date: 05/31/2018
api_location: 
---

# PLAYLIST.getNextCheckedItem2

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

 

 





