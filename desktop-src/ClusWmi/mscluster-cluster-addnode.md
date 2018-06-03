---
title: AddNode method of the MSCluster\_Cluster class
description: Adds a node to a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fa8af3c4-1553-40b2-b1b3-6f8c4f32fdf5
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddNode method
- AddNode method, MSCluster_Cluster class
- MSCluster_Cluster class, AddNode method
topic_type:
- apiref
api_name:
- MSCluster_Cluster.AddNode
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddNode method of the MSCluster\_Cluster class

Adds a node to a cluster.

## Syntax


```mof
void AddNode(
  [in] string NodeName
);
```



## Parameters

<dl> <dt>

*NodeName* \[in\]
</dt> <dd>

Name of the node to add.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The process that calls the **AddNode** method must be running on a node of the cluster.

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

 

 





