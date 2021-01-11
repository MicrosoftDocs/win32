---
description: If this bit is set on a check box or a radio button group, the button is drawn with the appearance of a push button, but its logic stays the same. If the bit is not set, the controls are drawn in their usual style.
ms.assetid: c30b383a-7fae-413a-a6e6-8e958009f10c
title: PushLike Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# PushLike Control Attribute

If this bit is set on a check box or a radio button group, the button is drawn with the appearance of a push button, but its logic stays the same. If the bit is not set, the controls are drawn in their usual style.

## Valid Controls

[CheckBox](checkbox-control.md)[RadioButtonGroup](radiobuttongroup-control.md)

## Value



| Decimal | Hexadecimal | Constant                           |
|---------|-------------|------------------------------------|
| 131072  | 0x00020000  | **msidbControlAttributesPushLike** |



 

## Remarks

To set this attribute on a control, include the PushLike bit in the Attributes column of the control's record in the [Control table](control-table.md).

See [Control Attributes](control-attributes.md) and [Controls](controls.md).

 

 



