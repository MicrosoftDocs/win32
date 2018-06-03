---
title: RemoveServerPerformanceLog method of the MSFT\_ServerManagerTasks class
description: Remove the log file for a data collector set that are older than a given threshold.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e68fd25c-81f8-4cdd-976a-48441ae6276c
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveServerPerformanceLog method
- RemoveServerPerformanceLog method, MSFT_ServerManagerTasks class
- MSFT_ServerManagerTasks class, RemoveServerPerformanceLog method
topic_type:
- apiref
api_name:
- MSFT_ServerManagerTasks.RemoveServerPerformanceLog
api_location:
- MgmtProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoveServerPerformanceLog method of the MSFT\_ServerManagerTasks class

Remove the log file for a data collector set that are older than a given threshold.

## Syntax


```mof
uint32 RemoveServerPerformanceLog(
  [in] string CollectorName,
  [in] uint64 MillisecondThreshold
);
```



## Parameters

<dl> <dt>

*CollectorName* \[in\]
</dt> <dd>

The data collector set name.

</dd> <dt>

*MillisecondThreshold* \[in\]
</dt> <dd>

The threshold to use when removing the log files.

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
</dt> </dl>

 

 





