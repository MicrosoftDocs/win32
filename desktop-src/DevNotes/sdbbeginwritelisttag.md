---
description: Creates a new list TAG for write operations.
ms.assetid: 3a52e2f2-9648-45fb-b487-ccfe5ed24f7f
title: SdbBeginWriteListTag function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbBeginWriteListTag
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbBeginWriteListTag function

Creates a new list TAG for write operations.

## Syntax


```C++
TAGID WINAPI SdbBeginWriteListTag(
  _In_ PDB pdb,
  _In_ TAG tTag
);
```



## Parameters

<dl> <dt>

*pdb* \[in\]
</dt> <dd>

A handle to the shim database.

</dd> <dt>

*tTag* \[in\]
</dt> <dd>

The TAG for the new entry. This value must be of type **TAG\_TYPE\_LIST**.

</dd> </dl>

## Return value

The function returns the [**TAGID**](tagid.md) of the new list on success or **TAGID\_NULL** on failure.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



## See also

<dl> <dt>

[**SdbCloseDatabase**](sdbclosedatabase.md)
</dt> <dt>

[**SdbCloseDatabaseWrite**](sdbclosedatabasewrite.md)
</dt> <dt>

[**SdbEndWriteListTag**](sdbendwritelisttag.md)
</dt> <dt>

[**TAG**](tag.md)
</dt> <dt>

[TAG Types](tag-types.md)
</dt> <dt>

[**TAGID**](tagid.md)
</dt> </dl>

 

 




