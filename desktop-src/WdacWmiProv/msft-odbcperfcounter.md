---
title: MSFT\_OdbcPerfCounter class
description: ODBC PerfMon Counters Configuration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 34733618-5f7f-4eb2-b927-4f87a64cd270
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_OdbcPerfCounter class
- MSFT_OdbcPerfCounter class, described
topic_type:
- apiref
api_name:
- MSFT_OdbcPerfCounter
- MSFT_OdbcPerfCounter.Platform
- MSFT_OdbcPerfCounter.IsEnabled
api_location:
- WdacWmiProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_OdbcPerfCounter class

ODBC PerfMon Counters Configuration.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("1.0"), AMENDMENT]
class MSFT_OdbcPerfCounter
{
  string  Platform;
  boolean IsEnabled;
};
```

## Members

The **MSFT\_OdbcPerfCounter** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_OdbcPerfCounter** class has these properties.

<dl> <dt>

**IsEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the ODBC connection pooling PerfMon counters is enabled.

</dd> <dt>

**Platform**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The platform architecture of the ODBC Connection Pooling PerfMon counters. Either '32-bit' or '64-bit'.

</dd> </dl>

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

 

 





