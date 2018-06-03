---
title: MSFT\_DtcTransactionsStatisticsTask class
description: Retrieves a summary of transactions.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 84ceb6b2-de25-490c-9025-6f5ec893f0de
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DtcTransactionsStatisticsTask class
- MSFT_DtcTransactionsStatisticsTask class, described
topic_type:
- apiref
api_name:
- MSFT_DtcTransactionsStatisticsTask
api_location:
- MsDtcWmi.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_DtcTransactionsStatisticsTask class

Retrieves a summary of transactions.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MsDtcWmi"), Version("1.0"), AMENDMENT]
class MSFT_DtcTransactionsStatisticsTask
{
};
```

## Members

The **MSFT\_DtcTransactionsStatisticsTask** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_DtcTransactionsStatisticsTask** class has these methods.



| Method                                                | Description                                                           |
|:------------------------------------------------------|:----------------------------------------------------------------------|
| [**Get**](get-msft-dtctransactionsstatisticstask.md) | Retrieves a summary of transactions run by a DTC instance.<br/> |



 

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

[Distributed Transaction Coordinator WMI Provider](distributed-transaction-coordinator-wmi-provider-portal.md)
</dt> </dl>

 

 





