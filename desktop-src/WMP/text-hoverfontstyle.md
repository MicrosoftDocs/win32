---
title: TEXT.hoverFontStyle
description: The hoverFontStyle attribute specifies or retrieves the font style used for the Text control when the mouse cursor hovers over it.
ms.assetid: 77ca8512-6150-4a75-8220-19de3fe9e719
keywords:
- TEXT.hoverFontStyle Windows Media Player
topic_type:
- apiref
api_name:
- TEXT.hoverFontStyle
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# TEXT.hoverFontStyle

The **hoverFontStyle** attribute specifies or retrieves the font style used for the Text control when the mouse cursor hovers over it.

``` syntax
        elementID.hoverFontStyle
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

If **hoverFontStyle** is not specified, **fontStyle** is used.

See the [value](text-value.md) attribute for a sample illustrating how the attributes of the **TEXT** element are used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**TEXT Element**](text-element.md)
</dt> <dt>

[**TEXT.fontStyle**](text-fontstyle.md)
</dt> </dl>

 

 





