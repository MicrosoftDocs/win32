---
description: If the CDROMVolume Control bit is set, the control shows all the volumes in the current installation plus all the CD-ROM volumes.
ms.assetid: 233df659-413d-416e-a3d7-d05a67e9bd73
title: CDROMVolume Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# CDROMVolume Control Attribute

If the CDROMVolume Control bit is set, the control shows all the volumes in the current installation plus all the CD-ROM volumes.

If this bit is not set, the control shows all the volumes in the current installation.

## Valid Controls

[DirectoryCombo](directorycombo-control.md)

 

[VolumeCostList](volumecostlist-control.md)

 

[VolumeSelectCombo](volumeselectcombo-control.md)

## Value



| Decimal | Hexadecimal | Constant                              |
|---------|-------------|---------------------------------------|
| 524288  | 0x00080000  | **msidbControlAttributesCDROMVolume** |



 

## Remarks

To set this attribute on a control, include the CDROMVolume bit in the Attributes column of the control's record in the [Control table](control-table.md).

See [Control Attributes](control-attributes.md) and the control you need to create under [Controls](controls.md).

 

 



