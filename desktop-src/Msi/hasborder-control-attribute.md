---
description: If this bit is set, the RadioButtonGroup has text and a border displayed around it.
ms.assetid: 25f88e07-a17d-4a5a-bf4f-5615e371cf6b
title: HasBorder Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# HasBorder Control Attribute

If this bit is set, the [RadioButtonGroup](radiobuttongroup-control.md) has text and a border displayed around it.

If the style bit is not set, the border is not displayed and no text is displayed on the group.

## Valid Controls

[RadioButtonGroup](radiobuttongroup-control.md)

## Valid



| Decimal  | Hexadecimal | Constant                            |
|----------|-------------|-------------------------------------|
| 16777216 | 0x01000000  | **msidbControlAttributesHasBorder** |



 

## Remarks

To set this attribute on a control, include the HasBorder bits in the Attributes column of the control's record in the [Control table](control-table.md).

See [Control Attributes](control-attributes.md) and the control you need to create under [Controls](controls.md).

 

 



