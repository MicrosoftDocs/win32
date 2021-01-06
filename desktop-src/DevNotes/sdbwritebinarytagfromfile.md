---
description: Writes binary data from the specified file to the specified database.
ms.assetid: 960633a8-5cec-462b-b7dc-72eb3e4fd0a2
title: SdbWriteBinaryTagFromFile function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbWriteBinaryTagFromFile
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbWriteBinaryTagFromFile function

Writes binary data from the specified file to the specified database.

## Syntax


```C++
BOOL WINAPI SdbWriteBinaryTagFromFile(
  _In_ PDB     pdb,
  _In_ TAG     tTag,
  _In_ LPCWSTR pwszPath
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

The TAG for the entry. This TAG must be of type **TAG\_TYPE\_BINARY**.

</dd> <dt>

*pwszPath* \[in\]
</dt> <dd>

The path to the file that contains the data. This parameter cannot be **NULL**.

</dd> </dl>

## Return value

The function returns **TRUE** on success or **FALSE** on failure.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



## See also

<dl> <dt>

[**SdbWriteBinaryTag**](sdbwritebinarytag.md)
</dt> </dl>

 

 




