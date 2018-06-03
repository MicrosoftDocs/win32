---
title: MoveToNewGroup method of the MSCluster\_Resource class
description: Moves the resource to a different group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ae1e5ff1-ecdb-46aa-ad62-40183ab429c6
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MoveToNewGroup method
- MoveToNewGroup method, MSCluster_Resource class
- MSCluster_Resource class, MoveToNewGroup method
topic_type:
- apiref
api_name:
- MSCluster_Resource.MoveToNewGroup
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MoveToNewGroup method of the MSCluster\_Resource class

Moves the [resource](https://msdn.microsoft.com/library/aa372152) to a different [group](https://msdn.microsoft.com/library/aa369645).

## Syntax


```mof
void MoveToNewGroup(
  [in] string Group
);
```



## Parameters

<dl> <dt>

*Group* \[in\]
</dt> <dd>

The name of the group to receive the resource.

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

[**MSCluster\_Resource**](mscluster-resource.md)
</dt> </dl>

 

 





