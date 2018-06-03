---
title: Rename method of the MSCluster\_Network class
description: Renames the network.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9c56f9c4-a180-4249-9fde-8a80f15519b0
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Rename method
- Rename method, MSCluster_Network class
- MSCluster_Network class, Rename method
topic_type:
- apiref
api_name:
- MSCluster_Network.Rename
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Rename method of the MSCluster\_Network class

Renames the network.

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

The new network name.

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

[**MSCluster\_Network**](mscluster-network.md)
</dt> </dl>

 

 





