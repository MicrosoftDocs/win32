---
title: Get method of the MSFT\_DtcTransactionsStatisticsTask class
description: Retrieves a summary of transactions run by a DTC instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1681e546-b35b-4aa7-bac9-62cade15c797
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, MSFT_DtcTransactionsStatisticsTask class
- MSFT_DtcTransactionsStatisticsTask class, Get method
topic_type:
- apiref
api_name:
- MSFT_DtcTransactionsStatisticsTask.Get
api_location:
- MsDtcWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the MSFT\_DtcTransactionsStatisticsTask class

Retrieves a summary of transactions run by a DTC instance.

## Syntax


```mof
uint32 Get(
  [in]  string                    DtcName,
  [out] DtcTransactionsStatistics cmdletOutput
);
```



## Parameters

<dl> <dt>

*DtcName* \[in\]
</dt> <dd>

The name of the DTC instance. This method gets the summary of transactions for this DTC instance. If you do not specify this parameter, or if you specify a value of "Local", this method displays the summary of transactions handled by the local DTC instance.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

A [**DtcTransactionsStatistics**](dtctransactionsstatistics.md) embedded instance containing the summary.

</dd> </dl>

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

[**MSFT\_DtcTransactionsStatisticsTask**](msft-dtctransactionsstatisticstask.md)
</dt> </dl>

 

 





