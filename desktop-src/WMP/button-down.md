---
title: BUTTON.down
description: The down attribute specifies or retrieves a value indicating whether the BUTTON is in the up or down position.
ms.assetid: 75398e8c-b13e-4836-b487-ed880da753ea
keywords:
- BUTTON.down Windows Media Player
topic_type:
- apiref
api_name:
- BUTTON.down
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# BUTTON.down

The **down** attribute specifies or retrieves a value indicating whether the **BUTTON** is in the up or down position.

``` syntax
        elementID.down
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                                                   |
|-------|---------------------------------------------------------------|
| true  | Indicates that the **BUTTON** is in the down position.        |
| false | Default. Indicates that the **BUTTON** is in the up position. |



 

## Remarks

For a **BUTTON** to remain in the down position, **sticky** must be set to true. By default, **sticky** is false, and any attempt to set **down** to true will be ignored.

If an invalid value is specified, the previous state is maintained.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**BUTTON Element**](button-element.md)
</dt> <dt>

[**BUTTON.downImage**](button-downimage.md)
</dt> <dt>

[**BUTTON.downToolTip**](button-downtooltip.md)
</dt> </dl>

 

 





