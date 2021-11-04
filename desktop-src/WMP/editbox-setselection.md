---
title: EDITBOX.setSelection
description: The setSelection method selects the text in the edit box control from the specified start index to the specified end index.
ms.assetid: 97b20a17-4b9c-4144-b448-8d7611c0e994
keywords:
- EDITBOX.setSelection Windows Media Player
topic_type:
- apiref
api_name:
- EDITBOX.setSelection
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# EDITBOX.setSelection

The **setSelection** method selects the text in the edit box control from the specified start index to the specified end index.

``` syntax
        elementID.setSelection(start, end)
```

## Parameters

<dl> <dt>

<span id="start"></span><span id="START"></span>*start*
</dt> <dd>

**Number** (**long**) containing the character index of the starting position of the selected text.

</dd> <dt>

<span id="end"></span><span id="END"></span>*end*
</dt> <dd>

**Number** (**long**) containing the character index of the ending position of the selected text.

</dd> </dl>

## Return Value

This method does not return a value.

## Remarks

If the start is 0 and the end is  1, all of the text in the edit box control is selected. If the start is  1, any current selection is deselected.

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

[**EDITBOX.replaceSelection**](editbox-replaceselection.md)
</dt> </dl>

 

 





