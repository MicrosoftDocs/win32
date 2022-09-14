---
title: EFFECTS.windowed
description: The windowed attribute specifies or retrieves a value indicating whether the visualization will be windowed or windowless, that is, whether the entire rectangle of the control will be visible at all times, or whether it can be clipped.
ms.assetid: bc535274-8bc3-43bb-aab0-11899134d71e
keywords:
- EFFECTS.windowed Windows Media Player
topic_type:
- apiref
api_name:
- EFFECTS.windowed
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# EFFECTS.windowed

The **windowed** attribute specifies or retrieves a value indicating whether the visualization will be windowed or windowless, that is, whether the entire rectangle of the control will be visible at all times, or whether it can be clipped. This attribute can only be set at design time.

``` syntax
        elementID.windowed
```

## Possible Values

This attribute is a **Boolean** specified at design time and read-only thereafter.



| Value | Description                              |
|-------|------------------------------------------|
| true  | The control will be windowed.            |
| false | Default. The control will be windowless. |



 

## Remarks

If a non-rectangular visualization window is desired, or if any part of the window is covered by an image, this attribute must be set to false. This sacrifices some performance to do the necessary clipping.

If **windowed** is set to true, any image covering the visualization window is ignored, and the visualization window has the highest-level z-order.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**EFFECTS Element**](effects-element.md)
</dt> </dl>

 

 





