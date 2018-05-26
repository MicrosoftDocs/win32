---
Description: Writes a NULL entry to the specified database.
ms.assetid: 2a29389b-d4f6-4527-a429-c9459b095f2f
title: SdbWriteNULLTag function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SdbWriteNULLTag function

Writes a **NULL** entry to the specified database.

## Syntax


```C++
BOOL WINAPI SdbWriteNULLTag(
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

The TAG for the entry. This TAG must be of type **TAG\_TYPE\_NULL**.

</dd> </dl>

## Return value

The function returns **TRUE** on success or **FALSE** on failure.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



## See also

<dl> <dt>

[**SdbWriteBinaryTag**](sdbwritebinarytag.md)
</dt> <dt>

[**SdbWriteDWORDTag**](sdbwritedwordtag.md)
</dt> <dt>

[**SdbWriteStringTag**](sdbwritestringtag.md)
</dt> <dt>

[**SdbWriteWORDTag**](sdbwritewordtag.md)
</dt> </dl>

 

 




