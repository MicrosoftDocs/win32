---
description: If the FixedVolume Control bit is set, the control shows all the volumes involved in the current installation plus all the fixed internal hard drives.
ms.assetid: e0917a8c-f43a-412d-9b91-9d5f80779f41
title: FixedVolume Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# FixedVolume Control Attribute

If the FixedVolume Control bit is set, the control shows all the volumes involved in the current installation plus all the fixed internal hard drives.

If this bit is not set, the control lists the volumes in the current installation.

## Valid Controls

[DirectoryCombo](directorycombo-control.md)

 

[VolumeCostList](volumecostlist-control.md)

 

[VolumeSelectCombo](volumeselectcombo-control.md)



| Decimal | Hexadecimal | Constant                              |
|---------|-------------|---------------------------------------|
| 131072  | 0x00020000  | **msidbControlAttributesFixedVolume** |



 

## Remarks

To set this attribute on a control, include the FixedVolume bit in the Attributes column of the control's record in the [Control table](control-table.md).

See [Control Attributes](control-attributes.md) and the control you need to create under [Controls](controls.md).

 

 



