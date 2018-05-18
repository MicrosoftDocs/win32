---
title: EvictNode method of the MSCluster\_Cluster class
description: Removes a specified node from the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd90eec1b-3800-4d78-95aa-b449a1462e68'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["EvictNode method", "EvictNode method, MSCluster_Cluster class", "MSCluster_Cluster class, EvictNode method"]
topic_type:
- apiref
api_name:
- MSCluster_Cluster.EvictNode
api_location:
- ClusWMI.dll
api_type:
- COM
---

# EvictNode method of the MSCluster\_Cluster class

Removes a specified node from the cluster.

## Syntax


```mof
void EvictNode(
  [in] string NodeName
);
```



## Parameters

<dl> <dt>

*NodeName* \[in\]
</dt> <dd>

Name of the cluster node to evict.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_Cluster**](mscluster-cluster.md)
</dt> </dl>

 

 





