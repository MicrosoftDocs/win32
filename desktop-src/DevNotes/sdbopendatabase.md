---
description: Opens the specified shim database.
ms.assetid: 148181d7-a20a-467c-984b-e32013960783
title: SdbOpenDatabase function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbOpenDatabase
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbOpenDatabase function

Opens the specified shim database.

## Syntax


```C++
PDB WINAPI SdbOpenDatabase(
  _In_ LPCTSTR   pwszPath,
  _In_ PATH_TYPE eType
);
```



## Parameters

<dl> <dt>

*pwszPath* \[in\]
</dt> <dd>

The database path. This parameter cannot be **NULL**.

</dd> <dt>

*eType* \[in\]
</dt> <dd>

The path type. See [**PATH\_TYPE**](path-type.md) for a list of values.

</dd> </dl>

## Return value

The function returns a handle to the shim database.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



## See also

<dl> <dt>

[**SdbCreateDatabase**](sdbcreatedatabase.md)
</dt> </dl>

 

 




