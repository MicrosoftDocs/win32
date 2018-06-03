---
title: InstallUpdates method of the MSFT\_CAUNode class
description: Installs updates to the node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5668bb18-6a7d-4174-afc5-1127f5adf486
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-aware-patching
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- InstallUpdates method
- InstallUpdates method, MSFT_CAUNode class
- MSFT_CAUNode class, InstallUpdates method
topic_type:
- apiref
api_name:
- MSFT_CAUNode.InstallUpdates
api_location:
- CauWmiV2.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# InstallUpdates method of the MSFT\_CAUNode class

Installs updates to the node.

## Syntax


```mof
uint32 InstallUpdates(
  [in]  string                     QueryString,
  [in]  boolean                    IncludeRecommendedUpdates,
  [out] MSFT_CAU_InstallUpdateInfo Info[]
);
```



## Parameters

<dl> <dt>

*QueryString* \[in\]
</dt> <dd>

A Windows Update Agent query for finding updates to install.

</dd> <dt>

*IncludeRecommendedUpdates* \[in\]
</dt> <dd>

**True** to include the recommended updates in the installation; otherwise, **false**.

</dd> <dt>

*Info* \[out\]
</dt> <dd>

An array of [**MSFT\_CAU\_InstallUpdateInfo**](msft-cau-installupdateinfo.md) embedded instances that represent update information returned by the installation operation.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ClusterUpdate<br/>                                      |
| MOF<br/>                      | <dl> <dt>CAUWMIv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CauWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_CAUNode**](msft-caunode.md)
</dt> </dl>

 

 





