---
title: Set method of the MSFT\_DtcTransactionsTraceSessionTask class
description: Modifies the DTC transactions trace setting of the host.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8503ae0b-79a7-47b5-bb0b-8bfd99250560'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-transaction-coordinator'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Set method", "Set method, MSFT_DtcTransactionsTraceSessionTask class", "MSFT_DtcTransactionsTraceSessionTask class, Set method"]
topic_type:
- apiref
api_name:
- MSFT_DtcTransactionsTraceSessionTask.Set
api_location:
- MsDtcWmi.dll
api_type:
- COM
---

# Set method of the MSFT\_DtcTransactionsTraceSessionTask class

Modifies the DTC transactions trace setting of the host.

## Syntax


```mof
uint32 Set(
  [in] uint32 BufferCount
);
```



## Parameters

<dl> <dt>

*BufferCount* \[in\]
</dt> <dd>

The number of buffers to use for a DTC transactions trace.

</dd> </dl>

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

 

 





