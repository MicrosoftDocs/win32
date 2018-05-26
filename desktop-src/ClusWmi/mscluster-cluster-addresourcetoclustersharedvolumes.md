---
title: AddResourceToClusterSharedVolumes method of the MSCluster\_Cluster class
description: Adds storage to Cluster Shared Volumes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f0860020-f458-4977-9bb7-6c1eb50ab652
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddResourceToClusterSharedVolumes method
- AddResourceToClusterSharedVolumes method, MSCluster_Cluster class
- MSCluster_Cluster class, AddResourceToClusterSharedVolumes method
topic_type:
- apiref
api_name:
- MSCluster_Cluster.AddResourceToClusterSharedVolumes
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddResourceToClusterSharedVolumes method of the MSCluster\_Cluster class

Adds storage to Cluster Shared Volumes.

## Syntax


```mof
void AddResourceToClusterSharedVolumes(
  [in] String Resource
);
```



## Parameters

<dl> <dt>

*Resource* \[in\]
</dt> <dd>

The name of the physical disk resource to add to Cluster Shared Volumes.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                      |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| Header<br/>                   | <dl> <dt>Clusapi.h</dt> </dl>   |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_Cluster**](mscluster-cluster.md)
</dt> </dl>

 

 





