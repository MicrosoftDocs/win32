---
title: SetStorageSpacesDirectDisk method of the MSCluster\_StorageSpacesDirect class
description: Sets Storage Spaces Direct Disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0fb0f334-e26e-4df2-95ed-e9cbbee1de2c
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetStorageSpacesDirectDisk method
- SetStorageSpacesDirectDisk method, MSCluster_StorageSpacesDirect class
- MSCluster_StorageSpacesDirect class, SetStorageSpacesDirectDisk method
topic_type:
- apiref
api_name:
- MSCluster_StorageSpacesDirect.SetStorageSpacesDirectDisk
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetStorageSpacesDirectDisk method of the MSCluster\_StorageSpacesDirect class

Sets Storage Spaces Direct Disk.

## Syntax


```mof
uint32 SetStorageSpacesDirectDisk(
  [in] boolean CanBeClaimed,
  [in] string  PhysicalDiskIds[]
);
```



## Parameters

<dl> <dt>

*CanBeClaimed* \[in\]
</dt> <dd>

Indicates whether the disk can be claimed.

</dd> <dt>

*PhysicalDiskIds* \[in\]
</dt> <dd>

The physical disks to be set.

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

[**MSCluster\_StorageSpacesDirect**](mscluster-storagespacesdirect.md)
</dt> </dl>

 

 





