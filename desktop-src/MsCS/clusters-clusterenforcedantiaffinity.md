---
title: ClusterEnforcedAntiAffinity
description: Prevents multiple cluster groups from running on the same cluster node when they contain the same AntiAffinityClassNames property value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 29FC4B03-E295-4ADE-A844-1BCBD89C124C
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusterEnforcedAntiAffinity Failover Cluster
topic_type:
- apiref
api_name:
- ClusterEnforcedAntiAffinity
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusterEnforcedAntiAffinity

Prevents multiple cluster groups from running on the same cluster node when they contain the same [**AntiAffinityClassNames**](groups-antiaffinityclassnames.md) property value.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 0                                         |
| Maximum   | 1                                         |
| Default   | 0                                         |



 

## Remarks

This property prevents multiple cluster groups from being hosted on the same cluster node when they have the same [**AntiAffinityClassNames**](groups-antiaffinityclassnames.md) property value. For example, if **ClusterEnforcedAntiAffinity** is set to 1, it will prevent two instances of Exchange Server from running on the same node. However, if **ClusterEnforcedAntiAffinity** is set to the default value (0), the system will try to prevent, but not block the two groups from running on the same node.

The constant for this property is **CLUSTER\_ENFORCED\_ANTIAFFINITY**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> <dt>

[**AntiAffinityClassNames**](groups-antiaffinityclassnames.md)
</dt> </dl>

 

 





