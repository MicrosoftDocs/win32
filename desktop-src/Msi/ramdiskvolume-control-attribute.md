---
description: If this bit is set, the control shows all the volumes involved in the current installation plus all the RAM disk volumes. If this bit is not set the control lists volumes in the current installation.
ms.assetid: 52526f39-26fb-4a67-a95f-77f7eb761372
title: RAMDiskVolume Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# RAMDiskVolume Control Attribute

If this bit is set, the control shows all the volumes involved in the current installation plus all the RAM disk volumes. If this bit is not set the control lists volumes in the current installation.

## Valid Controls

[DirectoryCombo](directorycombo-control.md)

 

[VolumeCostList](volumecostlist-control.md)

 

[VolumeSelectCombo](volumeselectcombo-control.md)

## Value



| Decimal | Hexadecimal | Constant                                |
|---------|-------------|-----------------------------------------|
| 1048567 | 0x00100000  | **msidbControlAttributesRAMDiskVolume** |



 

## Remarks

To set this attribute on a control, include the RAMDiskVolume bit in the Attributes column of the control's record in the [Control table](control-table.md).

See [Control Attributes](control-attributes.md) and [Controls](controls.md).

 

 



