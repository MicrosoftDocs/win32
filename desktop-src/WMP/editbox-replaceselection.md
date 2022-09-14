---
title: EDITBOX.replaceSelection
description: The replaceSelection method replaces the current selection with the specified text.
ms.assetid: 600650fb-f0c8-489a-9bf2-04f31705c6b0
keywords:
- EDITBOX.replaceSelection Windows Media Player
topic_type:
- apiref
api_name:
- EDITBOX.replaceSelection
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# EDITBOX.replaceSelection

The **replaceSelection** method replaces the current selection with the specified text.

``` syntax
        elementID.replaceSelection(newValue)
```

## Parameters

<dl> <dt>

<span id="newValue"></span><span id="newvalue"></span><span id="NEWVALUE"></span>*newValue*
</dt> <dd>

**String** containing the text to replace the selected text.

</dd> </dl>

## Return Value

This method does not return a value.

## Remarks

If there is no text selected, the replacement text is inserted at the current location of the insertion point.

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

[**EDITBOX.getSelectionStart**](editbox-getselectionstart.md)
</dt> <dt>

[**EDITBOX.setSelection**](editbox-setselection.md)
</dt> </dl>

 

 





