---
title: BUTTONELEMENT.down
description: The down attribute specifies or retrieves a value indicating whether the button element is in the up or down position.
ms.assetid: 6b3633c5-84c1-48a0-bd2f-94660890d9a6
keywords:
- BUTTONELEMENT.down Windows Media Player
topic_type:
- apiref
api_name:
- BUTTONELEMENT.down
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# BUTTONELEMENT.down

The **down** attribute specifies or retrieves a value indicating whether the button element is in the up or down position.

``` syntax
        elementID.down
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                                                     |
|-------|-----------------------------------------------------------------|
| true  | Indicates the **BUTTONELEMENT** is in the down position.        |
| false | Default. Indicates the **BUTTONELEMENT** is in the up position. |



 

## Remarks

For a button element to remain in the down position, **sticky** must be set to true. By default, **sticky** is false, and any attempt to set **down** to true will be ignored.

If an invalid value is specified, the previous state is maintained.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**BUTTONELEMENT Element**](buttonelement-element.md)
</dt> <dt>

[**BUTTONELEMENT.downToolTip**](buttonelement-downtooltip.md)
</dt> </dl>

 

 





