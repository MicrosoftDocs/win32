---
title: MSFT\_OdbcDsnTask class
description: Task provider for ODBC Data Source Name (DSN).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ec0e7030-fafa-40fd-adbc-e0cc22a6c4ac
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_OdbcDsnTask class
- MSFT_OdbcDsnTask class, described
topic_type:
- apiref
api_name:
- MSFT_OdbcDsnTask
api_location:
- WdacWmiProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_OdbcDsnTask class

Task provider for ODBC Data Source Name (DSN).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("WdacWmiProv"), ClassVersion("1.0"), AMENDMENT]
class MSFT_OdbcDsnTask
{
};
```

## Members

The **MSFT\_OdbcDsnTask** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_OdbcDsnTask** class has these methods.



| Method                                                          | Description                                                   |
|:----------------------------------------------------------------|:--------------------------------------------------------------|
| [**Add**](add-msft-odbcdsntask.md)                             | Adds an ODBC DSN.<br/>                                  |
| [**Get**](get-msft-odbcdsntask.md)                             | Retrieves one or more ODBC DSNs from the system.<br/>   |
| [**RemoveByDsnObject**](removebydsnobject-msft-odbcdsntask.md) | Removes one or more existing DSNs from the system.<br/> |
| [**RemoveByName**](removebyname-msft-odbcdsntask.md)           | Removes one or more existing DSNs from the system.<br/> |
| [**SetByInputObject**](setbyinputobject-msft-odbcdsntask.md)   | Modifies one or more ODBC DSNs.<br/>                    |
| [**SetByName**](setbyname-msft-odbcdsntask.md)                 | Modifies one or more ODBC DSNs.<br/>                    |



 

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

 

 





