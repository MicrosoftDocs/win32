---
description: Closes the specified shim database.
ms.assetid: e4480860-8055-4134-b6ed-926c010d462f
title: SdbCloseDatabase function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbCloseDatabase
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbCloseDatabase function

Closes the specified shim database.

## Syntax


```C++
void WINAPI SdbCloseDatabase(
  _Inout_ PDB pdb
);
```



## Parameters

<dl> <dt>

*pdb* \[in, out\]
</dt> <dd>

A handle to the shim database. This parameter cannot be **NULL**.

</dd> </dl>

## Return value

This function does not return a value.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



## See also

<dl> <dt>

[**SdbOpenDatabase**](sdbopendatabase.md)
</dt> </dl>

 

 




