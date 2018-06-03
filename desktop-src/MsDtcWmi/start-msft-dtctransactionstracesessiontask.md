---
title: Start method of the MSFT\_DtcTransactionsTraceSessionTask class
description: Starts a new DTC transactions trace session for the host.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6967fe68-3960-4e9b-aa8e-ea994e6d5325
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Start method
- Start method, MSFT_DtcTransactionsTraceSessionTask class
- MSFT_DtcTransactionsTraceSessionTask class, Start method
topic_type:
- apiref
api_name:
- MSFT_DtcTransactionsTraceSessionTask.Start
api_location:
- MsDtcWmi.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Start method of the MSFT\_DtcTransactionsTraceSessionTask class

Starts a new DTC transactions trace session for the host.

## Syntax


```mof
uint32 Start();
```



## Parameters

This method has no parameters.

## Return value

Returns "0" on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\MsDTC<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Msdtcwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsDtcWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DtcTransactionsTraceSessionTask**](msft-dtctransactionstracesessiontask.md)
</dt> </dl>

 

 





