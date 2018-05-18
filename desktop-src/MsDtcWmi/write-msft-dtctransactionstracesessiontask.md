---
title: Write method of the MSFT\_DtcTransactionsTraceSessionTask class
description: Writes the data from an active DTC transactions trace session into the log file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5a00993d-4dc9-4409-9cdd-655fa1d6277d'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-transaction-coordinator'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Write method", "Write method, MSFT_DtcTransactionsTraceSessionTask class", "MSFT_DtcTransactionsTraceSessionTask class, Write method"]
topic_type:
- apiref
api_name:
- MSFT_DtcTransactionsTraceSessionTask.Write
api_location:
- MsDtcWmi.dll
api_type:
- COM
---

# Write method of the MSFT\_DtcTransactionsTraceSessionTask class

Writes the data from an active DTC transactions trace session into the log file.

## Syntax


```mof
uint32 Write();
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

 

 





