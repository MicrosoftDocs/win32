---
title: SetByAbortSet method of the MSFT\_DtcTransactionTask class
description: Indicates whether to abort the transaction.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c6569990-ee38-4f37-b2b9-df6ef1b50858
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByAbortSet method
- SetByAbortSet method, MSFT_DtcTransactionTask class
- MSFT_DtcTransactionTask class, SetByAbortSet method
topic_type:
- apiref
api_name:
- MSFT_DtcTransactionTask.SetByAbortSet
api_location:
- MsDtcWmi.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetByAbortSet method of the MSFT\_DtcTransactionTask class

Indicates whether to abort the transaction.

## Syntax


```mof
uint32 SetByAbortSet(
  [in] string  DtcName,
  [in] string  TransactionId,
  [in] boolean Abort
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

*Abort* \[in\]
</dt> <dd>

**true** to abort the transaction; otherwise, **false**.

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

 

 





