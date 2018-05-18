---
title: RemoveProviderForGroup method of the MSCluster\_GroupSet class
description: Removes a group provider for the group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7447eeca-8ec8-4a31-b3d5-8dece172ff3f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoveProviderForGroup method", "RemoveProviderForGroup method, MSCluster_GroupSet class", "MSCluster_GroupSet class, RemoveProviderForGroup method"]
topic_type:
- apiref
api_name:
- MSCluster_GroupSet.RemoveProviderForGroup
api_location:
- ClusWMI.dll
api_type:
- COM
---

# RemoveProviderForGroup method of the MSCluster\_GroupSet class

Removes a group provider for the group.

## Syntax


```mof
uint32 RemoveProviderForGroup(
  [in] string Group,
  [in] string ProviderGroup,
  [in] string provider
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

The name of the group to remove as a provider.

</dd> <dt>

*provider* \[in\]
</dt> <dd>

The name of the set to remove as a provider.

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

 

 





