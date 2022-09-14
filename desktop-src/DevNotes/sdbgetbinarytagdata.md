---
description: Retrieves the binary data for the specified TAGID.
ms.assetid: 18992406-67b4-4c48-9629-04d6bf1c5824
title: SdbGetBinaryTagData function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbGetBinaryTagData
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbGetBinaryTagData function

Retrieves the binary data for the specified **TAGID**.

## Syntax


```C++
PVOID WINAPI SdbGetBinaryTagData(
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

The **TAGID** that corresponds to the data to be retrieved.

</dd> </dl>

## Return value

The function returns a pointer to the binary data or **NULL** if the **TAGID** is invalid.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



## See also

<dl> <dt>

[**SdbGetStringTagPtr**](sdbgetstringtagptr.md)
</dt> <dt>

[**SdbReadDWORDTag**](sdbreaddwordtag.md)
</dt> <dt>

[**SdbReadQWORDTag**](sdbreadqwordtag.md)
</dt> <dt>

[**SdbReadStringTag**](sdbreadstringtag.md)
</dt> </dl>

 

 




