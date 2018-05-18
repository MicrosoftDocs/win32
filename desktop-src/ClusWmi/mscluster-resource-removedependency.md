---
title: RemoveDependency method of the MSCluster\_Resource class
description: Removes a dependency relationship between two resources.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1ce063e3-bf90-4987-9f96-b858a7f39e31'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoveDependency method", "RemoveDependency method, MSCluster_Resource class", "MSCluster_Resource class, RemoveDependency method"]
topic_type:
- apiref
api_name:
- MSCluster_Resource.RemoveDependency
api_location:
- ClusWMI.dll
api_type:
- COM
---

# RemoveDependency method of the MSCluster\_Resource class

Removes a [dependency](https://msdn.microsoft.com/library/aa372236) relationship between two [resources](https://msdn.microsoft.com/library/aa372152).

## Syntax


```mof
void RemoveDependency(
  [in] string Resource
);
```



## Parameters

<dl> <dt>

*Resource* \[in\]
</dt> <dd>

The resource that this resource should no longer depend on.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| Header<br/>                   | <dl> <dt>Iiisext.h</dt> </dl>   |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_Resource**](mscluster-resource.md)
</dt> </dl>

 

 





