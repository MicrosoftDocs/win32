---
description: Finds the first DWORD record in the specified index that meets the specified criteria.
ms.assetid: 81302f84-497d-4fef-b348-eee2a53284c7
title: SdbFindFirstDWORDIndexedTag function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbFindFirstDWORDIndexedTag
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbFindFirstDWORDIndexedTag function

Finds the first **DWORD** record in the specified index that meets the specified criteria.

## Syntax


```C++
TAGID WINAPI SdbFindFirstDWORDIndexedTag(
  _In_  PDB       pdb,
  _In_  TAG       tWhich,
  _In_  TAG       tKey,
  _In_  DWORD     dwName,
  _Out_ FIND_INFO *pFindInfo
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

The index type. See [**TAG**](tag.md) for a list of values.

</dd> <dt>

*tKey* \[in\]
</dt> <dd>

The key type.

</dd> <dt>

*dwName* \[in\]
</dt> <dd>

The name of the data to be found. This value will be converted into a key.

</dd> <dt>

*pFindInfo* \[out\]
</dt> <dd>

A [**FIND\_INFO**](find-info.md) structure that receives the record.

</dd> </dl>

## Return value

The **TAGID** of the first match or **TAG\_NULL** if no match is found.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



## See also

<dl> <dt>

[**SdbFindFirstTag**](sdbfindfirsttag.md)
</dt> </dl>

 

 




