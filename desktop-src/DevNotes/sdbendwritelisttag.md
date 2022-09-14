---
description: Ends the write operations for the specified list.
ms.assetid: 318aa5dc-b562-47f8-8cd6-daa97f28c0f0
title: SdbEndWriteListTag function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbEndWriteListTag
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbEndWriteListTag function

Ends the write operations for the specified list.

## Syntax


```C++
BOOL WINAPI SdbEndWriteListTag(
  _Inout_ PDB   pdb,
  _In_    TAGID tiList
);
```



## Parameters

<dl> <dt>

*pdb* \[in, out\]
</dt> <dd>

A handle to the shim database.

</dd> <dt>

*tiList* \[in\]
</dt> <dd>

The [**TAGID**](tagid.md) of the list

</dd> </dl>

## Return value

The function returns **TRUE** on success or **FALSE** on failure.

## Remarks

Call this function after writing all list entries; it will mark the end of the list.

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

[**SdbCloseDatabaseWrite**](sdbclosedatabasewrite.md)
</dt> </dl>

 

 




