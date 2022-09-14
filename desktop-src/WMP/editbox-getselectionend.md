---
title: EDITBOX.getSelectionEnd
description: The getSelectionEnd method retrieves the ending position of the selected text in the editbox control.
ms.assetid: 82a445da-3c50-41b7-8ac8-da6c860056ba
keywords:
- EDITBOX.getSelectionEnd Windows Media Player
topic_type:
- apiref
api_name:
- EDITBOX.getSelectionEnd
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# EDITBOX.getSelectionEnd

The **getSelectionEnd** method retrieves the ending position of the selected text in the editbox control.

``` syntax
        elementID.getSelectionEnd()
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

[**EDITBOX.getSelectionStart**](editbox-getselectionstart.md)
</dt> <dt>

[**EDITBOX.replaceSelection**](editbox-replaceselection.md)
</dt> <dt>

[**EDITBOX.setSelection**](editbox-setselection.md)
</dt> </dl>

 

 





