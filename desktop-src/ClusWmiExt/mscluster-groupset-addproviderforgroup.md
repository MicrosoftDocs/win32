---
title: AddProviderForGroup method of the MSCluster\_GroupSet class
description: Adds a provider for the group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 77f1cb6c-855b-46bf-a15c-198f59db9d97
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddProviderForGroup method
- AddProviderForGroup method, MSCluster_GroupSet class
- MSCluster_GroupSet class, AddProviderForGroup method
topic_type:
- apiref
api_name:
- MSCluster_GroupSet.AddProviderForGroup
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddProviderForGroup method of the MSCluster\_GroupSet class

Adds a provider for the group.

## Syntax


```mof
uint32 AddProviderForGroup(
  [in] string Group,
  [in] string ProviderGroup,
  [in] string provider
);
```



## Parameters

<dl> <dt>

*Group* \[in\]
</dt> <dd>

The name of the group to find.

</dd> <dt>

*ProviderGroup* \[in\]
</dt> <dd>

The name of the group to add as a provider.

</dd> <dt>

*provider* \[in\]
</dt> <dd>

The name of the set to add as a provider.

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

 

 





