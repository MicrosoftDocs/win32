---
description: If this bit is set, the control is displayed with a sunken, three dimensional look.
ms.assetid: 00052b01-f2f0-4749-8826-084e5ebb300a
title: Sunken Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# Sunken Control Attribute

If this bit is set, the control is displayed with a sunken, three dimensional look. The effect of this style bit is different on different controls and versions of Windows. On some controls it has no visible effect. If the system does not support the Sunken control attribute, the control is displayed in the default visual style. If this bit is not set, the control is displayed with the default visual style.

## Valid Controls

All controls.

## Value



| Decimal | Hexadecimal | Constant                         |
|---------|-------------|----------------------------------|
| 4       | 0x00000004  | **msidbControlAttributesSunken** |



 

## Remarks

To set this attribute on a control, include the Sunken bit in the Attributes column of the control's record in the [Control table](control-table.md).

See [Control Attributes](control-attributes.md) and [Controls](controls.md).

 

 



