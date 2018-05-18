---
title: Get method of the MSFT\_DtcTransactionsTraceSessionTask class
description: Retrieves the DTC transactions trace session specific setting of the host.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1ffc72cc-28c4-40b1-a077-98fece2d2c61'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-transaction-coordinator'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, MSFT_DtcTransactionsTraceSessionTask class", "MSFT_DtcTransactionsTraceSessionTask class, Get method"]
topic_type:
- apiref
api_name:
- MSFT_DtcTransactionsTraceSessionTask.Get
api_location:
- MsDtcWmi.dll
api_type:
- COM
---

# Get method of the MSFT\_DtcTransactionsTraceSessionTask class

Retrieves the DTC transactions trace session specific setting of the host.

## Syntax


```mof
uint32 Get(
  [out] DtcTransactionsTraceSession cmdletOutput
);
```



## Parameters

<dl> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

A [**DtcTransactionsTraceSession**](dtctransactionstracesession.md) embedded instance containing the specified trace session.

</dd> </dl>

## Return value

Returns "0" on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\MsDTC<br/>                                                                  |
| Header<br/>                   | <dl> <dt>Wbemcli.h</dt> </dl>    |
| MOF<br/>                      | <dl> <dt>Msdtcwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsDtcWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DtcTransactionsTraceSessionTask**](msft-dtctransactionstracesessiontask.md)
</dt> </dl>

 

 





