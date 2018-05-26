---
title: CreateStorageResource method of the MSCluster\_AvailableDisk class
description: Creates the available disk storage resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 91760188-D74F-4A7C-BFC0-C295A4B90E0D
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateStorageResource method
- CreateStorageResource method, MSCluster_AvailableDisk interface
- MSCluster_AvailableDisk interface, CreateStorageResource method
topic_type:
- apiref
api_name:
- MSCluster_AvailableDisk.CreateStorageResource
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreateStorageResource method of the MSCluster\_AvailableDisk class

Creates the available disk storage resource.

## Syntax


```mof
void CreateStorageResource(
  [in]  string ResourceName,
  [out] string Path
);
```



## Parameters

<dl> <dt>

*ResourceName* \[in\]
</dt> <dd>

The optional resource name to use when creating the storage resource.

</dd> <dt>

*Path* \[out\]
</dt> <dd>

The path to the created physical disk resource.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_AvailableDisk**](mscluster-availabledisk.md)
</dt> </dl>

 

 





