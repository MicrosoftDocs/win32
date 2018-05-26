---
title: MSFT\_DtcTransactionsTraceSessionTask class
description: Modifies and retrieves the DTC transactions trace setting of the host.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ef5ad5a8-5021-42a3-b141-288dec7b7ee6
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DtcTransactionsTraceSessionTask class
- MSFT_DtcTransactionsTraceSessionTask class, described
topic_type:
- apiref
api_name:
- MSFT_DtcTransactionsTraceSessionTask
api_location:
- MsDtcWmi.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_DtcTransactionsTraceSessionTask class

Modifies and retrieves the DTC transactions trace setting of the host.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MsDtcWmi"), Version("1.0"), AMENDMENT]
class MSFT_DtcTransactionsTraceSessionTask
{
};
```

## Members

The **MSFT\_DtcTransactionsTraceSessionTask** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_DtcTransactionsTraceSessionTask** class has these methods.



| Method                                                      | Description                                                                                 |
|:------------------------------------------------------------|:--------------------------------------------------------------------------------------------|
| [**Get**](get-msft-dtctransactionstracesessiontask.md)     | Retrieves the DTC transactions trace session specific setting of the host.<br/>       |
| [**Set**](set-msft-dtctransactionstracesessiontask.md)     | Modifies the DTC transactions trace setting of the host.<br/>                         |
| [**Start**](start-msft-dtctransactionstracesessiontask.md) | Starts a new DTC transactions trace session for the host.<br/>                        |
| [**Stop**](stop-msft-dtctransactionstracesessiontask.md)   | Stops the active DTC transactions trace session on the host.<br/>                     |
| [**Write**](write-msft-dtctransactionstracesessiontask.md) | Writes the data from an active DTC transactions trace session into the log file.<br/> |



 

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

 

 





