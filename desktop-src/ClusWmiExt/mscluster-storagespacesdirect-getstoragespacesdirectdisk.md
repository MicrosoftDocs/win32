---
title: GetStorageSpacesDirectDisk method of the MSCluster\_StorageSpacesDirect class
description: Sets Storage Spaces Direct Disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d8bd5571-8054-406f-9b30-9e0bd1699362
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetStorageSpacesDirectDisk method
- GetStorageSpacesDirectDisk method, MSCluster_StorageSpacesDirect class
- MSCluster_StorageSpacesDirect class, GetStorageSpacesDirectDisk method
topic_type:
- apiref
api_name:
- MSCluster_StorageSpacesDirect.GetStorageSpacesDirectDisk
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetStorageSpacesDirectDisk method of the MSCluster\_StorageSpacesDirect class

Sets Storage Spaces Direct Disk.

## Syntax


```mof
uint32 GetStorageSpacesDirectDisk(
  [in]  boolean CanBeClaimed,
  [out] string  PhysicalDiskIds[]
);
```



## Parameters

<dl> <dt>

*CanBeClaimed* \[in\]
</dt> <dd>

Indicates whether the disk can be claimed.

</dd> <dt>

*PhysicalDiskIds* \[out\]
</dt> <dd>

The physical disks.

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

 

 





