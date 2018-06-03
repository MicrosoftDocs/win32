---
title: CreateResourceType method of the MSCluster\_ResourceType class
description: Creates a resource type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c75ec4da-f2bb-4544-8b22-fd9c14b14f86
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateResourceType method
- CreateResourceType method, MSCluster_ResourceType class
- MSCluster_ResourceType class, CreateResourceType method
topic_type:
- apiref
api_name:
- MSCluster_ResourceType.CreateResourceType
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateResourceType method of the MSCluster\_ResourceType class

Creates a [resource type](https://msdn.microsoft.com/library/aa372279).

## Syntax


```mof
void CreateResourceType(
  [in] string Name,
  [in] string DisplayName,
  [in] string DLLName,
  [in] uint32 LooksAlivePollInterval,
  [in] uint32 IsAlivePollInterval
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the resource type.

</dd> <dt>

*DisplayName* \[in\]
</dt> <dd>

The display name of the resource type.

</dd> <dt>

*DLLName* \[in\]
</dt> <dd>

The fully qualified name of the resource DLL for the resource type.

</dd> <dt>

*LooksAlivePollInterval* \[in\]
</dt> <dd>

The default value (in milliseconds) to be used as the poll interval needed by the new resource type's [**LooksAlive**](https://msdn.microsoft.com/library/aa370972) function.

</dd> <dt>

*IsAlivePollInterval* \[in\]
</dt> <dd>

Default value (in milliseconds) to be used as the poll interval needed by the new resource type's [**IsAlive**](https://msdn.microsoft.com/library/aa370496) function.

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

[**MSCluster\_ResourceType**](mscluster-resourcetype.md)
</dt> </dl>

 

 





