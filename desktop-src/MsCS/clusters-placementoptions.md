---
title: PlacementOptions
description: Options for placing the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '704DD1EB-5763-46B0-9B53-5B37A2AE2299'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["PlacementOptions Failover Cluster"]
topic_type:
- apiref
api_name:
- PlacementOptions
api_type:
- NA
---

# PlacementOptions

Options for placing the cluster.



| Attribute | Value                                               |
|-----------|-----------------------------------------------------|
| Data type | **DWORD**                                           |
| Access    | [Read/write](read-write-properties.md)             |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md)           |
| Minimum   | **PLACEMENT\_OPTIONS\_MIN\_VALUE**                  |
| Maximum   | **PLACEMENT\_OPTIONS\_ALL**                         |
| Default   | **PLACEMENT\_OPTIONS\_DEFAULT\_PLACEMENT\_OPTIONS** |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_PLACEMENT\_OPTIONS**.

This property can contain a bitwise combination of the following [**PLACEMENT\_OPTIONS**](placement-options.md) values.



| Name                                                 | Value                                                                                                  | Description                      |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------|----------------------------------|
| **PLACEMENT\_OPTIONS\_MIN\_VALUE**                   | 0(0x0000000000000000)                                                                                  | Mimimum<br/>               |
| **PLACEMENT\_OPTIONS\_DEFAULT\_PLACEMENT\_OPTIONS**  | **PLACEMENT\_OPTIONS\_MIN\_VALUE**                                                                     | Default<br/>               |
| **PLACEMENT\_OPTIONS\_DISABLE\_CSV\_VM\_DEPENDENCY** | 1(0x0000000000000001)                                                                                  | Disable VM cependency<br/> |
| **PLACEMENT\_OPTIONS\_CONSIDER\_OFFLINE\_VMS**       | 2(0x0000000000000002)                                                                                  | Consider offline VMS<br/>  |
| **PLACEMENT\_OPTIONS\_ALL**                          | **PLACEMENT\_OPTIONS\_DISABLE\_CSV\_VM\_DEPENDENCY** \| **PLACEMENT\_OPTIONS\_CONSIDER\_OFFLINE\_VMS** | All options<br/>           |



 

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





