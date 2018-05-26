---
title: SetPerformanceCollectorState method of the MSFT\_ServerManagerTasks class
description: Configures the state of a Data Collector Set in Performance Logs Alerts.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 24ead768-f893-4226-841e-3415b59d676f
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetPerformanceCollectorState method
- SetPerformanceCollectorState method, MSFT_ServerManagerTasks class
- MSFT_ServerManagerTasks class, SetPerformanceCollectorState method
topic_type:
- apiref
api_name:
- MSFT_ServerManagerTasks.SetPerformanceCollectorState
api_location:
- MgmtProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetPerformanceCollectorState method of the MSFT\_ServerManagerTasks class

Configures the state of a Data Collector Set in Performance Logs & Alerts.

## Syntax


```mof
uint32 SetPerformanceCollectorState(
  [in] string CollectorName,
  [in] uint8  State
);
```



## Parameters

<dl> <dt>

*CollectorName* \[in\]
</dt> <dd>

The name of the Data Collector Set in Performance Logs & Alerts.

</dd> <dt>

*State* \[in\]
</dt> <dd>

The required state of the Data Collector Set.

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

 

 





