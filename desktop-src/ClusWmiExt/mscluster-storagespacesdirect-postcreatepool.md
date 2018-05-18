---
title: PostCreatePool method of the MSCluster\_StorageSpacesDirect class
description: Creates storage tiers used by Storage Spaces Direct.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7f53545a-db67-4a01-8701-21c7eb77c8ad'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PostCreatePool method", "PostCreatePool method, MSCluster_StorageSpacesDirect class", "MSCluster_StorageSpacesDirect class, PostCreatePool method"]
---

# PostCreatePool method of the MSCluster\_StorageSpacesDirect class

Creates storage tiers used by Storage Spaces Direct.

## Syntax


```mof
uint32 PostCreatePool(
  [in] string  PoolUniqueId,
  [in] uint32  nNodesInSite,
  [in] boolean PoolHasNonCacheHdd,
  [in] boolean PoolHasNonCacheSsd
);
```



## Parameters

<dl> <dt>

*PoolUniqueId* \[in\]
</dt> <dd>

Pool Unique ID for which storage tiers have to be created.

</dd> <dt>

*nNodesInSite* \[in\]
</dt> <dd>

Number of nodes residing in the site hosting the storage pool.

</dd> <dt>

*PoolHasNonCacheHdd* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*PoolHasNonCacheSsd* \[in\]
</dt> <dd>

TBD

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\MSCluster<br/>                                                                |
| MOF<br/>                      | <dl> <dt>ClusWmiExt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl>    |



## See also

<dl> <dt>

[**MSCluster\_StorageSpacesDirect**](mscluster-storagespacesdirect.md)
</dt> </dl>

 

 





