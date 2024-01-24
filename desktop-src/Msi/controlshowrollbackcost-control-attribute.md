---
description: This attribute specifies whether or not the rollback backup files are included in the costs displayed by the VolumeCostList control.
ms.assetid: a3ed4d8a-170b-4708-afc2-03d2a5b665a3
title: ControlShowRollbackCost Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# ControlShowRollbackCost Control Attribute

This attribute specifies whether or not the rollback backup files are included in the costs displayed by the [VolumeCostList control](volumecostlist-control.md).

If this bit is set and [**PROMPTROLLBACKCOST**](promptrollbackcost.md) property = P, the rollback backup files are included in the cost displayed by the [VolumeCostList Control](volumecostlist-control.md).

If this bit is not set and [**PROMPTROLLBACKCOST**](promptrollbackcost.md) property = P, the rollback backup files are not included in the cost displayed by the [VolumeCostList Control](volumecostlist-control.md).

## Valid Controls

[VolumeCostList](volumecostlist-control.md)

## Value



| Decimal | Hexadecimal | Constant                         |
|---------|-------------|----------------------------------|
| 4194304 | 0x00400000  | **msidbControlShowRollbackCost** |



 

## Remarks

This control attribute is ignored if [**PROMPTROLLBACKCOST**](promptrollbackcost.md) = D or F.

If [**PROMPTROLLBACKCOST**](promptrollbackcost.md) = F, the cost of the rollback, backup files is included.

If [**PROMPTROLLBACKCOST**](promptrollbackcost.md) = D, or [**DISABLEROLLBACK**](-disablerollback.md) property = 1, the cost of the rollback, backup files is not included.

 

 



