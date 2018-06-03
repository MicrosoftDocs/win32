---
title: MSFT\_DtcTransactionTask class
description: Modifies and retrieves the state of DTC transactions.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5b3909ae-046f-4e42-8e0a-f0d33e4283e8
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DtcTransactionTask class
- MSFT_DtcTransactionTask class, described
topic_type:
- apiref
api_name:
- MSFT_DtcTransactionTask
api_location:
- MsDtcWmi.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_DtcTransactionTask class

Modifies and retrieves the state of DTC transactions.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MsDtcWmi"), Version("1.0"), AMENDMENT]
class MSFT_DtcTransactionTask
{
};
```

## Members

The **MSFT\_DtcTransactionTask** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_DtcTransactionTask** class has these methods.



| Method                                                           | Description                                                                 |
|:-----------------------------------------------------------------|:----------------------------------------------------------------------------|
| [**Get**](get-msft-dtctransactiontask.md)                       | Retrieves information about the transactions for a DTC instance.<br/> |
| [**SetByAbortSet**](setbyabortset-msft-dtctransactiontask.md)   | Indicates whether to abort the transaction.<br/>                      |
| [**SetByCommitSet**](setbycommitset-msft-dtctransactiontask.md) | Indicates whether to commit the transaction.<br/>                     |
| [**SetByForgetSet**](setbyforgetset-msft-dtctransactiontask.md) | Indicates whether to forget the transaction.<br/>                     |
| [**SetByTraceSet**](setbytraceset-msft-dtctransactiontask.md)   | Indicates whether to trace the transaction.<br/>                      |



 

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

 

 





