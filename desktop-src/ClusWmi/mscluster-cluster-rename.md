---
title: Rename method of the MSCluster\_Cluster class
description: Renames the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 19a8aad1-e074-4f7c-a398-f18e3189f396
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Rename method
- Rename method, MSCluster_Cluster class
- MSCluster_Cluster class, Rename method
topic_type:
- apiref
api_name:
- MSCluster_Cluster.Rename
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Rename method of the MSCluster\_Cluster class

Renames the [*cluster*](https://msdn.microsoft.com/library/aa369336#-wolf-cluster-gly).

## Syntax


```mof
void Rename(
  [in] string newName
);
```



## Parameters

<dl> <dt>

*newName* \[in\]
</dt> <dd>

String specifying the new cluster name.

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

 

 





