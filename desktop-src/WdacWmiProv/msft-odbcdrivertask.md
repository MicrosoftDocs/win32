---
title: MSFT\_OdbcDriverTask class
description: Task provider for ODBC driver.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1347a239-abc8-4a67-b930-46fb110caf2f
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_OdbcDriverTask class
- MSFT_OdbcDriverTask class, described
topic_type:
- apiref
api_name:
- MSFT_OdbcDriverTask
api_location:
- WdacWmiProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_OdbcDriverTask class

Task provider for ODBC driver.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("WdacWmiProv"), ClassVersion("1.0"), AMENDMENT]
class MSFT_OdbcDriverTask
{
};
```

## Members

The **MSFT\_OdbcDriverTask** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_OdbcDriverTask** class has these methods.



| Method                                                           | Description                                                                          |
|:-----------------------------------------------------------------|:-------------------------------------------------------------------------------------|
| [**Get**](get-msft-odbcdrivertask.md)                           | Retrieves one or more installed ODBC drivers from the system.<br/>             |
| [**SetByInputObject**](setbyinputobject-msft-odbcdrivertask.md) | Configure driver\\\\'s properties for one or more installed ODBC drivers.<br/> |
| [**SetByName**](setbyname-msft-odbcdrivertask.md)               | Configure driver\\\\'s properties for one or more installed ODBC drivers.<br/> |



 

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                             |
| Namespace<br/>                | Root\\Microsoft\\Windows\\WDAC<br/>                                                  |
| MOF<br/>                      | <dl> <dt>WdacWmiProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WdacWmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[WDAC WMI Provider Reference](wdac-wmi-provider-reference.md)
</dt> </dl>

 

 





