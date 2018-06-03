---
title: SetByTraceSelectedParameterSet method of the MSFT\_DtcTransactionsTraceSettingTask class
description: Modifies the DTC transactions trace setting of the host.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: db734757-fa67-4147-829e-30fbf3adc3ac
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByTraceSelectedParameterSet method
- SetByTraceSelectedParameterSet method, MSFT_DtcTransactionsTraceSettingTask class
- MSFT_DtcTransactionsTraceSettingTask class, SetByTraceSelectedParameterSet method
topic_type:
- apiref
api_name:
- MSFT_DtcTransactionsTraceSettingTask.SetByTraceSelectedParameterSet
api_location:
- MsDtcWmi.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetByTraceSelectedParameterSet method of the MSFT\_DtcTransactionsTraceSettingTask class

Modifies the DTC transactions trace setting of the host.

## Syntax


```mof
uint32 SetByTraceSelectedParameterSet(
  [in] boolean AbortedTransactionsTracingEnabled,
  [in] boolean LongLivedTransactionsTracingEnabled
);
```



## Parameters

<dl> <dt>

*AbortedTransactionsTracingEnabled* \[in\]
</dt> <dd>

**true** to enable tracing for aborted transactions; otherwise, **false**.

</dd> <dt>

*LongLivedTransactionsTracingEnabled* \[in\]
</dt> <dd>

**true** to enable tracing for long-lived transactions; otherwise, **false**.

</dd> </dl>

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

[**MSFT\_DtcTransactionsTraceSettingTask**](msft-dtctransactionstracesettingtask.md)
</dt> </dl>

 

 





