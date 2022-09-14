---
title: EDITBOX.getSelectionStart
description: The getSelectionStart method retrieves the starting position of the selected text in the editbox control.
ms.assetid: 2d7efe14-549c-4f73-96a7-b8ce88b881ad
keywords:
- EDITBOX.getSelectionStart Windows Media Player
topic_type:
- apiref
api_name:
- EDITBOX.getSelectionStart
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# EDITBOX.getSelectionStart

The **getSelectionStart** method retrieves the starting position of the selected text in the editbox control.

``` syntax
        elementID.getSelectionStart()
```

## Parameters

This method has no parameters.

## Return Value

This method returns a **Number** (**long**).

## Remarks

If no text is selected, this method returns the position of the insertion point.

If the control is multiline, this method returns the character index in the control, not the line index.

This method can only be called after the control becomes visible.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------|
| Version<br/> | Windows Media Player for Windows XP or later<br/> |



## See also

<dl> <dt>

[**EDITBOX Element**](editbox-element.md)
</dt> <dt>

[**EDITBOX.getSelectionEnd**](editbox-getselectionend.md)
</dt> <dt>

[**EDITBOX.replaceSelection**](editbox-replaceselection.md)
</dt> <dt>

[**EDITBOX.setSelection**](editbox-setselection.md)
</dt> </dl>

 

 





