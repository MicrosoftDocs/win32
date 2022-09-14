---
description: If this bit is set, the scroll bar is located on the left side of the control.
ms.assetid: bf59ec6b-ac24-4a0b-9326-aea181b7539b
title: LeftScroll Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# LeftScroll Control Attribute

If this bit is set, the scroll bar is located on the left side of the control.

If this bit is not set, the scroll bar is on the right side of the control.

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



| Decimal | Hexadecimal | Constant                             |
|---------|-------------|--------------------------------------|
| 128     | 0x00000080  | **msidbControlAttributesLeftScroll** |



 

## Remarks

To set this attribute on a control, include the LeftScroll bit in the Attributes column of the control's record in the [Control table](control-table.md).

See [Control Attributes](control-attributes.md) and [Controls](controls.md).

 

 



