---
title: SetByTraceSet method of the MSFT\_DtcTransactionTask class
description: Indicates whether to trace the transaction.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 838743ee-ad04-443c-b7ec-a570c695a30a
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByTraceSet method
- SetByTraceSet method, MSFT_DtcTransactionTask class
- MSFT_DtcTransactionTask class, SetByTraceSet method
topic_type:
- apiref
api_name:
- MSFT_DtcTransactionTask.SetByTraceSet
api_location:
- MsDtcWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetByTraceSet method of the MSFT\_DtcTransactionTask class

Indicates whether to trace the transaction.

## Syntax


```mof
uint32 SetByTraceSet(
  [in] string  DtcName,
  [in] string  TransactionId,
  [in] boolean Trace
);
```



## Parameters

<dl> <dt>

*DtcName* \[in\]
</dt> <dd>

The name of the DTC instance. This method modifies the state of a transaction in the DTC host-level properties for this instance.

</dd> <dt>

*TransactionId* \[in\]
</dt> <dd>

The ID of the transaction.

</dd> <dt>

*Trace* \[in\]
</dt> <dd>

**true** to trace the transaction; otherwise, **false**.

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

[**MSFT\_DtcTransactionTask**](msft-dtctransactiontask.md)
</dt> </dl>

 

 





