---
description: Retrieves the TAGID and a handle to the shim database for the specified TAGREF.
ms.assetid: 869c6af5-4c10-4358-9d6a-1a354be6f4e9
title: SdbTagRefToTagID function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbTagRefToTagID
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbTagRefToTagID function

Retrieves the **TAGID** and a handle to the shim database for the specified [**TAGREF**](tagref.md).

## Syntax


```C++
BOOL WINAPI SdbTagRefToTagID(
  _In_  HSDB   hSDB,
  _In_  TAGREF trWhich,
  _Out_ PDB    *ppdb,
  _Out_ TAGID  *ptiWhich
);
```



## Parameters

<dl> <dt>

*hSDB* \[in\]
</dt> <dd>

A handle to the shim database returned by the [**SdbInitDatabase**](sdbinitdatabase.md) function.

</dd> <dt>

*trWhich* \[in\]
</dt> <dd>

The [**TAGREF**](tagref.md).

</dd> <dt>

*ppdb* \[out\]
</dt> <dd>

The resulting handle to the shim database.

</dd> <dt>

*ptiWhich* \[out\]
</dt> <dd>

The resulting **TAGID**.

</dd> </dl>

## Return value

The function returns **TRUE** on success or **FALSE** on failure.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



## See also

<dl> <dt>

[**SdbInitDatabase**](sdbinitdatabase.md)
</dt> <dt>

[**TAGID**](tagid.md)
</dt> <dt>

[**TAGREF**](tagref.md)
</dt> </dl>

 

 




