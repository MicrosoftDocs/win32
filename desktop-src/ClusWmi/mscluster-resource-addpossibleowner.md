---
title: AddPossibleOwner method of the MSCluster\_Resource class
description: Adds a possible owner (host) node to the list of possible owners for this resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ed8824b0-ae9f-4493-b5bc-b7b2f32623f7
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddPossibleOwner method
- AddPossibleOwner method, MSCluster_Resource class
- MSCluster_Resource class, AddPossibleOwner method
topic_type:
- apiref
api_name:
- MSCluster_Resource.AddPossibleOwner
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddPossibleOwner method of the MSCluster\_Resource class

Adds a possible owner (host) node to the list of possible owners for this resource.

## Syntax


```mof
void AddPossibleOwner(
  [in] string NodeName
);
```



## Parameters

<dl> <dt>

*NodeName* \[in\]
</dt> <dd>

A node that can be an owner (host) of this resource.

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

 

 





