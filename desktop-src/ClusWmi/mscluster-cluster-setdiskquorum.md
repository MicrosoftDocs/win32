---
title: SetDiskQuorum method of the MSCluster\_Cluster class
description: Sets the quorum behavior to not be a majority and to use the passed-in disk as the quorum resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 976eeaa3-6bf7-4823-8833-86d8b2b52ea9
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetDiskQuorum method
- SetDiskQuorum method, MSCluster_Cluster class
- MSCluster_Cluster class, SetDiskQuorum method
topic_type:
- apiref
api_name:
- MSCluster_Cluster.SetDiskQuorum
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetDiskQuorum method of the MSCluster\_Cluster class

Sets the quorum behavior to not be a majority and to use the passed-in disk as the quorum resource.

## Syntax


```mof
void SetDiskQuorum(
  [in] string Resource,
  [in] string QuorumPath
);
```



## Parameters

<dl> <dt>

*Resource* \[in\]
</dt> <dd>

The name of the disk quorum resource.

</dd> <dt>

*QuorumPath* \[in\]
</dt> <dd>

The optional path that will be used to maintain quorum files.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_Cluster**](mscluster-cluster.md)
</dt> </dl>

 

 





