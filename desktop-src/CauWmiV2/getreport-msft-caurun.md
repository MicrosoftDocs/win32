---
title: GetReport method of the MSFT\_CAUReportHelper class
description: Gets the contents of an updating run report.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8dd317bc-2049-4286-ac9f-4cbf8883362b
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-aware-patching
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetReport method
- GetReport method, MSFT_CAUReportHelper class
- MSFT_CAUReportHelper class, GetReport method
topic_type:
- apiref
api_name:
- MSFT_CAUReportHelper.GetReport
api_location:
- CauWmiV2.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetReport method of the MSFT\_CAUReportHelper class

Gets the contents of an updating run report.

## Syntax


```mof
uint32 GetReport(
  [in]  MSFT_CAURun_Report_ID    ReportId,
  [in]  Uint32                   ChunkSize,
  [out] MSFT_CAURun_Report_Chunk ReportChunks[]
);
```



## Parameters

<dl> <dt>

*ReportId* \[in\]
</dt> <dd>

An embedded instance of [**MSFT\_CAURun\_Report\_ID**](msft-caurun-report-id.md) that contains the identifier of the updating run report to be retrieved.

</dd> <dt>

*ChunkSize* \[in\]
</dt> <dd>

The size, in bytes, of a chunk of the updating run report.

</dd> <dt>

*ReportChunks* \[out\]
</dt> <dd>

An array of [**MSFT\_CAURun\_Report\_Chunk**](msft-caurun-report-chunk.md) embedded instances that contains the contents of each chunk of the updating run report.

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

[**MSFT\_CAUReportHelper**](msft-caureporthelper.md)
</dt> </dl>

 

 





