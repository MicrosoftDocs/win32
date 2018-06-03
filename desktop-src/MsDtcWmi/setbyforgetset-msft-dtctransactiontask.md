---
title: SetByForgetSet method of the MSFT\_DtcTransactionTask class
description: Indicates whether to forget the transaction.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dfd16d53-8ed9-4857-a2ca-84357cb3f434
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByForgetSet method
- SetByForgetSet method, MSFT_DtcTransactionTask class
- MSFT_DtcTransactionTask class, SetByForgetSet method
topic_type:
- apiref
api_name:
- MSFT_DtcTransactionTask.SetByForgetSet
api_location:
- MsDtcWmi.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetByForgetSet method of the MSFT\_DtcTransactionTask class

Indicates whether to forget the transaction.

## Syntax


```mof
uint32 SetByForgetSet(
  [in] string  DtcName,
  [in] string  TransactionId,
  [in] boolean Forget
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

*Forget* \[in\]
</dt> <dd>

**true** to forget the transaction; otherwise, **false**.

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

 

 





