---
title: MSFT\_DtcDefaultTask class
description: Retrieves and updates the default DTC instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '03e16032-705a-4056-9bbd-e00518cb39d2'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-transaction-coordinator'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_DtcDefaultTask class", "MSFT_DtcDefaultTask class, described"]
topic_type:
- apiref
api_name:
- MSFT_DtcDefaultTask
api_location:
- MsDtcWmi.dll
api_type:
- DllExport
---

# MSFT\_DtcDefaultTask class

Retrieves and updates the default DTC instance.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MsDtcWmi"), Version("1.0"), AMENDMENT]
class MSFT_DtcDefaultTask
{
};
```

## Members

The **MSFT\_DtcDefaultTask** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_DtcDefaultTask** class has these methods.



| Method                                 | Description                                    |
|:---------------------------------------|:-----------------------------------------------|
| [**Get**](get-msft-dtcdefaulttask.md) | Retrieves the default DTC instance.<br/> |
| [**Set**](set-msft-dtcdefaulttask.md) | Sets the default DTC instance.<br/>      |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\MsDTC<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Msdtcwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsDtcWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[Distributed Transaction Coordinator WMI Provider](distributed-transaction-coordinator-wmi-provider-portal.md)
</dt> </dl>

 

 





