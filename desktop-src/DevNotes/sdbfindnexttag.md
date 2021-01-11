---
description: Searches for the next TAG match within the specified parent and returns the TAGID of the match.
ms.assetid: c96aa1c1-b0e6-49f5-9f74-7d0e050bee3b
title: SdbFindNextTag function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbFindNextTag
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbFindNextTag function

Searches for the next TAG match within the specified parent and returns the **TAGID** of the match.

## Syntax


```C++
TAGID WINAPI SdbFindNextTag(
  _In_ PDB   pdb,
  _In_ TAGID tiParent,
  _In_ TAGID tiPrev
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

*tiPrev* \[in\]
</dt> <dd>

The **TAGID** of the previous match.

</dd> </dl>

## Return value

The **TAGID** of the match.

## Remarks

Before calling this function, call the [**SdbFindFirstTag**](sdbfindfirsttag.md) function.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



## See also

<dl> <dt>

[**SdbFindFirstTag**](sdbfindfirsttag.md)
</dt> <dt>

[**SdbTagRefToTagID**](sdbtagreftotagid.md)
</dt> </dl>

 

 




