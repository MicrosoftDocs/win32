---
Description: Retrieves the string data for the specified TAGID.
ms.assetid: c558e0bb-7e35-4298-93fb-400db00a2972
title: SdbGetStringTagPtr function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SdbGetStringTagPtr function

Retrieves the string data for the specified **TAGID**.

## Syntax


```C++
LPTSTR WINAPI SdbGetStringTagPtr(
  _In_ PDB   pdb,
  _In_ TAGID tiWhich
);
```



## Parameters

<dl> <dt>

*pdb* \[in\]
</dt> <dd>

A handle to the shim database.

</dd> <dt>

*tiWhich* \[in\]
</dt> <dd>

The **TAGID** that corresponds to the string data to be retrieved.

</dd> </dl>

## Return value

The function returns a pointer to the string data or **NULL** if the **TAGID** is invalid or not of type **TAG\_TYPE\_STRING** or **TAG\_TYPE\_STRINGREF**.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



## See also

<dl> <dt>

[**SdbGetBinaryTagData**](sdbgetbinarytagdata.md)
</dt> <dt>

[**SdbReadDWORDTag**](sdbreaddwordtag.md)
</dt> <dt>

[**SdbReadQWORDTag**](sdbreadqwordtag.md)
</dt> <dt>

[**SdbReadStringTag**](sdbreadstringtag.md)
</dt> </dl>

 

 




