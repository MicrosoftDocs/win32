---
title: UpdateFunctionalLevel method of the MSCluster\_ClusterService class
description: Updates the clusters functional level.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f3b12d0a-e397-4374-b164-7c32983a2f9d
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- UpdateFunctionalLevel method
- UpdateFunctionalLevel method, MSCluster_ClusterService class
- MSCluster_ClusterService class, UpdateFunctionalLevel method
topic_type:
- apiref
api_name:
- MSCluster_ClusterService.UpdateFunctionalLevel
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# UpdateFunctionalLevel method of the MSCluster\_ClusterService class

Updates the cluster's functional level

## Syntax


```mof
uint32 UpdateFunctionalLevel(
  [in] boolean WhatIf
);
```



## Parameters

<dl> <dt>

*WhatIf* \[in\]
</dt> <dd>

If true, only check whether updating would succeed without actually performing update. If omitted, update is performed.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\MSCluster<br/>                                                                |
| MOF<br/>                      | <dl> <dt>ClusWmiExt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl>    |



## See also

<dl> <dt>

[**MSCluster\_ClusterService**](mscluster-clusterservice.md)
</dt> </dl>

 

 





