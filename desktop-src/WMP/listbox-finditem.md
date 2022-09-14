---
title: LISTBOX.findItem
description: The findItem method searches for a given string starting with the item following the specified item index.
ms.assetid: 8d112d99-1866-45e5-b0ef-5d4a3c8b388d
keywords:
- LISTBOX.findItem Windows Media Player
topic_type:
- apiref
api_name:
- LISTBOX.findItem
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# LISTBOX.findItem

The **findItem** method searches for a given string starting with the item following the specified item index.

``` syntax
        elementID.findItem(startIndex, searchString)
```

## Parameters

<dl> <dt>

<span id="startIndex"></span><span id="startindex"></span><span id="STARTINDEX"></span>*startIndex*
</dt> <dd>

**Number** (**long**) containing the index of the item at which to start the search.

</dd> <dt>

<span id="searchString"></span><span id="searchstring"></span><span id="SEARCHSTRING"></span>*searchString*
</dt> <dd>

**String** containing the text to search for.

</dd> </dl>

## Return Value

This method returns a **Number** (**long**) containing the index of the item that contains the string.

## Remarks

To start the search at the first line of the list box control, use  1 as the *startIndex*. To continue to search for text after the first line is found, use the returned line index as the *startIndex*, and the search will start at the next line. This method will search for substrings and is not case-sensitive.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------|
| Version<br/> | Windows Media Player for Windows XP or later<br/> |



## See also

<dl> <dt>

[**LISTBOX Element**](listbox-element.md)
</dt> </dl>

 

 





