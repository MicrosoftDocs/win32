---
title: MSFT\_OdbcDsn class
description: ODBC DSN Instance Provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'efea10f1-20a6-44fa-a741-4d231f2898cc'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_OdbcDsn class", "MSFT_OdbcDsn class, described"]
topic_type:
- apiref
api_name:
- MSFT_OdbcDsn
- MSFT_OdbcDsn.Name
- MSFT_OdbcDsn.DsnType
- MSFT_OdbcDsn.Platform
- MSFT_OdbcDsn.DriverName
- MSFT_OdbcDsn.KeyValuePair
api_location:
- WdacWmiProv.dll
api_type:
- DllExport
---

# MSFT\_OdbcDsn class

ODBC DSN Instance Provider.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("1.0"), AMENDMENT]
class MSFT_OdbcDsn
{
  string                Name;
  string                DsnType;
  string                Platform;
  string                DriverName;
  MSFT_OdbcKeyValuePair KeyValuePair[];
};
```

## Members

The **MSFT\_OdbcDsn** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_OdbcDsn** class has these properties.

<dl> <dt>

**DriverName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (255)
</dt> </dl>

The name of the ODBC driver for this DSN.

</dd> <dt>

**DsnType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Either 'User' or 'System'.

</dd> <dt>

**KeyValuePair**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_OdbcKeyValuePair** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_OdbcKeyValuePair**](msft-odbckeyvaluepair.md)")
</dt> </dl>

An array of [**MSFT\_OdbcKeyValuePair**](msft-odbckeyvaluepair.md) classes that represent the key-value pairs of the ODBC DSN.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (32)
</dt> </dl>

Name of an ODBC DSN.

</dd> <dt>

**Platform**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

One of '32-bit', '64-bit', '32/64-bit' or 'Unknown Platform'.

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

 

 





