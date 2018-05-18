---
title: AddGroupToSet method of the MSCluster\_GroupSet class
description: Adds a group to the set.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9e854b7c-43ec-4577-95ba-199e8801f132'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddGroupToSet method", "AddGroupToSet method, MSCluster_GroupSet class", "MSCluster_GroupSet class, AddGroupToSet method"]
topic_type:
- apiref
api_name:
- MSCluster_GroupSet.AddGroupToSet
api_location:
- ClusWMI.dll
api_type:
- COM
---

# AddGroupToSet method of the MSCluster\_GroupSet class

Adds a group to the set.

## Syntax


```mof
uint32 AddGroupToSet(
  [in] string Group
);
```



## Parameters

<dl> <dt>

*Group* \[in\]
</dt> <dd>

The name of the group to add to the set.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\MSCluster<br/>                                                                |
| MOF<br/>                      | <dl> <dt>ClusWmiExt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl>    |



## See also

<dl> <dt>

[**MSCluster\_GroupSet**](mscluster-groupset.md)
</dt> </dl>

 

 





