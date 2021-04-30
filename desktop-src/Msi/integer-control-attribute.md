---
description: If this bit is set on a control, the associated property specified in the Property column of the Control table is an integer. If this bit is not set, the property is a string value.
ms.assetid: 58db9451-d152-439b-b7cf-39ddea84bcc9
title: Integer Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# Integer Control Attribute

If this bit is set on a control, the associated property specified in the Property column of the [Control table](control-table.md) is an integer. If this bit is not set, the property is a string value.

## Valid Controls

[CheckBox](checkbox-control.md)

[ComboBox](combobox-control.md)

[Edit](edit-control.md)

[ListBox](listbox-control.md)

[RadioButtonGroup](radiobuttongroup-control.md)

## Value



| Decimal | Hexadecimal | Constant                          |
|---------|-------------|-----------------------------------|
| 16      | 0x00000010  | **msidbControlAttributesInteger** |



 

## Remarks

To set this attribute on a control, include the Integer bit in the Attributes column of the control's record in the [Control table](control-table.md).

See [Control Attributes](control-attributes.md) and [Controls](controls.md).

 

 



