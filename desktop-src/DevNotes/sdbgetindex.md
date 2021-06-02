---
description: Retrieves the index for the specified tag and key type from the specified database.
ms.assetid: 5fa44252-ba26-43ed-9de0-5917e4ec797c
title: SdbGetIndex function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbGetIndex
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbGetIndex function

Retrieves the index for the specified tag and key type from the specified database.

## Syntax


```C++
TAGID WINAPI SdbGetIndex(
  _In_      PDB     pdb,
  _In_      TAG     tWhich,
  _In_      TAG     tKey,
  _Out_opt_ LPDWORD lpdwFlags
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

The TAG.

</dd> <dt>

*tKey* \[in\]
</dt> <dd>

The key type.

</dd> <dt>

*lpdwFlags* \[out, optional\]
</dt> <dd>

This parameter can be 0 or **SHIMDB\_INDEX\_UNIQUE\_KEY** (0x00000001).

</dd> </dl>

## Return value

The **TAGID** of the index or **TAGID\_NULL**.

## Remarks

The resulting index can be used for read operations.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



 

 




