---
title: MSFT\_OdbcPerfCounterTask class
description: Task provider for ODBC Connection Pooling PerfMon counters setting.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8763b1c7-6e73-474f-853e-b66ae56db069
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_OdbcPerfCounterTask class
- MSFT_OdbcPerfCounterTask class, described
topic_type:
- apiref
api_name:
- MSFT_OdbcPerfCounterTask
api_location:
- WdacWmiProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_OdbcPerfCounterTask class

Task provider for ODBC Connection Pooling PerfMon counters setting.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("WdacWmiProv"), ClassVersion("1.0"), AMENDMENT]
class MSFT_OdbcPerfCounterTask
{
};
```

## Members

The **MSFT\_OdbcPerfCounterTask** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_OdbcPerfCounterTask** class has these methods.



| Method                                                                        | Description                                                                                                          |
|:------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------|
| [**DisableByInputObject**](disablebyinputobject-msft-odbcperfcountertask.md) | Disables the ODBC Connection Pooling PerfMon counters for ODBC Connection Pooling feature.<br/>                |
| [**DisableByPlatform**](disablebyplatform-msft-odbcperfcountertask.md)       | Disables the ODBC Connection Pooling PerfMon counters for ODBC Connection Pooling feature.<br/>                |
| [**EnableByInputObject**](enablebyinputobject-msft-odbcperfcountertask.md)   | Enables the ODBC Connection Pooling PerfMon counters for troubleshooting ODBC Connection Pooling feature.<br/> |
| [**EnableByPlatform**](enablebyplatform-msft-odbcperfcountertask.md)         | Enables the ODBC Connection Pooling PerfMon counters for troubleshooting ODBC Connection Pooling feature.<br/> |
| [**Get**](get-msft-odbcperfcountertask.md)                                   | Retrieves the ODBC Connection Pooling PerfMon counters for ODBC Connection Pooling feature.<br/>               |



 

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

 

 





