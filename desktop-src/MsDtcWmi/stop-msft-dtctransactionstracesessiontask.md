---
title: Stop method of the MSFT\_DtcTransactionsTraceSessionTask class
description: Stops the active DTC transactions trace session on the host.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '53097a54-f1a7-486a-9356-cf0783800a16'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-transaction-coordinator'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Stop method", "Stop method, MSFT_DtcTransactionsTraceSessionTask class", "MSFT_DtcTransactionsTraceSessionTask class, Stop method"]
topic_type:
- apiref
api_name:
- MSFT_DtcTransactionsTraceSessionTask.Stop
api_location:
- MsDtcWmi.dll
api_type:
- COM
---

# Stop method of the MSFT\_DtcTransactionsTraceSessionTask class

Stops the active DTC transactions trace session on the host.

## Syntax


```mof
uint32 Stop();
```



## Parameters

This method has no parameters.

## Return value

Returns "0" on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\MsDTC<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Msdtcwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsDtcWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DtcTransactionsTraceSessionTask**](msft-dtctransactionstracesessiontask.md)
</dt> </dl>

 

 





