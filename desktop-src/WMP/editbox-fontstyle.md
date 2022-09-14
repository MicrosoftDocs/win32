---
title: EDITBOX.fontStyle
description: The fontStyle attribute specifies or retrieves the font style for the edit box control.
ms.assetid: bc71359d-2b75-4134-99e8-52b2ca48dcde
keywords:
- EDITBOX.fontStyle Windows Media Player
topic_type:
- apiref
api_name:
- EDITBOX.fontStyle
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# EDITBOX.fontStyle

The **fontStyle** attribute specifies or retrieves the font style for the edit box control.

``` syntax
        elementID.fontStyle
```

## Possible Values

This attribute is a read/write **String** containing one or more of the following values.



| Value     | Description           |
|-----------|-----------------------|
| Bold      | Bold font style.      |
| Italic    | Italic font style.    |
| Underline | Underline font style. |
| Strikeout | Strikeout font style. |
| Normal    | Normal font style.    |



 

## Remarks

Any combination of the values can be used, separated with spaces. The Normal style has priority over all other values, and any others specified along with Normal will be ignored.

For rendering purposes, Normal is the default font style. The default value retrieved from this attribute is "" (empty string).

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------|
| Version<br/> | Windows Media Player for Windows XP or later<br/> |



## See also

<dl> <dt>

[**EDITBOX Element**](editbox-element.md)
</dt> <dt>

[**EDITBOX.fontFace**](editbox-fontface.md)
</dt> <dt>

[**EDITBOX.fontSize**](editbox-fontsize.md)
</dt> </dl>

 

 





