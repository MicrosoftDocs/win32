---
title: PutReport method of the MSFT\_CAUReportHelper class
description: Saves a chunk of an updating run report on the current node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e282c91b-58aa-4058-9e8a-934c8f32bc8b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-aware-patching'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PutReport method", "PutReport method, MSFT_CAUReportHelper class", "MSFT_CAUReportHelper class, PutReport method"]
topic_type:
- apiref
api_name:
- MSFT_CAUReportHelper.PutReport
api_location:
- CauWmiV2.dll
api_type:
- COM
---

# PutReport method of the MSFT\_CAUReportHelper class

Saves a chunk of an updating run report on the current node.

## Syntax


```mof
uint32 PutReport(
  [in] Uint64                   ReportSize,
  [in] MSFT_CAURun_Report_Chunk ReportChunk,
  [in] boolean                  LastChunk
);
```



## Parameters

<dl> <dt>

*ReportSize* \[in\]
</dt> <dd>

The total size, in bytes, of the updating run report to save.

</dd> <dt>

*ReportChunk* \[in\]
</dt> <dd>

An embedded instance of [**MSFT\_CAURun\_Report\_Chunk**](msft-caurun-report-chunk.md) that contains the contents of a chunk of the updating run report.

</dd> <dt>

*LastChunk* \[in\]
</dt> <dd>

**True** to specify that this is the last chunk in the updating run report; otherwise, **false**.

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

[**MSFT\_CAUReportHelper**](msft-caureporthelper.md)
</dt> </dl>

 

 





