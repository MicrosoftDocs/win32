---
description: If this bit is set, text is replaced by an icon image and the Text column in the Control table is a foreign key into the Binary table.
ms.assetid: 5eefdfcb-89a5-4885-bab0-6409ef3ce349
title: Icon Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# Icon Control Attribute

If this bit is set, text is replaced by an icon image and the Text column in the [Control table](control-table.md) is a foreign key into the [Binary table](binary-table.md).

If this bit is not set, text in the control is specified in the Text column of the [Control table](control-table.md).

## Valid Controls

[CheckBox](checkbox-control.md)

[PushButton](pushbutton-control.md)

[RadioButtonGroup](radiobuttongroup-control.md)

## Value



| Decimal | Hexadecimal | Constant                       |
|---------|-------------|--------------------------------|
| 5242288 | 0x00080000  | **msidbControlAttributesIcon** |



 

## Remarks

To set this attribute on a control, include the Icon bits in the Attributes column of the control's record in the [Control table](control-table.md).

The Text column in the Control table is used as a foreign key to the [Binary table](binary-table.md), therefore the control cannot contain both an icon image and text.

Do not set both the Icon and [Bitmap](bitmap-control-attribute.md) bits.

See [Control Attributes](control-attributes.md) and the control you need to create under [Controls](controls.md).

 

 



