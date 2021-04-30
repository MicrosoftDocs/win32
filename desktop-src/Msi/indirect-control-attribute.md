---
description: The Indirect control attribute specifies whether the value displayed or changed by this control is referenced indirectly.
ms.assetid: dc9c0dd6-7e19-44ec-b1a5-3d51a1855adf
title: Indirect Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# Indirect Control Attribute

The Indirect control attribute specifies whether the value displayed or changed by this control is referenced indirectly. If this bit is set, the control displays or changes the value of the property that has the identifier listed in the Property column of the [Control table](control-table.md). If this bit is not set, the control displays or changes the value of the property in the Property column of the Control table.

## Valid Controls

All active controls.

## Value



| Decimal | Hexadecimal | Constant                           |
|---------|-------------|------------------------------------|
| 8       | 0x00000008  | **msidbControlAttributesIndirect** |



 

## Remarks

See [Control Attributes](control-attributes.md) and the control you need to create under [Controls](controls.md).

 

 



