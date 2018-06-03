---
title: GetCounterSamplesInTimeRange method of the MSFT\_ServerManagerTasks class
description: Retrieves the performance counter samples logged by a Data Collector Set in a particular time range.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7bbeda83-3de6-49d5-874e-c7631d3561dc
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetCounterSamplesInTimeRange method
- GetCounterSamplesInTimeRange method, MSFT_ServerManagerTasks class
- MSFT_ServerManagerTasks class, GetCounterSamplesInTimeRange method
topic_type:
- apiref
api_name:
- MSFT_ServerManagerTasks.GetCounterSamplesInTimeRange
api_location:
- MgmtProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetCounterSamplesInTimeRange method of the MSFT\_ServerManagerTasks class

Retrieves the performance counter samples logged by a Data Collector Set in a particular time range.

## Syntax


```mof
uint32 GetCounterSamplesInTimeRange(
  [in]  string                               CollectorName,
  [in]  string                               CounterPaths[],
  [in]  datetime                             StartTime,
  [in]  datetime                             EndTime,
  [in]  uint32                               BatchSize,
  [out] MSFT_ServerPerformanceCounterSamples cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*CollectorName* \[in\]
</dt> <dd>

The name of the Data Collector Set in Performance Logs & Alerts.

</dd> <dt>

*CounterPaths* \[in\]
</dt> <dd>

The list of performance counters to query in the performance log file.

</dd> <dt>

*StartTime* \[in\]
</dt> <dd>

The start boundary of the time range.

</dd> <dt>

*EndTime* \[in\]
</dt> <dd>

The end boundary of the time range.

</dd> <dt>

*BatchSize* \[in\]
</dt> <dd>

The batch size to use for streaming data back to the client.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An array of embedded instances of [**MSFT\_ServerPerformanceCounterSamples**](msft-serverperformancecountersamples.md) that represent the selected performance counter samples.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\Windows\\ServerManager<br/>                                                     |
| MOF<br/>                      | <dl> <dt>MgmtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MgmtProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_ServerManagerTasks**](msft-servermanagertasks.md)
</dt> <dt>

[**MSFT\_ServerPerformanceCounterSamples**](msft-serverperformancecountersamples.md)
</dt> </dl>

 

 





