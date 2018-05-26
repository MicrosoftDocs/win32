---
title: MSFT\_DtcLogTask class
description: Manages DTC log file settings for a DTC instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 824f10c1-4677-498d-b9c8-42440e15d1a4
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DtcLogTask class
- MSFT_DtcLogTask class, described
topic_type:
- apiref
api_name:
- MSFT_DtcLogTask
api_location:
- MsDtcWmi.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_DtcLogTask class

Manages DTC log file settings for a DTC instance.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MsDtcWmi"), Version("1.0"), AMENDMENT]
class MSFT_DtcLogTask
{
};
```

## Members

The **MSFT\_DtcLogTask** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_DtcLogTask** class has these methods.



| Method                                 | Description                                                    |
|:---------------------------------------|:---------------------------------------------------------------|
| [**Get**](get-msft-dtclogtask.md)     | Retrieves DTC log file settings for a DTC instance.<br/> |
| [**Reset**](reset-msft-dtclogtask.md) | Resets the log file of a DTC instance.<br/>              |
| [**Set**](set-msft-dtclogtask.md)     | Modifies DTC log file settings for a DTC instance.<br/>  |



 

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

 

 





