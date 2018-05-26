---
title: NodeDrainStatus
description: Specifies the status of a node drain.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: B68E19D2-2B81-496A-B090-06B6B3495268
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- NodeDrainStatus Failover Cluster
topic_type:
- apiref
api_name:
- NodeDrainStatus
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# NodeDrainStatus

Specifies the status of a node drain.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | **NodeDrainStatusNotInitiated** (0)       |
| Maximum   | **NodeDrainStatusFailed** (3)             |
| Default   | **NodeDrainStatusNotInitiated**           |



 

## Remarks

This property can contain one of the following values from the [**CLUSTER\_NODE\_DRAIN\_STATUS**](/windows/previous-versions/ClusApi/ne-clusapi-cluster_node_drain_status?branch=master) enumeration:



| Name                            | Value | Description                            |
|---------------------------------|-------|----------------------------------------|
| **NodeDrainStatusNotInitiated** | 0     | The node drain has not been initiated. |
| **NodeDrainStatusInProgress**   | 1     | The node drain is in progress.         |
| **NodeDrainStatusCompleted**    | 2     | The node drain has completed.          |
| **NodeDrainStatusFailed**       | 3     | The node drain has failed.             |



 

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Node Common Properties](node-common-properties.md)
</dt> <dt>

[**CLUSTER\_NODE\_DRAIN\_STATUS**](/windows/previous-versions/ClusApi/ne-clusapi-cluster_node_drain_status?branch=master)
</dt> </dl>

 

 





