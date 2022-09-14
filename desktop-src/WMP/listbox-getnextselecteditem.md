---
title: LISTBOX.getNextSelectedItem
description: The getNextSelectedItem method retrieves the next selected item in the list box control starting at the item after the one with the specified index.
ms.assetid: 060d196d-2b14-4386-ba01-34256c137db5
keywords:
- LISTBOX.getNextSelectedItem Windows Media Player
topic_type:
- apiref
api_name:
- LISTBOX.getNextSelectedItem
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# LISTBOX.getNextSelectedItem

The **getNextSelectedItem** method retrieves the next selected item in the list box control starting at the item after the one with the specified index.

``` syntax
        elementID.getNextSelectedItem(startIndex)
```

## Parameters

<dl> <dt>

<span id="startIndex"></span><span id="startindex"></span><span id="STARTINDEX"></span>*startIndex*
</dt> <dd>

**Number** (**long**) containing the index of the item that precedes the item being retrieved.

</dd> </dl>

## Return Value

This method returns a **Number** (**long**) containing the index of the next selected item.

## Remarks

To start search from the beginning, use  1 for the start index.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------|
| Version<br/> | Windows Media Player for Windows XP or later<br/> |



## See also

<dl> <dt>

[**LISTBOX Element**](listbox-element.md)
</dt> </dl>

 

 





