---
title: BUTTONELEMENT.sticky
description: The sticky attribute specifies or retrieves a value indicating whether the BUTTONELEMENT is a toggle, that is, whether it is a two-state or single-state button.
ms.assetid: a7e74f70-9fa6-45a1-ab65-2db107e13551
keywords:
- BUTTONELEMENT.sticky Windows Media Player
topic_type:
- apiref
api_name:
- BUTTONELEMENT.sticky
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# BUTTONELEMENT.sticky

The **sticky** attribute specifies or retrieves a value indicating whether the **BUTTONELEMENT** is a toggle, that is, whether it is a two-state or single-state button.

``` syntax
        elementID.sticky
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                               |
|-------|-------------------------------------------|
| true  | **BUTTONELEMENT** is sticky.              |
| false | Default. **BUTTONELEMENT** is not sticky. |



 

## Remarks

If the **sticky** attribute is set to true, the button element will change to the down state when clicked and will remain in that state until clicked again. When the button element is in the down state, the **down** attribute will be true and the appropriate portion of the button group **downImage** will be displayed.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**BUTTONELEMENT Element**](buttonelement-element.md)
</dt> <dt>

[**BUTTONELEMENT.down**](buttonelement-down.md)
</dt> <dt>

[**BUTTONGROUP.downImage**](buttongroup-downimage.md)
</dt> </dl>

 

 





