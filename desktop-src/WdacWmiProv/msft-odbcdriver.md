---
title: MSFT\_OdbcDriver class
description: ODBC Driver Instance Provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '16d7d505-d21d-495e-8b91-3c11806c3352'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_OdbcDriver class", "MSFT_OdbcDriver class, described"]
topic_type:
- apiref
api_name:
- MSFT_OdbcDriver
- MSFT_OdbcDriver.Name
- MSFT_OdbcDriver.Platform
- MSFT_OdbcDriver.KeyValuePair
api_location:
- WdacWmiProv.dll
api_type:
- DllExport
---

# MSFT\_OdbcDriver class

ODBC Driver Instance Provider.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("1.0"), AMENDMENT]
class MSFT_OdbcDriver
{
  string                Name;
  string                Platform;
  MSFT_OdbcKeyValuePair KeyValuePair[];
};
```

## Members

The **MSFT\_OdbcDriver** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_OdbcDriver** class has these properties.

<dl> <dt>

**KeyValuePair**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_OdbcKeyValuePair** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_OdbcKeyValuePair**](msft-odbckeyvaluepair.md)")
</dt> </dl>

An array of [**MSFT\_OdbcKeyValuePair**](msft-odbckeyvaluepair.md) classes that represent the key-value pairs of the ODBC driver.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (255)
</dt> </dl>

Name of an ODBC driver.

</dd> <dt>

**Platform**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Either '32-bit' or '64-bit'.

</dd> </dl>

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                             |
| Namespace<br/>                | Root\\Microsoft\\Windows\\WDAC<br/>                                                  |
| MOF<br/>                      | <dl> <dt>WdacWmiProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WdacWmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[WDAC WMI Provider Reference](wdac-wmi-provider-reference.md)
</dt> <dt>

[**MSFT\_OdbcKeyValuePair**](msft-odbckeyvaluepair.md)
</dt> </dl>

 

 





