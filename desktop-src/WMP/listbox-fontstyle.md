---
title: LISTBOX.fontStyle
description: The fontStyle attribute specifies or retrieves the font style for the list box control.
ms.assetid: c42b80b6-0dea-4080-a06e-931fdc02fa55
keywords:
- LISTBOX.fontStyle Windows Media Player
topic_type:
- apiref
api_name:
- LISTBOX.fontStyle
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# LISTBOX.fontStyle

The **fontStyle** attribute specifies or retrieves the font style for the list box control.

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

[**LISTBOX Element**](listbox-element.md)
</dt> <dt>

[**LISTBOX.fontSize**](listbox-fontsize.md)
</dt> </dl>

 

 





