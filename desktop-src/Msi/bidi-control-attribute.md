---
description: This is a combination of the right-to-left reading order RTLRO, the RightAligned, and LeftScroll attributes.
ms.assetid: 4eaec16f-ee1c-437b-8b76-7ebbdc4e2f71
title: BiDi Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# BiDi Control Attribute

This is a combination of the right-to-left reading order [RTLRO](rtlro-control-attribute.md), the [RightAligned](rightaligned-control-attribute.md), and [LeftScroll](leftscroll-control-attribute.md) attributes.

## Valid Controls

[ScrollableText](scrollabletext-control.md)

 

[VolumeCostList](volumecostlist-control.md)

 

[ComboBox](combobox-control.md)

 

[DirectoryList](directorylist-control.md)

 

[DirectoryCombo](directorycombo-control.md)

 

[Edit](edit-control.md)

 

[ListBox](listbox-control.md)

 

[ListView](listview-control.md)

 

[SelectionTree](selectiontree-control.md)

 

[VolumeSelectCombo](volumeselectcombo-control.md)

## Value



| Decimal | Hexadecimal | Constant                       |
|---------|-------------|--------------------------------|
| 224     | 0x000000E0  | **msidbControlAttributesBiDi** |



 

## Remarks

To set this attribute on a control, include the BiDi bit in the Attributes column of the control's record in the [Control table](control-table.md).

See [Control Attributes](control-attributes.md) and the control you need to create under [Controls](controls.md).

 

 



