---
description: If the ComboList Control bit is set on a combo box, the edit field is replaced by a static text field. This prevents a user from entering a new value and requires the user to choose only one of the predefined values.
ms.assetid: 79af4bb0-1e0f-4df3-ae25-d2798842adb6
title: ComboList Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# ComboList Control Attribute

If the ComboList Control bit is set on a combo box, the edit field is replaced by a static text field. This prevents a user from entering a new value and requires the user to choose only one of the predefined values.

If this bit is not set, the combo box has an edit field.

## Valid Controls

[ComboBox](combobox-control.md)

## Value



| Decimal | Hexadecimal | Description                     |
|---------|-------------|---------------------------------|
| 131072  | 0x00020000  | msidbControlAttributesComboList |



 

## Remarks

To set this attribute on a control, include the ComboList bit in the Attributes column of the control's record in the [Control table](control-table.md).

See [Control Attributes](control-attributes.md) and the control you need to create under [Controls](controls.md).

 

 



