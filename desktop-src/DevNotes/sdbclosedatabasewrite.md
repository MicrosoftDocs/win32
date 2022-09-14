---
description: Closes the specified database.
ms.assetid: 69546f03-9912-401a-9c1a-b7fdbe16dbf8
title: SdbCloseDatabaseWrite function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbCloseDatabaseWrite
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbCloseDatabaseWrite function

Closes the specified database.

## Syntax


```C++
void WINAPI SdbCloseDatabaseWrite(
  _Inout_ PDB pdb
);
```



## Parameters

<dl> <dt>

*pdb* \[in, out\]
</dt> <dd>

A handle to the shim database.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

This function calls [**SdbCloseDatabase**](sdbclosedatabase.md); therefore, these two functions are equivalent.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



## See also

<dl> <dt>

[**SdbBeginWriteListTag**](sdbbeginwritelisttag.md)
</dt> <dt>

[**SdbCloseDatabase**](sdbclosedatabase.md)
</dt> <dt>

[**SdbEndWriteListTag**](sdbendwritelisttag.md)
</dt> </dl>

 

 




