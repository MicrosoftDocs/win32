---
title: RemoveResourceFromClusterSharedVolumes method of the MSCluster\_Cluster class
description: Removes storage from Cluster Shared Volumes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '92c3d133-56d4-4e92-aec5-a8a06853609d'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoveResourceFromClusterSharedVolumes method", "RemoveResourceFromClusterSharedVolumes method, MSCluster_Cluster class", "MSCluster_Cluster class, RemoveResourceFromClusterSharedVolumes method"]
topic_type:
- apiref
api_name:
- MSCluster_Cluster.RemoveResourceFromClusterSharedVolumes
api_location:
- ClusWMI.dll
api_type:
- COM
---

# RemoveResourceFromClusterSharedVolumes method of the MSCluster\_Cluster class

Removes storage from Cluster Shared Volumes.

## Syntax


```mof
void RemoveResourceFromClusterSharedVolumes(
  [in] String Resource
);
```



## Parameters

<dl> <dt>

*Resource* \[in\]
</dt> <dd>

The name of the physical disk resource to remove from Cluster Shared Volumes.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                      |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| Header<br/>                   | <dl> <dt>Clusapi.h</dt> </dl>   |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_Cluster**](mscluster-cluster.md)
</dt> </dl>

 

 





