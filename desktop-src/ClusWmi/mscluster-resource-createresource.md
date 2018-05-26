---
title: CreateResource method of the MSCluster\_Resource class
description: Creates a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c577fdbc-935a-4eb8-b461-e974069b3f11
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateResource method
- CreateResource method, MSCluster_Resource class
- MSCluster_Resource class, CreateResource method
topic_type:
- apiref
api_name:
- MSCluster_Resource.CreateResource
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreateResource method of the MSCluster\_Resource class

Creates a [resource](https://msdn.microsoft.com/library/aa372152).

## Syntax


```mof
void CreateResource(
  [in]      string  Group,
  [in]      string  ResourceName,
  [in]      string  ResourceType,
  [in]      boolean SeparateMonitor = ,
  [in, out] string  Id
);
```



## Parameters

<dl> <dt>

*Group* \[in\]
</dt> <dd>

The name of the group to receive the resource.

</dd> <dt>

*ResourceName* \[in\]
</dt> <dd>

The name to assign to the resource.

</dd> <dt>

*ResourceType* \[in\]
</dt> <dd>

The type of resource to create.

</dd> <dt>

*SeparateMonitor* \[in\]
</dt> <dd>

**TRUE** if the resource needs a separate resource monitor; otherwise, **FALSE**. The default value is **FALSE**.

</dd> <dt>

*Id* \[in, out\]
</dt> <dd>

Id of the resource.

**Windows Server 2008 R2 and Windows Server 2008:  **

This parameter is not supported before Windows Server 2012.

</dd> </dl>

## Return value

This method has no return values.

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

 

 





