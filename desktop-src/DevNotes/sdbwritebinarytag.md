---
description: Writes binary data to the specified database.
ms.assetid: 935321b8-904e-46be-ad11-77d89670a072
title: SdbWriteBinaryTag function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbWriteBinaryTag
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbWriteBinaryTag function

Writes binary data to the specified database.

## Syntax


```C++
BOOL WINAPI SdbWriteBinaryTag(
  _In_ PDB   pdb,
  _In_ TAG   tTag,
  _In_ PBYTE pBuffer,
  _In_ DWORD dwSize
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

*pBuffer* \[in\]
</dt> <dd>

The buffer that contains the data. This parameter cannot be **NULL**.

</dd> <dt>

*dwSize* \[in\]
</dt> <dd>

The size of the *pBuffer* buffer, in bytes.

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

[**SdbWriteBinaryTagFromFile**](sdbwritebinarytagfromfile.md)
</dt> <dt>

[**SdbWriteDWORDTag**](sdbwritedwordtag.md)
</dt> <dt>

[**SdbWriteQWORDTag**](sdbwriteqwordtag.md)
</dt> <dt>

[**SdbWriteStringTag**](sdbwritestringtag.md)
</dt> <dt>

[**SdbWriteWORDTag**](sdbwritewordtag.md)
</dt> </dl>

 

 




