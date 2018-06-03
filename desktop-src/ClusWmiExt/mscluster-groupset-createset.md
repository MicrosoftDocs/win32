---
title: CreateSet method of the MSCluster\_GroupSet class
description: Creates a set.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4a51210a-9af5-42bb-8f43-ecd64f87d231
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateSet method
- CreateSet method, MSCluster_GroupSet class
- MSCluster_GroupSet class, CreateSet method
topic_type:
- apiref
api_name:
- MSCluster_GroupSet.CreateSet
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateSet method of the MSCluster\_GroupSet class

Creates a set.

## Syntax


```mof
uint32 CreateSet(
  [in]  string             Name,
  [in]  string             Group[],
  [in]  string             provider[],
  [out] MSCluster_GroupSet CreatedSet
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the set to create.

</dd> <dt>

*Group* \[in\]
</dt> <dd>

The groups that should be in the container.

</dd> <dt>

*provider* \[in\]
</dt> <dd>

The sets that this container should be dependent on.

</dd> <dt>

*CreatedSet* \[out\]
</dt> <dd>

On success, returns a [**MSCluster\_GroupSet**](mscluster-groupset.md) that contains the newly created set.

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

 

 





