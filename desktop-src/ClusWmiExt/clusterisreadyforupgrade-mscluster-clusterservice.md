---
title: ClusterIsReadyForUpgrade method of the MSCluster\_ClusterService class
description: Determines whether the clusters functional level can be updated.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f4aa3ef5-e52e-4411-8602-bfb7a229b033
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ClusterIsReadyForUpgrade method
- ClusterIsReadyForUpgrade method, MSCluster_ClusterService class
- MSCluster_ClusterService class, ClusterIsReadyForUpgrade method
topic_type:
- apiref
api_name:
- MSCluster_ClusterService.ClusterIsReadyForUpgrade
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusterIsReadyForUpgrade method of the MSCluster\_ClusterService class

Determines whether the cluster's functional level can be updated

## Syntax


```mof
uint32 ClusterIsReadyForUpgrade(
  [out] boolean isReady
);
```



## Parameters

<dl> <dt>

*isReady* \[out\]
</dt> <dd>

If true, the cluster supports an update of the functional level

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

 

 





