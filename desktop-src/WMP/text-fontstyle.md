---
title: TEXT.fontStyle
description: The fontStyle attribute specifies or retrieves the font style for the Text control.
ms.assetid: 1bb99305-dccc-489d-9a02-7cb306f0d47d
keywords:
- TEXT.fontStyle Windows Media Player
topic_type:
- apiref
api_name:
- TEXT.fontStyle
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# TEXT.fontStyle

The **fontStyle** attribute specifies or retrieves the font style for the Text control.

``` syntax
        elementID.fontStyle
```

## Possible Values

This attribute is a read/write **String** containing one or more of the following values.



| Value     | Description                 |
|-----------|-----------------------------|
| Bold      | Bold font style.            |
| Italic    | Italic font style.          |
| Underline | Underline font style.       |
| Strikeout | Strikeout font style.       |
| Normal    | Default. Normal font style. |



 

## Remarks

Any combination of the values can be used, separated with spaces. The Normal style has priority over all other values, and any others specified along with Normal will be ignored.

See the [value](text-value.md) attribute for a sample illustrating how the attributes of the **TEXT** element are used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**TEXT Element**](text-element.md)
</dt> </dl>

 

 





