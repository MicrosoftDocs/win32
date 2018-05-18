---
title: S2DCacheBehavior
description: Specifies the cache behavior for Storage Spaces Direct (2SD).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '808A156F-F54C-45C4-AE69-FA8AD4E7DE5B'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["S2DCacheBehavior Failover Cluster"]
topic_type:
- apiref
api_name:
- S2DCacheBehavior
api_type:
- NA
---

# S2DCacheBehavior

Specifies the cache behavior for Storage Spaces Direct (2SD).

> [!Note]  
> Instead of setting this property, we recommend that you use the [**S2DCacheDesiredState**](dasmodecachedesiredstate.md) property.

 



| Attribute            | Value                                                                   |
|----------------------|-------------------------------------------------------------------------|
| Data type<br/> | Unsigned large integer<br/>                                       |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>                      |
| Structure<br/> | [**CLUSPROP\_ULARGE\_INTEGER**](clusprop-ularge-integer.md)<br/> |
| Minimum<br/>   | 0<br/>                                                            |
| Maximum<br/>   | 4 (disable and remove flash partitions)<br/>                      |
| Default<br/>   | 0<br/>                                                            |



 

The possible values for the **S2DCacheBehavior** property are:



| Value | Description                          |
|-------|--------------------------------------|
| 0     | default                              |
| 1     | dormant                              |
| 2     | remove spindle partitions on disable |
| 4     | disable and remove flash partitions  |



 

## Remarks

The constant for this property is **CLUSTER\_S2D\_CACHE\_BEHAVIOR\_FLAGS**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> <dt>

[CLUSCTL\_CLUSTER\_SET\_CLUSTER\_S2D\_ENABLED](clusctl-cluster-set-cluster-das-mode-enabled.md)
</dt> </dl>

 

 





