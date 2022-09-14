---
title: BUTTON.sticky
description: The sticky attribute specifies or retrieves a value indicating whether the BUTTON is a toggle, that is, whether it is a two-state or single-state BUTTON.
ms.assetid: aa0b48b4-29ce-440c-aeb9-dce31ab3cb63
keywords:
- BUTTON.sticky Windows Media Player
topic_type:
- apiref
api_name:
- BUTTON.sticky
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# BUTTON.sticky

The **sticky** attribute specifies or retrieves a value indicating whether the **BUTTON** is a toggle, that is, whether it is a two-state or single-state **BUTTON**.

``` syntax
        elementID.sticky
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                        |
|-------|------------------------------------|
| true  | **BUTTON** is sticky.              |
| false | Default. **BUTTON** is not sticky. |



 

## Remarks

If **sticky** is set to true, the **BUTTON** will change to the down state when clicked and will remain in that state until clicked again. When the **BUTTON** is in the down state, the **down** attribute will be true and the **downImage** will be displayed.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**BUTTON Element**](button-element.md)
</dt> <dt>

[**BUTTON.down**](button-down.md)
</dt> <dt>

[**BUTTON.downImage**](button-downimage.md)
</dt> </dl>

 

 





