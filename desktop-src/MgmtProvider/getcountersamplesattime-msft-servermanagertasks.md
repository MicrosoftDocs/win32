---
title: GetCounterSamplesAtTime method of the MSFT\_ServerManagerTasks class
description: Retrieves the performance counter samples logged by a Data Collector Set at the specified time stamps.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 85434ea7-b480-4b2b-a95a-36e8d009a18d
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetCounterSamplesAtTime method
- GetCounterSamplesAtTime method, MSFT_ServerManagerTasks class
- MSFT_ServerManagerTasks class, GetCounterSamplesAtTime method
topic_type:
- apiref
api_name:
- MSFT_ServerManagerTasks.GetCounterSamplesAtTime
api_location:
- MgmtProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetCounterSamplesAtTime method of the MSFT\_ServerManagerTasks class

Retrieves the performance counter samples logged by a Data Collector Set at the specified time stamps.

## Syntax


```mof
uint32 GetCounterSamplesAtTime(
  [in]  string                               CollectorName,
  [in]  string                               CounterPaths[],
  [in]  datetime                             Timestamps[],
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

*Timestamps* \[in\]
</dt> <dd>

The list of timestamps to filter the performance counter samples.

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

 

 





