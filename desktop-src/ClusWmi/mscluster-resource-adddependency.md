---
title: AddDependency method of the MSCluster\_Resource class
description: Creates a dependency relationship between two resources.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 14fb8fe2-77f1-4e03-a1bc-9d884aa6029c
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddDependency method
- AddDependency method, MSCluster_Resource class
- MSCluster_Resource class, AddDependency method
topic_type:
- apiref
api_name:
- MSCluster_Resource.AddDependency
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddDependency method of the MSCluster\_Resource class

Creates a [dependency](https://msdn.microsoft.com/library/aa372236) relationship between two [resources](https://msdn.microsoft.com/library/aa372152).

## Syntax


```mof
void AddDependency(
  [in] string Resource
);
```



## Parameters

<dl> <dt>

*Resource* \[in\]
</dt> <dd>

The resource that this resource should depend on.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| Header<br/>                   | <dl> <dt>Iiisext.h</dt> </dl>   |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_Resource**](mscluster-resource.md)
</dt> </dl>

 

 





