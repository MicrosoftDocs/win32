---
title: EDITBOX.getLine
description: The getLine method retrieves the text for the line with the specified index.
ms.assetid: a692c32b-86b9-419e-a3a5-464687be04da
keywords:
- EDITBOX.getLine Windows Media Player
topic_type:
- apiref
api_name:
- EDITBOX.getLine
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# EDITBOX.getLine

The **getLine** method retrieves the text for the line with the specified index.

``` syntax
        elementID.getLine(index)
```

## Parameters

<dl> <dt>

<span id="index"></span><span id="INDEX"></span>*index*
</dt> <dd>

**Number** (**long**) containing the index of the line to retrieve.

</dd> </dl>

## Return Value

This method returns a **String**.

## Remarks

If the index is not valid, an empty string is returned. This method can only be called after the control becomes visible.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------|
| Version<br/> | Windows Media Player for Windows XP or later<br/> |



## See also

<dl> <dt>

[**EDITBOX Element**](editbox-element.md)
</dt> <dt>

[**EDITBOX.getLineFromChar**](editbox-getlinefromchar.md)
</dt> <dt>

[**EDITBOX.getLineIndex**](editbox-getlineindex.md)
</dt> </dl>

 

 





