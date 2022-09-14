---
title: PLAYLIST.setCheckedState2
description: The setCheckedState2 method sets the checked state of the item with the specified index in the PLAYLIST element.
ms.assetid: 241221a3-810b-422d-8f73-25c5b5c82c70
keywords:
- PLAYLIST.setCheckedState2 Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.setCheckedState2
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# PLAYLIST.setCheckedState2

The **setCheckedState2** method sets the checked state of the item with the specified index in the **PLAYLIST** element.

``` syntax
        elementID.setCheckedState(item, checked)
```

## Parameters

<dl> <dt>

<span id="item"></span><span id="ITEM"></span>*item*
</dt> <dd>

**Number** (**long**) indicating the index of the playlist item to be checked or unchecked.

</dd> <dt>

<span id="checked"></span><span id="CHECKED"></span>*checked*
</dt> <dd>

**Boolean** indicating whether the specified item is to be checked (true) or unchecked (false).

</dd> </dl>

## Return Value

This method returns a **Boolean**.

## Remarks

This method can work with nested playlists and replaces the **setCheckedState** method, which cannot. You can set all items to the requested state by specifying  1 in the *item* parameter.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> <dt>

[**PLAYLIST.setCheckedState**](playlist-setcheckedstate.md)
</dt> </dl>

 

 





