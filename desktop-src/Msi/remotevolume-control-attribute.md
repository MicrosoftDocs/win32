---
description: If this bit is set, the control shows all the volumes involved in the current installation plus all the remote volumes. If this bit is not set, the control lists volumes in the current installation.
ms.assetid: be70cd86-6aaf-4307-a553-715d6185accd
title: RemoteVolume Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# RemoteVolume Control Attribute

If this bit is set, the control shows all the volumes involved in the current installation plus all the remote volumes. If this bit is not set, the control lists volumes in the current installation.

## Valid Controls

[DirectoryCombo](directorycombo-control.md)

[VolumeCostList](volumecostlist-control.md)

[VolumeSelectCombo](volumeselectcombo-control.md)

## Value



| Decimal | Hexadecimal | Constant                               |
|---------|-------------|----------------------------------------|
| 262144  | 0x00040000  | **msidbControlAttributesRemoteVolume** |



 

## Remarks

To set this attribute on a control, include the RemoteVolume bit in the Attributes column of the control's record in the [Control table](control-table.md).

See [Control Attributes](control-attributes.md) and [Controls](controls.md).

 

 



