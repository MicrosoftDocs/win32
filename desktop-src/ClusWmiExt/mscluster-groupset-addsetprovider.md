---
title: AddSetProvider method of the MSCluster\_GroupSet class
description: Adds a set as a provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8b129174-670b-4bfb-b908-29687de73b5b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddSetProvider method", "AddSetProvider method, MSCluster_GroupSet class", "MSCluster_GroupSet class, AddSetProvider method"]
topic_type:
- apiref
api_name:
- MSCluster_GroupSet.AddSetProvider
api_location:
- ClusWMI.dll
api_type:
- COM
---

# AddSetProvider method of the MSCluster\_GroupSet class

Adds a set as a provider.

## Syntax


```mof
uint32 AddSetProvider(
  [in] string provider
);
```



## Parameters

<dl> <dt>

*provider* \[in\]
</dt> <dd>

The name of the set to add as a provider.

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

 

 





