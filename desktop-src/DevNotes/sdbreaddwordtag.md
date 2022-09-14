---
description: Retrieves the DWORD value for the specified TAGID.
ms.assetid: 6610e101-9068-4812-b0ca-528658b62535
title: SdbReadDWORDTag function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbReadDWORDTag
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbReadDWORDTag function

Retrieves the **DWORD** value for the specified **TAGID**.

## Syntax


```C++
DWORD WINAPI SdbReadDWORDTag(
  _In_ PDB   pdb,
  _In_ TAGID tiWhich,
  _In_ DWORD dwDefault
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

</dd> <dt>

*dwDefault* \[in\]
</dt> <dd>

The default value to be returned on failure.

</dd> </dl>

## Return value

The function returns the value on success or *dwDefault* on failure.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



## See also

<dl> <dt>

[**SdbGetBinaryTagData**](sdbgetbinarytagdata.md)
</dt> <dt>

[**SdbGetStringTagPtr**](sdbgetstringtagptr.md)
</dt> <dt>

[**SdbReadQWORDTag**](sdbreadqwordtag.md)
</dt> <dt>

[**SdbReadStringTag**](sdbreadstringtag.md)
</dt> </dl>

 

 




