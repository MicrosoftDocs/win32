---
title: EDITBOX.getLineIndex
description: The getLineIndex method retrieves the character index of the first character on the line with the specified line index.
ms.assetid: 1298227a-d839-44fc-bacb-44c3c968bd94
keywords:
- EDITBOX.getLineIndex Windows Media Player
topic_type:
- apiref
api_name:
- EDITBOX.getLineIndex
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# EDITBOX.getLineIndex

The **getLineIndex** method retrieves the character index of the first character on the line with the specified line index.

``` syntax
        elementID.getLineIndex(index)
```

## Parameters

<dl> <dt>

<span id="index"></span><span id="INDEX"></span>*index*
</dt> <dd>

**Number** (**long**) containing the index of the line whose character index is to be retrieved.

</dd> </dl>

## Return Value

This method returns a **Number** (**long**).

## Remarks

If the specified line index is  1, the line containing the insertion point is used.

This method can only be called after the control becomes visible.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------|
| Version<br/> | Windows Media Player for Windows XP or later<br/> |



## See also

<dl> <dt>

[**EDITBOX Element**](editbox-element.md)
</dt> <dt>

[**EDITBOX.getLine**](editbox-getline.md)
</dt> <dt>

[**EDITBOX.getLineFromChar**](editbox-getlinefromchar.md)
</dt> </dl>

 

 





