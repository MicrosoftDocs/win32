---
title: EnableStorageSpacesDirect method of the MSCluster\_StorageSpacesDirect class
description: Enables Storage Spaces Direct.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 89d3b337-1dbd-4173-a048-0931021ceb65
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- EnableStorageSpacesDirect method
- EnableStorageSpacesDirect method, MSCluster_StorageSpacesDirect class
- MSCluster_StorageSpacesDirect class, EnableStorageSpacesDirect method
topic_type:
- apiref
api_name:
- MSCluster_StorageSpacesDirect.EnableStorageSpacesDirect
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# EnableStorageSpacesDirect method of the MSCluster\_StorageSpacesDirect class

Enables Storage Spaces Direct.

## Syntax


```mof
uint32 EnableStorageSpacesDirect(
  [in] uint32  CacheState,
  [in] uint64  CacheMetadataReserveBytes,
  [in] string  XML,
  [in] string  CacheDeviceModel[],
  [in] boolean AutoConfig,
  [in] uint32  CachePageSizeKBytes,
  [in] string  PoolFriendlyName,
  [in] boolean SkipEligibilityChecks
);
```



## Parameters

<dl> <dt>

*CacheState* \[in\]
</dt> <dd>

The cache state.

<dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (0)


</dt> <dd></dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (1)


</dt> <dd></dd> </dl> </dd> <dt>

*CacheMetadataReserveBytes* \[in\]
</dt> <dd>

How many bytes that the cache should leave unused.

</dd> <dt>

*XML* \[in\]
</dt> <dd>

The XML describing disk related settings.

</dd> <dt>

*CacheDeviceModel* \[in\]
</dt> <dd>

The model prefixes of the disks to be used for cache.

</dd> <dt>

*AutoConfig* \[in\]
</dt> <dd>

Create storage pool and configure storage after enabling Storage Spaces Direct.

</dd> <dt>

*CachePageSizeKBytes* \[in\]
</dt> <dd>

Cache page size in KB.

<dt>



 (8)


</dt> <dd></dd> <dt>



 (16)


</dt> <dd></dd> <dt>



 (32)


</dt> <dd></dd> <dt>



 (64)


</dt> <dd></dd> </dl> </dd> <dt>

*PoolFriendlyName* \[in\]
</dt> <dd>

Pool friendly name to be used for S2D pool.

</dd> <dt>

*SkipEligibilityChecks* \[in\]
</dt> <dd>

Indicates that disk eligibility should be skipped.

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

 

 





