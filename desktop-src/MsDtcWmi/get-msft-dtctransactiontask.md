---
title: Get method of the MSFT\_DtcTransactionTask class
description: Retrieves information about the transactions for a DTC instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c19509b0-46af-4f11-b813-39bb813860de
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, MSFT_DtcTransactionTask class
- MSFT_DtcTransactionTask class, Get method
topic_type:
- apiref
api_name:
- MSFT_DtcTransactionTask.Get
api_location:
- MsDtcWmi.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the MSFT\_DtcTransactionTask class

Retrieves information about the transactions for a DTC instance.

## Syntax


```mof
uint32 Get(
  [in]  string             DtcName,
  [out] DtcTransactionInfo cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*DtcName* \[in\]
</dt> <dd>

The name of the DTC instance. If you do not specify this parameter, or if you specify a value of "Local", this method gets the information for transactions handled by the local DTC instance.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An array of [**DtcTransactionInfo**](dtctransactioninfo.md) embedded instances representing the specified transaction information.

</dd> </dl>

## Return value

Returns "0" on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\MsDTC<br/>                                                                  |
| Header<br/>                   | <dl> <dt>Wbemcli.h</dt> </dl>    |
| MOF<br/>                      | <dl> <dt>Msdtcwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsDtcWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DtcTransactionTask**](msft-dtctransactiontask.md)
</dt> </dl>

 

 





