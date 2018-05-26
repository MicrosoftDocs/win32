---
title: S2DCacheDesiredState
description: Specifies the desired cache state for Storage Spaces Direct (2SD).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: C7A274CD-5878-4074-A311-6B721E1402ED
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- S2DCacheDesiredState Failover Cluster
topic_type:
- apiref
api_name:
- S2DCacheDesiredState
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# S2DCacheDesiredState

Specifies the desired cache state for Storage Spaces Direct (2SD).



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)<br/> |
| Minimum<br/>   | 0x00000000 (disabled)<br/>                     |
| Maximum<br/>   | 0x00000002 (read/write)<br/>                   |
| Default<br/>   | 0x00000002 (read/write)<br/>                   |



 

The possible values for the **S2DCacheDesiredState** property are:



| Value      | Description                                  |
|------------|----------------------------------------------|
| 0x00000000 | disabled                                     |
| 0x00000001 | read-only                                    |
| 0x00000002 | read/write                                   |
| 0x0000000A | provisioning                                 |
| 0x0000000F | provisioning - NVM Express (NVMe) flash tier |
| 0x00000014 | provisioning - spinning media                |
| 0x00000078 | disabling                                    |
| 0x000000C8 | dormant                                      |
| 0x000003E9 | ineligible - no disks                        |
| 0x000003EA | ineligible - no NVMe flash tier              |
| 0x000003EB | ineligible - not mixed                       |



 

## Remarks

The constant for this property is **CLUSTER\_S2D\_CACHE\_DESIRED\_STATE**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> <dt>

[CLUSCTL\_CLUSTER\_SET\_CLUSTER\_S2D\_ENABLED](clusctl-cluster-set-cluster-das-mode-enabled.md)
</dt> </dl>

 

 





