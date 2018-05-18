---
title: S2DCacheMetadataReserveBytes
description: The amount of disk space, in bytes, to reserve for the cache of a flash drive when using Storage Spaces Direct (2SD).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5E97D4CC-5F8C-45AA-827D-E84D79B54B36'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["S2DCacheMetadataReserveBytes Failover Cluster"]
topic_type:
- apiref
api_name:
- S2DCacheMetadataReserveBytes
api_type:
- NA
---

# S2DCacheMetadataReserveBytes

The amount of disk space, in bytes, to reserve for the cache of a flash drive when using Storage Spaces Direct (2SD).



| Attribute            | Value                                                                   |
|----------------------|-------------------------------------------------------------------------|
| Data type<br/> | Unsigned large integer<br/>                                       |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>                      |
| Structure<br/> | [**CLUSPROP\_ULARGE\_INTEGER**](clusprop-ularge-integer.md)<br/> |
| Minimum<br/>   | 0<br/>                                                            |
| Maximum<br/>   | 4398046511104<br/>                                                |
| Default<br/>   | 34359738368<br/>                                                  |



 

## Remarks

The constant for this property is **CLUSTER\_S2D\_CACHE\_METADATA\_RESERVE**.

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

 

 





