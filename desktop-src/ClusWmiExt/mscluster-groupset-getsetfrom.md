---
title: GetSetFrom method of the MSCluster\_GroupSet class
description: Gets the sets that contain the group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 303e2ed7-8ff9-4df0-989e-7f24f7554baf
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSetFrom method
- GetSetFrom method, MSCluster_GroupSet class
- MSCluster_GroupSet class, GetSetFrom method
topic_type:
- apiref
api_name:
- MSCluster_GroupSet.GetSetFrom
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetSetFrom method of the MSCluster\_GroupSet class

Gets the sets that contain the group.

## Syntax


```mof
uint32 GetSetFrom(
  [in]  string             ContainedGroup,
  [in]  string             Name,
  [in]  string             provider,
  [in]  string             DependentGroup,
  [out] MSCluster_GroupSet Sets[]
);
```



## Parameters

<dl> <dt>

*ContainedGroup* \[in\]
</dt> <dd>

The name of the group that is contained in the set.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The name of the collection.

</dd> <dt>

*provider* \[in\]
</dt> <dd>

The name of the set that is providing for the sets.

</dd> <dt>

*DependentGroup* \[in\]
</dt> <dd>

The name of the group that the sets provide for.

</dd> <dt>

*Sets* \[out\]
</dt> <dd>

On success, returns a [**MSCluster\_GroupSet**](mscluster-groupset.md) that contains the group.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\MSCluster<br/>                                                                |
| MOF<br/>                      | <dl> <dt>ClusWmiExt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl>    |



## See also

<dl> <dt>

[**MSCluster\_GroupSet**](mscluster-groupset.md)
</dt> </dl>

 

 





