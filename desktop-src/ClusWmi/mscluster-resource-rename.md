---
title: Rename method of the MSCluster\_Resource class
description: Renames the resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 39aad4f1-4946-4cc3-92b6-1e4a3d24ec28
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Rename method
- Rename method, MSCluster_Resource class
- MSCluster_Resource class, Rename method
topic_type:
- apiref
api_name:
- MSCluster_Resource.Rename
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Rename method of the MSCluster\_Resource class

Renames the [resource](https://msdn.microsoft.com/library/aa372152).

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

The new resource name.

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

 

 





