---
description: Searches for the next child TAG within the specified parent and returns the TAGID of the next child.
ms.assetid: c7311f20-15ca-4b2d-a08d-8bb992a3a0cd
title: SdbGetNextChild function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbGetNextChild
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbGetNextChild function

Searches for the next child TAG within the specified parent and returns the **TAGID** of the next child.

## Syntax


```C++
TAGID WINAPI SdbGetNextChild(
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

The **TAGID** of the previous child.

</dd> </dl>

## Return value

The **TAGID** of the child or **TAGID\_NULL** if no child is found.

## Remarks

Before calling this function, call the [**SdbGetFirstChild**](sdbgetfirstchild.md) function.

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

[**SdbFindNextTag**](sdbfindnexttag.md)
</dt> <dt>

[**SdbGetFirstChild**](sdbgetfirstchild.md)
</dt> </dl>

 

 




