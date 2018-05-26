---
title: ArbitrationDelay
description: The number of seconds to delay a node from locking a file share witness during a vote for the next file share witness. This property is used by a cluster node that does not currently own the quorum resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: C7FDAAA4-B373-4FB5-B1C6-6A8A5D8C88FF
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ArbitrationDelay Failover Cluster
topic_type:
- apiref
api_name:
- ArbitrationDelay
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ArbitrationDelay

The number of seconds to delay a node from locking a file share witness during a vote for the next file share witness. This property is used by a cluster node that does not currently own the quorum resource.



| Attribute | Value                                   |
|-----------|-----------------------------------------|
| Data type | **DWORD**                               |
| Access    | [Read/write](read-write-properties.md) |
| Status    | Required                                |
| Structure | **CLUSPROP\_DWORD**                     |
| Minimum   | 0                                       |
| Maximum   | 60                                      |
| Default   | 6                                       |



 

## Remarks

If cluster nodes lose communication with each other and a file share witness is needed to maintain a quorum, the node that owns the quorum resource gets the first chance to lock the file share witness. This property specifies the delay before another node can lock the file share witness.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[File Share Quorum Witness Resource Private Properties](file-share-quorum-witness-resource-private-properties.md)
</dt> </dl>

 

 





