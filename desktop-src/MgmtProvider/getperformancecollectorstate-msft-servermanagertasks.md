---
title: GetPerformanceCollectorState method of the MSFT\_ServerManagerTasks class
description: Retrieves the state of a Data Collector Set in Performance Logs Alerts.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 09c23ae3-4a83-433d-8973-f466b3389869
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetPerformanceCollectorState method
- GetPerformanceCollectorState method, MSFT_ServerManagerTasks class
- MSFT_ServerManagerTasks class, GetPerformanceCollectorState method
topic_type:
- apiref
api_name:
- MSFT_ServerManagerTasks.GetPerformanceCollectorState
api_location:
- MgmtProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetPerformanceCollectorState method of the MSFT\_ServerManagerTasks class

Retrieves the state of a Data Collector Set in Performance Logs & Alerts.

## Syntax


```mof
uint32 GetPerformanceCollectorState(
  [in]  string CollectorName,
  [out] uint8  cmdletOutput
);
```



## Parameters

<dl> <dt>

*CollectorName* \[in\]
</dt> <dd>

The name of the Data Collector Set in Performance Logs & Alerts.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The state of the data collector set in PLA.

<dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>

**Stopped** (0)


</dt> <dd></dd> <dt>

<span id="Running"></span><span id="running"></span><span id="RUNNING"></span>

**Running** (1)


</dt> <dd></dd> </dl> </dd> </dl>

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
</dt> </dl>

 

 





