---
title: MoveToNewHost method of the MSCluster\_ClusterSharedVolume class
description: Moves the cluster shared volume to a another node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1fbe1d2e-e2b1-47fc-b819-8a5c7e0caa64
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MoveToNewHost method
- MoveToNewHost method, MSCluster_ClusterSharedVolume class
- MSCluster_ClusterSharedVolume class, MoveToNewHost method
topic_type:
- apiref
api_name:
- MSCluster_ClusterSharedVolume.MoveToNewHost
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MoveToNewHost method of the MSCluster\_ClusterSharedVolume class

Moves the cluster shared volume to a another node. All volumes of this resource will also be moved.

## Syntax


```mof
void MoveToNewHost(
  [in] string HostName
);
```



## Parameters

<dl> <dt>

*HostName* \[in\]
</dt> <dd>

Name of the host which to move the cluster shared volume to.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                      |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_ClusterSharedVolume**](mscluster-clustersharedvolume.md)
</dt> </dl>

 

 





