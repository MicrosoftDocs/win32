---
title: MSFT\_DtcClusterDefaultTask class
description: Manages tasks for the cluster DTC .
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9b1f007b-daca-44a8-a495-327062287b09
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DtcClusterDefaultTask class
- MSFT_DtcClusterDefaultTask class, described
topic_type:
- apiref
api_name:
- MSFT_DtcClusterDefaultTask
api_location:
- MsDtcWmi.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_DtcClusterDefaultTask class

Manages tasks for the cluster DTC .

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MsDtcWmi"), Version("1.0"), AMENDMENT]
class MSFT_DtcClusterDefaultTask
{
};
```

## Members

The **MSFT\_DtcClusterDefaultTask** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_DtcClusterDefaultTask** class has these methods.



| Method                                        | Description                           |
|:----------------------------------------------|:--------------------------------------|
| [**Get**](get-msft-dtcclusterdefaulttask.md) | Retrieves the cluster DTC.<br/> |
| [**Set**](set-msft-dtcclusterdefaulttask.md) | Updates the cluster DTC.<br/>   |



 

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

 

 





