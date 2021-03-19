---
title: LISTBOX.insertItem
description: The insertItem method inserts the specified text at the specified index in the list box control.
ms.assetid: c45eb75e-074d-4f3f-bfdd-6c3cbbd71f54
keywords:
- LISTBOX.insertItem Windows Media Player
topic_type:
- apiref
api_name:
- LISTBOX.insertItem
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# LISTBOX.insertItem

The **insertItem** method inserts the specified text at the specified index in the list box control.

``` syntax
        elementID.insertItem(index, text)
```

## Parameters

<dl> <dt>

<span id="index"></span><span id="INDEX"></span>*index*
</dt> <dd>

**Number** (**long**) containing the index of the line to retrieve.

</dd> <dt>

<span id="text"></span><span id="TEXT"></span>*text*
</dt> <dd>

**String** containing the text to be inserted.

</dd> </dl>

## Return Value

This method does not return a value.

## Remarks

When a line is inserted, the line indexes for the lines below the inserted line increase by one.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------|
| Version<br/> | Windows Media Player for Windows XP or later<br/> |



## See also

<dl> <dt>

[**LISTBOX Element**](listbox-element.md)
</dt> </dl>

 

 





