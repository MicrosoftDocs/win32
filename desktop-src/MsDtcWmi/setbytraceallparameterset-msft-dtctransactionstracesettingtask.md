---
title: SetByTraceAllParameterSet method of the MSFT\_DtcTransactionsTraceSettingTask class
description: Modifies the DTC transactions trace setting of the host.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd444f31b-27c7-4195-beb2-d841a3d21e11'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-transaction-coordinator'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetByTraceAllParameterSet method", "SetByTraceAllParameterSet method, MSFT_DtcTransactionsTraceSettingTask class", "MSFT_DtcTransactionsTraceSettingTask class, SetByTraceAllParameterSet method"]
topic_type:
- apiref
api_name:
- MSFT_DtcTransactionsTraceSettingTask.SetByTraceAllParameterSet
api_location:
- MsDtcWmi.dll
api_type:
- COM
---

# SetByTraceAllParameterSet method of the MSFT\_DtcTransactionsTraceSettingTask class

Modifies the DTC transactions trace setting of the host.

## Syntax


```mof
uint32 SetByTraceAllParameterSet(
  [in] boolean AllTransactionsTracingEnabled
);
```



## Parameters

<dl> <dt>

*AllTransactionsTracingEnabled* \[in\]
</dt> <dd>

**true** to enable tracing for all transactions; otherwise, **false**.

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

[**MSFT\_DtcTransactionsTraceSettingTask**](msft-dtctransactionstracesettingtask.md)
</dt> </dl>

 

 





