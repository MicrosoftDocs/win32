---
title: ForceCleanup method of the MSCluster\_Cluster class
description: Forces a node to be cleaned up.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 47136071-6771-4662-bf42-0ea572cfcb52
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ForceCleanup method
- ForceCleanup method, MSCluster_Cluster class
- MSCluster_Cluster class, ForceCleanup method
topic_type:
- apiref
api_name:
- MSCluster_Cluster.ForceCleanup
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ForceCleanup method of the MSCluster\_Cluster class

Forces a node to be cleaned up.

## Syntax


```mof
void ForceCleanup(
  [in] string NodeName,
  [in] uint32 Timeout
);
```



## Parameters

<dl> <dt>

*NodeName* \[in\]
</dt> <dd>

The name of the cluster node to clean up.

</dd> <dt>

*Timeout* \[in\]
</dt> <dd>

The number of milliseconds that this method will wait for cleanup to complete.

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

 

 





