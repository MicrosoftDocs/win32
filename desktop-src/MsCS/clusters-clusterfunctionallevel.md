---
title: ClusterFunctionalLevel
description: The major version of the OS on a cluster during a rolling upgrade.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 55E9FF3F-B4B7-4A94-A515-D608A37DF84E
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusterFunctionalLevel Failover Cluster
topic_type:
- apiref
api_name:
- ClusterFunctionalLevel
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusterFunctionalLevel

The major version of the OS on a cluster during a rolling upgrade.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | DWORD<br/>                                     |
| Access<br/>    | [Read-only](read-only-properties.md)<br/>     |
| Structure<br/> | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)<br/> |
| Minimum<br/>   | 0<br/>                                         |
| Maximum<br/>   | 0xFFFFFFFF<br/>                                |
| Default<br/>   | 0<br/>                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_FUNCTIONAL\_LEVEL**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> <dt>

[**ClusterUpgradeFunctionalLevel**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_upgrade?branch=master)
</dt> </dl>

 

 





