---
title: MSFT\_OdbcKeyValuePair class
description: Key-value pair for ODBC CIM providers.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '29c406da-5470-4107-a2fd-c1d4ea29d3af'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_OdbcKeyValuePair class", "MSFT_OdbcKeyValuePair class, described"]
topic_type:
- apiref
api_name:
- MSFT_OdbcKeyValuePair
- MSFT_OdbcKeyValuePair.ParentKey
- MSFT_OdbcKeyValuePair.key
- MSFT_OdbcKeyValuePair.Value
api_location:
- WdacWmiProv.dll
api_type:
- DllExport
---

# MSFT\_OdbcKeyValuePair class

Key-value pair for ODBC CIM providers.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("1.0"), AMENDMENT]
class MSFT_OdbcKeyValuePair
{
  string ParentKey;
  string key;
  string Value;
};
```

## Members

The **MSFT\_OdbcKeyValuePair** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_OdbcKeyValuePair** class has these properties.

<dl> <dt>

**key**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (512)
</dt> </dl>

</dd> <dt>

**ParentKey**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (512)
</dt> </dl>

</dd> <dt>

**Value**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (512)
</dt> </dl>

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
</dt> </dl>

 

 





