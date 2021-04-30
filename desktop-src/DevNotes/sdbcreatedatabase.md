---
description: Creates a new shim database.
ms.assetid: 91fb180d-1a21-4011-821d-ea0fc999dc76
title: SdbCreateDatabase function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbCreateDatabase
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbCreateDatabase function

Creates a new shim database.

## Syntax


```C++
PDB WINAPI SdbCreateDatabase(
  _In_ LPCWSTR   pwszPath,
  _In_ PATH_TYPE eType
);
```



## Parameters

<dl> <dt>

*pwszPath* \[in\]
</dt> <dd>

The path where the database should be saved. This parameter cannot be **NULL**.

</dd> <dt>

*eType* \[in\]
</dt> <dd>

The path type. See [**PATH\_TYPE**](path-type.md) for a list of values.

</dd> </dl>

## Return value

The function returns a handle to the shim database or **NULL** on failure.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



## See also

<dl> <dt>

[**SdbOpenDatabase**](sdbopendatabase.md)
</dt> </dl>

 

 




