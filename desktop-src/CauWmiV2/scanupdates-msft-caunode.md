---
title: ScanUpdates method of the MSFT\_CAUNode class
description: Scans for applicable updates.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0af9a10b-0577-4acb-afc6-79dd48615f35
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-aware-patching
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ScanUpdates method
- ScanUpdates method, MSFT_CAUNode class
- MSFT_CAUNode class, ScanUpdates method
topic_type:
- apiref
api_name:
- MSFT_CAUNode.ScanUpdates
api_location:
- CauWmiV2.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ScanUpdates method of the MSFT\_CAUNode class

Scans for applicable updates.

## Syntax


```mof
uint32 ScanUpdates(
  [in]  string                  QueryString,
  [in]  boolean                 IncludeRecommendedUpdates,
  [out] MSFT_CAU_ScanUpdateInfo Info[]
);
```



## Parameters

<dl> <dt>

*QueryString* \[in\]
</dt> <dd>

A Windows Update Agent query for finding applicable updates.

</dd> <dt>

*IncludeRecommendedUpdates* \[in\]
</dt> <dd>

**True** to include the recommended updates in the scan; otherwise, **false**.

</dd> <dt>

*Info* \[out\]
</dt> <dd>

An array of [**MSFT\_CAU\_ScanUpdateInfo**](msft-cau-scanupdateinfo.md) embedded instances that represent update information returned by the scan operation.

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

 

 





