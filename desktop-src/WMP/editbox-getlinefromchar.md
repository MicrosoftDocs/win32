---
title: EDITBOX.getLineFromChar
description: The getLineFromChar method retrieves the line index for the specified character index.
ms.assetid: c3a29bdf-ff63-4b6d-90e8-d414dde87f85
keywords:
- EDITBOX.getLineFromChar Windows Media Player
topic_type:
- apiref
api_name:
- EDITBOX.getLineFromChar
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# EDITBOX.getLineFromChar

The **getLineFromChar** method retrieves the line index for the specified character index.

``` syntax
        elementID.getLineFromChar(index)
```

## Parameters

<dl> <dt>

<span id="index"></span><span id="INDEX"></span>*index*
</dt> <dd>

**Number** (**long**) containing the index of the character whose line index is to be retrieved.

</dd> </dl>

## Return Value

This method returns a **Number** (**long**).

## Remarks

If the specified character position is  1, this method retrieves the line index of the current line.

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

[**EDITBOX.getLineIndex**](editbox-getlineindex.md)
</dt> </dl>

 

 





