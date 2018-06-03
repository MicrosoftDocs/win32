---
title: RemovePossibleOwner method of the MSCluster\_Resource class
description: Removes a possible owner node (host) from the list of possible owners for this resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0c062b09-b6de-4df2-8c44-4b9726f2ad1d
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemovePossibleOwner method
- RemovePossibleOwner method, MSCluster_Resource class
- MSCluster_Resource class, RemovePossibleOwner method
topic_type:
- apiref
api_name:
- MSCluster_Resource.RemovePossibleOwner
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemovePossibleOwner method of the MSCluster\_Resource class

Removes a possible owner node (host) from the list of possible owners for this resource.

## Syntax


```mof
void RemovePossibleOwner(
  [in] string NodeName
);
```



## Parameters

<dl> <dt>

*NodeName* \[in\]
</dt> <dd>

The node that can no longer own (host) this resource.

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

 

 





