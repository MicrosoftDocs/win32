---
title: DisableStorageSpacesDirect method of the MSCluster\_StorageSpacesDirect class
description: Disables Storage Spaces Direct.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0e3b5763-2b36-4b40-aad6-72f4d5e886df
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DisableStorageSpacesDirect method
- DisableStorageSpacesDirect method, MSCluster_StorageSpacesDirect class
- MSCluster_StorageSpacesDirect class, DisableStorageSpacesDirect method
topic_type:
- apiref
api_name:
- MSCluster_StorageSpacesDirect.DisableStorageSpacesDirect
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DisableStorageSpacesDirect method of the MSCluster\_StorageSpacesDirect class

Disables Storage Spaces Direct.

## Syntax


```mof
uint32 DisableStorageSpacesDirect(
  [in] boolean CleanupCache
);
```



## Parameters

<dl> <dt>

*CleanupCache* \[in\]
</dt> <dd>

**true** to flush and purge data from solid-state drives (SSDs). This removes cache partitions. Note that this removal can take a significant amount of time.

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

 

 





