---
title: ADSI Simple Data Types (Iads.h)
description: Active Directory Service Interfaces (ADSI) defines and uses the following simple data types.
ms.assetid: 0bd34f13-269f-4f5d-8a18-74577522e402
ms.tgt_platform: multiple
keywords:
- ADS_BOOLEAN
- ADS_CASE_EXACT_STRING
- ADS_CASE_IGNORE_STRING
- ADS_DN_STRING
- ADS_INTEGER
- ADS_LARGE_INTEGER
- ADS_NUMERIC_STRING
- ADS_OBJECT_CLASS
- ADS_PRINTABLE_STRING
- ADS_SEARCH_HANDLE
- ADS_UTC_TIME
ms.topic: reference
ms.date: 05/31/2018
---

# ADSI Simple Data Types

Active Directory Service Interfaces (ADSI) defines and uses the following simple data types.


```C++
typedef DWORD ADS_BOOLEAN, *PADS_BOOLEAN;
typedef LPWSTR ADS_CASE_EXACT_STRING, *PADS_CASE_EXACT_STRING;
typedef LPWSTR ADS_CASE_IGNORE_STRING, *PADS_CASE_IGNORE_STRING;
typedef LPWSTR ADS_DN_STRING, *PADS_DN_STRING;
typedef DWORD ADS_INTEGER, *PADS_INTEGER;
typedef LARGE_INTEGER ADS_LARGE_INTEGER, *PADS_LARGE_INTEGER;
typedef LPWSTR ADS_NUMERIC_STRING, *PADS_NUMERIC_STRING;
typedef LPWSTR ADS_OBJECT_CLASS, *PADS_OBJECT_CLASS;
typedef LPWSTR ADS_PRINTABLE_STRING, *PADS_PRINTABLE_STRING;
typedef HANDLE ADS_SEARCH_HANDLE, *PADS_SEARCH_HANDLE;
typedef SYSTEMTIME ADS_UTC_TIME, *PADS_UTC_TIME;
```



<dl> <dt>

**ADS\_BOOLEAN**
</dt> <dd>

DWORD

</dd> <dt>

**ADS\_CASE\_EXACT\_STRING**
</dt> <dd>

LPWSTR

</dd> <dt>

**ADS\_CASE\_IGNORE\_STRING**
</dt> <dd>

LPWSTR

</dd> <dt>

**ADS\_DN\_STRING**
</dt> <dd>

LPWSTR

</dd> <dt>

**ADS\_INTEGER**
</dt> <dd>

DWORD

</dd> <dt>

**ADS\_LARGE\_INTEGER**
</dt> <dd>

[**LARGE\_INTEGER**](/windows/win32/api/winnt/ns-winnt-large_integer-r1)

</dd> <dt>

**ADS\_NUMERIC\_STRING**
</dt> <dd>

LPWSTR

</dd> <dt>

**ADS\_OBJECT\_CLASS**
</dt> <dd>

LPWSTR

</dd> <dt>

**ADS\_PRINTABLE\_STRING**
</dt> <dd>

LPWSTR

</dd> <dt>

**ADS\_SEARCH\_HANDLE**
</dt> <dd>

HANDLE

</dd> <dt>

**ADS\_UTC\_TIME**
</dt> <dd>

[**SYSTEMTIME**](/windows/desktop/api/minwinbase/ns-minwinbase-systemtime)

</dd> </dl>

## Remarks

When ADSI reads an attribute that has been defined as an **INTEGER** in the LDAP schema, it will always handle the integer as a 32-bit value and may truncate the data. This is only a concern for LDAP servers that allow arbitrary sized integer values. If the attribute is a custom attribute defined by extending the schema, this problem can be avoided by defining the custom attribute as a string.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                    |
| Header<br/>                   | <dl> <dt>Iads.h</dt> </dl> |



 

