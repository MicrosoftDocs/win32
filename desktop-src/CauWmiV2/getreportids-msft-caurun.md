---
title: GetReportIDs method of the MSFT\_CAUReportHelper class
description: Gets identifiers for updating run reports that are stored on the current node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4d75602b-efa4-4a00-b37c-f3b36544e4a6'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-aware-patching'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetReportIDs method", "GetReportIDs method, MSFT_CAUReportHelper class", "MSFT_CAUReportHelper class, GetReportIDs method"]
topic_type:
- apiref
api_name:
- MSFT_CAUReportHelper.GetReportIDs
api_location:
- CauWmiV2.dll
api_type:
- COM
---

# GetReportIDs method of the MSFT\_CAUReportHelper class

Gets identifiers for updating run reports that are stored on the current node.

## Syntax


```mof
uint32 GetReportIDs(
  [out] MSFT_CAURun_Report_ID ReportID[]
);
```



## Parameters

<dl> <dt>

*ReportID* \[out\]
</dt> <dd>

An array of [**MSFT\_CAURun\_Report\_ID**](https://msdn.microsoft.com/library/hh706781) embedded instances that contains the identifiers of updating run reports on the current node.

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

 

 





