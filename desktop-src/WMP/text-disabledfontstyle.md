---
title: TEXT.disabledFontStyle
description: The disabledFontStyle attribute specifies or retrieves the font style used for the Text control when it is disabled.
ms.assetid: d0593fe0-f80d-44a3-b989-e85887465d8a
keywords:
- TEXT.disabledFontStyle Windows Media Player
topic_type:
- apiref
api_name:
- TEXT.disabledFontStyle
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# TEXT.disabledFontStyle

The **disabledFontStyle** attribute specifies or retrieves the font style used for the Text control when it is disabled.

``` syntax
        elementID.disabledFontStyle
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

If **disabledFontStyle** is not specified, **fontStyle** is used.

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

 

 





