---
description: If this style bit is set the text in the control is displayed in a right-to-left reading order.
ms.assetid: 68394498-98ca-4bcd-86c0-3f692a26a258
title: RTLRO Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# RTLRO Control Attribute

If this style bit is set the text in the control is displayed in a right-to-left reading order.

## Valid Controls

[GroupBox](groupbox-control.md)

 

[ProgressBar](progressbar-control.md)

 

[PushButton](pushbutton-control.md)

 

[ScrollableText](scrollabletext-control.md)

 

[Text](text-control.md)

 

[VolumeCostList](volumecostlist-control.md)

 

[CheckBox](checkbox-control.md)

 

[ComboBox](combobox-control.md)

 

[DirectoryList](directorylist-control.md)

 

[DirectoryCombo](directorycombo-control.md)

 

[Edit](edit-control.md)

 

[PathEdit](pathedit-control.md)

 

[ListBox](listbox-control.md)

 

[ListView](listview-control.md)

 

[RadioButtonGroup](radiobuttongroup-control.md)

 

[SelectionTree](selectiontree-control.md)

 

[VolumeSelectCombo](volumeselectcombo-control.md)

## Value



| Decimal | Hexadecimal | Constant                        |
|---------|-------------|---------------------------------|
| 32      | 0x00000020  | **msidbControlAttributesRTLRO** |



 

## Remarks

To set this attribute on a control, include the RTLRO bit in the Attributes column of the control's record in the [Control table](control-table.md).

See [Control Attributes](control-attributes.md) and [Controls](controls.md).

 

 



