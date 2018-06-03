---
title: MSFT\_DtcTask class
description: Manages DTC instances.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5c0f43a3-5b09-453d-89c0-657a286fbfb5
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DtcTask class
- MSFT_DtcTask class, described
topic_type:
- apiref
api_name:
- MSFT_DtcTask
api_location:
- MsDtcWmi.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_DtcTask class

Manages DTC instances.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MsDtcWmi"), Version("1.0"), AMENDMENT]
class MSFT_DtcTask
{
};
```

## Members

The **MSFT\_DtcTask** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_DtcTask** class has these methods.



| Method                                      | Description                                               |
|:--------------------------------------------|:----------------------------------------------------------|
| [**Get**](get-msft-dtctask.md)             | Retrieves a DTC instance.<br/>                      |
| [**Install**](install-msft-dtctask.md)     | Installs the local transactions coordinator.<br/>   |
| [**Start**](start-msft-dtctask.md)         | Starts the DTC instance.<br/>                       |
| [**Stop**](stop-msft-dtctask.md)           | Stops a DTC instance.<br/>                          |
| [**Uninstall**](uninstall-msft-dtctask.md) | Uninstalls the local transactions coordinator.<br/> |



 

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

 

 





