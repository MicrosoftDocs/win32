---
title: MSFT\_DtcTransactionsTraceSettingTask class
description: Gets the DTC transactions trace setting of the host.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7cd9c48d-8c21-4bf2-81bc-5073b4e3fdc9
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DtcTransactionsTraceSettingTask class
- MSFT_DtcTransactionsTraceSettingTask class, described
topic_type:
- apiref
api_name:
- MSFT_DtcTransactionsTraceSettingTask
api_location:
- MsDtcWmi.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_DtcTransactionsTraceSettingTask class

Gets the DTC transactions trace setting of the host.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MsDtcWmi"), Version("1.0"), AMENDMENT]
class MSFT_DtcTransactionsTraceSettingTask
{
};
```

## Members

The **MSFT\_DtcTransactionsTraceSettingTask** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_DtcTransactionsTraceSettingTask** class has these methods.



| Method                                                                                                        | Description                                                         |
|:--------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------|
| [**Get**](get-msft-dtctransactionstracesettingtask.md)                                                       | Gets the DTC transactions trace setting of the host.<br/>     |
| [**SetByTraceAllParameterSet**](setbytraceallparameterset-msft-dtctransactionstracesettingtask.md)           | Modifies the DTC transactions trace setting of the host.<br/> |
| [**SetByTraceSelectedParameterSet**](setbytraceselectedparameterset-msft-dtctransactionstracesettingtask.md) | Modifies the DTC transactions trace setting of the host.<br/> |



 

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

 

 





