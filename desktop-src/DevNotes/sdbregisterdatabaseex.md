---
description: Registers the specified database.
ms.assetid: 65eceb1a-9ce1-4b97-98d7-731932797794
title: SdbRegisterDatabaseEx function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbRegisterDatabaseEx
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbRegisterDatabaseEx function

Registers the specified database.

## Syntax


```C++
BOOL WINAPI SdbRegisterDatabaseEx(
  _In_     LPCTSTR    pszDatabasePath,
  _In_     DWORD      dwDatabaseType,
  _In_opt_ PULONGLONG pTimeStamp
);
```



## Parameters

<dl> <dt>

*pszDatabasePath* \[in\]
</dt> <dd>

The database path. This parameter cannot be **NULL**.

</dd> <dt>

*dwDatabaseType* \[in\]
</dt> <dd>

The database type. See [Shim Database Types](shim-database-types.md) for a list of values.

</dd> <dt>

*pTimeStamp* \[in, optional\]
</dt> <dd>

The time stamp for the database. If this parameter is **NULL**, the system time is used.

</dd> </dl>

## Return value

The function returns **TRUE** on success or **FALSE** on failure.

## Remarks

A database must be registered before you can use any other SDB functions.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



## See also

<dl> <dt>

[**SdbUnregisterDatabase**](sdbunregisterdatabase.md)
</dt> </dl>

 

 




