---
description: If the Bitmap Control bit is set, the text in the control is replaced by a bitmap image. The Text column in the Control table is a foreign key into the Binary table.
ms.assetid: ec774f31-7712-4a70-8c69-1cc731009049
title: Bitmap Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# Bitmap Control Attribute

If the Bitmap Control bit is set, the text in the control is replaced by a bitmap image. The Text column in the [Control table](control-table.md) is a foreign key into the [Binary table](binary-table.md).

If this bit is not set, the text in the control is specified in the Text column of the [Control table](control-table.md).

## Valid Controls

[CheckBox](checkbox-control.md)

 

[PushButton](pushbutton-control.md)

 

[RadioButtonGroup](radiobuttongroup-control.md)

## Value



| Decimal | Hexadecimal | Constant                         |
|---------|-------------|----------------------------------|
| 262144  | 0x00040000  | **msidbControlAttributesBitmap** |



 

## Remarks

To set this attribute on a control, include the Bitmap bit in the Attributes column of the control's record in the [Control table](control-table.md).

The Text column in the Control table is used as a foreign key to the [Binary table](binary-table.md), therefore the control cannot contain both an icon image and text.

Do not set both the [Icon](icon-control-attribute.md) and Bitmap bits.

See [Control Attributes](control-attributes.md) and the control you need to create under [Controls](controls.md).

 

 



