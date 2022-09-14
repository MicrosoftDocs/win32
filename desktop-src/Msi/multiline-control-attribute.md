---
description: If this bit is set on an Edit control, the installer creates a multiple line edit control with a vertical scroll bar.
ms.assetid: cbdbe088-9cf1-4af8-a5f7-072faee7f34e
title: MultiLine Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# MultiLine Control Attribute

If this bit is set on an [Edit control](edit-control.md), the installer creates a multiple line edit control with a vertical scroll bar.

If this bit is not set, it specifies displaying a normal edit control.

## Valid Controls

[Edit control](edit-control.md).



| Decimal | Hexadecimal | Constant                            |
|---------|-------------|-------------------------------------|
| 65536   | 0x00010000  | **msidbControlAttributesMultiline** |



 

## Remarks

To set this attribute on a control, include the MultiLine bit in the Attributes column of the control's record in the [Control table](control-table.md).

See [Control Attributes](control-attributes.md) and [Controls](controls.md).

 

 



