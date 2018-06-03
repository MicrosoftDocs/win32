---
title: GetDependencies method of the MSCluster\_Resource class
description: Gets the resource dependency expression.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9c339090-3fd9-4d1f-9826-e287885f4bab
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetDependencies method
- GetDependencies method, MSCluster_Resource class
- MSCluster_Resource class, GetDependencies method
topic_type:
- apiref
api_name:
- MSCluster_Resource.GetDependencies
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetDependencies method of the MSCluster\_Resource class

Gets the resource dependency expression.

## Syntax


```mof
void GetDependencies(
  [out] string  Expression,
  [in]  boolean AsResourceIds
);
```



## Parameters

<dl> <dt>

*Expression* \[out\]
</dt> <dd>

The expression that represents the resource dependencies.

</dd> <dt>

*AsResourceIds* \[in\]
</dt> <dd>

If the expression should contain the id of the resource instead of the resource friendly name.

**Windows Server 2008 R2 and Windows Server 2008:  **

This method is not supported before Windows Server 2012.

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

 

 





