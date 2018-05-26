---
title: Get method of the MSFT\_DtcTransactionsTraceSettingTask class
description: Gets the DTC transactions trace setting of the host.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8cf5c632-1bdf-4bab-acdb-7b32c8a9e4de
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, MSFT_DtcTransactionsTraceSettingTask class
- MSFT_DtcTransactionsTraceSettingTask class, Get method
topic_type:
- apiref
api_name:
- MSFT_DtcTransactionsTraceSettingTask.Get
api_location:
- MsDtcWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the MSFT\_DtcTransactionsTraceSettingTask class

Gets the DTC transactions trace setting of the host.

## Syntax


```mof
uint32 Get(
  [out] DtcTransactionsTraceSettings cmdletOutput
);
```



## Parameters

<dl> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The object that contains the retrieved trace setting.

A [**DtcTransactionsTraceSettings**](dtctransactionstracesettings.md) embedded instance containing the specified trace settings.

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

[**MSFT\_DtcTransactionsTraceSettingTask**](msft-dtctransactionstracesettingtask.md)
</dt> </dl>

 

 





