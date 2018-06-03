---
title: UseClientAccessNetworksForSharedVolumes
description: Enables or disables the use of client access networks for cluster shared volumes (CSV) used by the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9A5FE399-6182-473D-A191-149703A3DF12
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- UseClientAccessNetworksForSharedVolumes Failover Cluster
topic_type:
- apiref
api_name:
- UseClientAccessNetworksForSharedVolumes
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# UseClientAccessNetworksForSharedVolumes

Enables or disables the use of client access networks for cluster shared volumes (CSV) used by the cluster.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 0                                         |
| Maximum   | 2                                         |
| Default   | 0                                         |



 

## Remarks

The constant for this property is **USE\_CLIENT\_ACCESS\_NETWORKS\_FOR\_CSV**.

**Windows Server 2012 R2 and Windows Server 2012:** The Maximum value is 1.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





