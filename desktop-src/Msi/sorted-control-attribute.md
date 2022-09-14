---
description: If this bit is set, the items listed in the control are displayed in a specified order. If the bit is not set, items are displayed in alphabetical order.
ms.assetid: c55bf6bf-6625-47cb-867a-14b3ef8aea0a
title: Sorted Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# Sorted Control Attribute

If this bit is set, the items listed in the control are displayed in a specified order. If the bit is not set, items are displayed in alphabetical order.

## Valid Controls

[ComboBox](combobox-control.md)

 

[ListBox](listbox-control.md)

 

[ListView Control](listview-control.md)

## Value



| Decimal | Hexadecimal | Constant                         |
|---------|-------------|----------------------------------|
| 65536   | 0x00010000  | **msidbControlAttributesSorted** |



 

## Remarks

To sort the items in a [ComboBox](combobox-control.md), include the Sorted bit in the Attributes column of the [Control table](control-table.md) and specify the item order in the Order column of the [ComboBox table](combobox-table.md).

To sort the items in a [ListBox](listbox-control.md), include the Sorted bit in the Attributes column of the [Control table](control-table.md) and specify the item order in the Order column of the [ComboBox table](combobox-table.md).

To sort the items in a [ListView](listview-control.md), include the Sorted bit in the Attributes column of the [Control table](control-table.md) and specify the order of items in the [ComboBox table](combobox-table.md).

See [Control Attributes](control-attributes.md) and [Controls](controls.md).

 

 



