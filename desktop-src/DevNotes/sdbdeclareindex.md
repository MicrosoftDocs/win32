---
description: Declares a new index in the specified database.
ms.assetid: 21a09201-8f84-4263-b258-77716826a3cd
title: SdbDeclareIndex function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbDeclareIndex
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbDeclareIndex function

Declares a new index in the specified database.

## Syntax


```C++
BOOL WINAPI SdbDeclareIndex(
  _In_  PDB     pdb,
  _In_  TAG     tWhich,
  _In_  TAG     tKey,
  _In_  DWORD   dwEntries,
  _In_  BOOL    bUniqueKey,
  _Out_ INDEXID *piiIndex
);
```



## Parameters

<dl> <dt>

*pdb* \[in\]
</dt> <dd>

A handle to the shim database.

</dd> <dt>

*tWhich* \[in\]
</dt> <dd>

This parameter must be **TAG\_TYPE\_LIST**.

</dd> <dt>

*tKey* \[in\]
</dt> <dd>

The TAG that specifies the type to be used as the key. This parameter cannot be **TAG\_TYPE\_LIST**.

</dd> <dt>

*dwEntries* \[in\]
</dt> <dd>

The number of entries to allocate in the index.

</dd> <dt>

*bUniqueKey* \[in\]
</dt> <dd>

If this parameter is **TRUE**, the index is a unique-key index.

</dd> <dt>

*piiIndex* \[out\]
</dt> <dd>

The resulting **INDEXID** of the newly declared index.

</dd> </dl>

## Return value

The function returns **TRUE** on success or **FALSE** on failure.

## Remarks

Call this function before writing tags to the new index.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



## See also

<dl> <dt>

[**INDEXID**](indexid.md)
</dt> <dt>

[**SdbCommitIndexes**](sdbcommitindexes.md)
</dt> <dt>

[**SdbStartIndexing**](sdbstartindexing.md)
</dt> <dt>

[**SdbStopIndexing**](sdbstopindexing.md)
</dt> </dl>

 

 




