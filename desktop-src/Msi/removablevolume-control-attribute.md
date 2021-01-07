---
description: If this bit is set, the control shows all the volumes involved in the current installation plus all the removable volumes. If this bit is not set, the control lists volumes in the current installation.
ms.assetid: fc16ca46-54a1-4b24-ba51-8b4d358268f4
title: RemovableVolume Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# RemovableVolume Control Attribute

If this bit is set, the control shows all the volumes involved in the current installation plus all the removable volumes. If this bit is not set, the control lists volumes in the current installation.

## Valid Controls

[DirectoryCombo](directorycombo-control.md)

 

[VolumeCostList](volumecostlist-control.md)

 

[VolumeSelectCombo](volumeselectcombo-control.md)

## Value



| Decimal | Hexadecimal | Constant                                  |
|---------|-------------|-------------------------------------------|
| 65536   | 0x00010000  | **msidbControlAttributesRemovableVolume** |



 

## Remarks

To set this attribute on a control, include the RemovableVolume bit in the Attributes column of the control's record in the [Control table](control-table.md).

See [Control Attributes](control-attributes.md) and [Controls](controls.md).

 

 



