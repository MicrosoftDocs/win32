---
description: Searches for a TAG match within the specified parent and returns the TAGID of the first match.
ms.assetid: ecbe216c-1e46-4472-b1d1-e2ac7ace82ab
title: SdbFindFirstTag function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbFindFirstTag
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbFindFirstTag function

Searches for a TAG match within the specified parent and returns the **TAGID** of the first match.

## Syntax


```C++
TAGID WINAPI SdbFindFirstTag(
  _In_ PDB   pdb,
  _In_ TAGID tiParent,
  _In_ TAG   tTag
);
```



## Parameters

<dl> <dt>

*pdb* \[in\]
</dt> <dd>

A handle to the shim database.

</dd> <dt>

*tiParent* \[in\]
</dt> <dd>

The **TAGID** of the search start. This parameter can be **TAGID\_ROOT** or **TAG\_TYPE\_LIST**.

</dd> <dt>

*tTag* \[in\]
</dt> <dd>

The TAG to be matched. See [TAG](tag.md) for a list of possible values.

</dd> </dl>

## Return value

The **TAGID** of the first match.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



## See also

<dl> <dt>

[**SdbFindNextTag**](sdbfindnexttag.md)
</dt> <dt>

[**SdbTagRefToTagID**](sdbtagreftotagid.md)
</dt> </dl>

 

 




