---
title: IgnorePersistentStateOnStartup
description: Specifies whether the cluster will bring online groups that were online when the cluster was shut down.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3355aa3a-cb40-4f70-bf47-171637175776
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- IgnorePersistentStateOnStartup Failover Cluster ,for clusters
- IgnorePersistentStateOnStartup Failover Cluster ,for failover clusters
- IgnorePersistentStateOnStartup Failover Cluster
topic_type:
- apiref
api_name:
- IgnorePersistentStateOnStartup
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IgnorePersistentStateOnStartup

Specifies whether the cluster will bring online groups that were online when the cluster was shut down. The following table summarizes the attributes of the **IgnorePersistentStateOnStartup** property.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)<br/> |
| Minimum<br/>   | 0<br/>                                         |
| Maximum<br/>   | 1<br/>                                         |
| Default<br/>   | 0<br/>                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_IGNORE\_PERSISTENT\_STATE**.

**Windows Server 2012 R2, Windows Server 2012 and Windows Server 2008 R2:** This property is read-only. It can only be set by stopping the cluster and restarting it with the "/IgnorePersistentState" or "/ips" switch passed to the cluster service (for example `Net Start ClusSvc /ips`.)

This property is also exposed as the **IgnorePersistentStateOnStartup** property of the [**MSCluster\_Cluster**](https://msdn.microsoft.com/library/aa371422) WMI class.

## Requirements



|                                     |                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2008 R2 Enterprise, Windows Server 2008 R2 Datacenter<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**MSCluster\_Cluster**](https://msdn.microsoft.com/library/aa371422)
</dt> </dl>

 

 





