---
title: UseNetftForSharedVolumes
description: Specifies whether to enable Network Fault-Tolerance (NETFT) for cluster shared volumes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 246A5BE4-55BE-44D9-9199-8C6ED142F344
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- UseNetftForSharedVolumes Failover Cluster
topic_type:
- apiref
api_name:
- UseNetftForSharedVolumes
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# UseNetftForSharedVolumes

Specifies whether to enable Network Fault-Tolerance (NETFT) for cluster shared volumes.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 0                                         |
| Maximum   | 1                                         |
| Default   | 1                                         |



 

"1" to enable NETFT, "0" to disable it.

## Remarks

The constant for this property is **USE\_NETFT\_FOR\_SHARED\_VOLUMES**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





