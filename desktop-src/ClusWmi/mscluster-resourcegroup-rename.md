---
title: Rename method of the MSCluster\_ResourceGroup class
description: Renames the group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 91c5b957-9a6a-42bf-b2a5-74b910e6cc91
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Rename method
- Rename method, MSCluster_ResourceGroup class
- MSCluster_ResourceGroup class, Rename method
topic_type:
- apiref
api_name:
- MSCluster_ResourceGroup.Rename
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Rename method of the MSCluster\_ResourceGroup class

Renames the [group](https://msdn.microsoft.com/library/aa369645).

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

The new group name.

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

[**MSCluster\_ResourceGroup**](mscluster-resourcegroup.md)
</dt> </dl>

 

 





