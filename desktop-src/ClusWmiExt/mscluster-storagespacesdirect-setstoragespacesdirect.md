---
title: SetStorageSpacesDirect method of the MSCluster\_StorageSpacesDirect class
description: Sets Storage Spaces Direct.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ac2046b7-7408-4258-a31a-e7b93f794f6b
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetStorageSpacesDirect method
- SetStorageSpacesDirect method, MSCluster_StorageSpacesDirect class
- MSCluster_StorageSpacesDirect class, SetStorageSpacesDirect method
topic_type:
- apiref
api_name:
- MSCluster_StorageSpacesDirect.SetStorageSpacesDirect
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetStorageSpacesDirect method of the MSCluster\_StorageSpacesDirect class

Sets Storage Spaces Direct.

## Syntax


```mof
uint32 SetStorageSpacesDirect(
  [in] uint32  CacheState,
  [in] uint32  CacheModeHdd,
  [in] uint32  CacheModeSsd,
  [in] boolean SkipEligibilityChecks,
  [in] string  Nodes[]
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

*CacheModeHdd* \[in\]
</dt> <dd>

The cache mode for HDDs.

<dt>

<span id="ReadOnly"></span><span id="readonly"></span><span id="READONLY"></span>

**ReadOnly** (1)


</dt> <dd></dd> <dt>

<span id="ReadWrite"></span><span id="readwrite"></span><span id="READWRITE"></span>

**ReadWrite** (2)


</dt> <dd></dd> <dt>

<span id="WriteOnly"></span><span id="writeonly"></span><span id="WRITEONLY"></span>

**WriteOnly** (3)


</dt> <dd></dd> </dl> </dd> <dt>

*CacheModeSsd* \[in\]
</dt> <dd>

The cache mode for SSDs.

<dt>

<span id="ReadOnly"></span><span id="readonly"></span><span id="READONLY"></span>

**ReadOnly** (1)


</dt> <dd></dd> <dt>

<span id="ReadWrite"></span><span id="readwrite"></span><span id="READWRITE"></span>

**ReadWrite** (2)


</dt> <dd></dd> <dt>

<span id="WriteOnly"></span><span id="writeonly"></span><span id="WRITEONLY"></span>

**WriteOnly** (3)


</dt> <dd></dd> </dl> </dd> <dt>

*SkipEligibilityChecks* \[in\]
</dt> <dd>

**true** to skip disk eligibility.

</dd> <dt>

*Nodes* \[in\]
</dt> <dd>

Nodes on which the operation should take place. When omitted operation will be cluster-wide.

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

 

 





