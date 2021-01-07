---
description: If the FloppyVolume Control bit is set, the control shows all the volumes involved in the current installation plus all the floppy volumes.
ms.assetid: 65e17920-bb2c-4b98-a2dd-ebaee752ed0a
title: FloppyVolume Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# FloppyVolume Control Attribute

If the FloppyVolume Control bit is set, the control shows all the volumes involved in the current installation plus all the floppy volumes.

If this bit is not set, the control lists volumes in the current installation.

## Valid Controls

[DirectoryCombo](directorycombo-control.md)

[VolumeCostList](volumecostlist-control.md)

[VolumeSelectCombo](volumeselectcombo-control.md)

## Value



| Decimal | Hexadecimal | Constant                               |
|---------|-------------|----------------------------------------|
| 2097152 | 0x00200000  | **msidbControlAttributesFloppyVolume** |



 

## Remarks

To set this attribute on a control, include the FloppyVolume bit in the Attributes column of the control's record in the [Control table](control-table.md).

See [Control Attributes](control-attributes.md) and the control you need to create under [Controls](controls.md).

 

 



