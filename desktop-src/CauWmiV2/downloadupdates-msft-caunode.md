---
title: DownloadUpdates method of the MSFT\_CAUNode class
description: Downloads updates to the node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f408f88c-bcc2-4c52-8e11-958c1eea02d6'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-aware-patching'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DownloadUpdates method", "DownloadUpdates method, MSFT_CAUNode class", "MSFT_CAUNode class, DownloadUpdates method"]
topic_type:
- apiref
api_name:
- MSFT_CAUNode.DownloadUpdates
api_location:
- CauWmiV2.dll
api_type:
- COM
---

# DownloadUpdates method of the MSFT\_CAUNode class

Downloads updates to the node.

## Syntax


```mof
uint32 DownloadUpdates(
  [in]  string                      QueryString,
  [in]  boolean                     IncludeRecommendedUpdates,
  [out] MSFT_CAU_DownloadUpdateInfo Info[]
);
```



## Parameters

<dl> <dt>

*QueryString* \[in\]
</dt> <dd>

A Windows Update Agent query for finding updates to download.

</dd> <dt>

*IncludeRecommendedUpdates* \[in\]
</dt> <dd>

**True** to include the recommended updates in the download; otherwise, **false**.

</dd> <dt>

*Info* \[out\]
</dt> <dd>

An array of [**MSFT\_CAU\_DownloadUpdateInfo**](msft-cau-downloadupdateinfo.md) embedded instances representing update information returned by the download operation.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ClusterUpdate<br/>                                      |
| MOF<br/>                      | <dl> <dt>CAUWMIv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CauWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_CAUNode**](msft-caunode.md)
</dt> </dl>

 

 





