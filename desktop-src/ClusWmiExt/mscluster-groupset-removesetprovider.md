---
title: RemoveSetProvider method of the MSCluster\_GroupSet class
description: Removes a set as a provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'fd988d04-0993-4ee0-8306-290b16f35575'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoveSetProvider method", "RemoveSetProvider method, MSCluster_GroupSet class", "MSCluster_GroupSet class, RemoveSetProvider method"]
topic_type:
- apiref
api_name:
- MSCluster_GroupSet.RemoveSetProvider
api_location:
- ClusWMI.dll
api_type:
- COM
---

# RemoveSetProvider method of the MSCluster\_GroupSet class

Removes a set as a provider.

## Syntax


```mof
uint32 RemoveSetProvider(
  [in] string provider
);
```



## Parameters

<dl> <dt>

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

 

 





