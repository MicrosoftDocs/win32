---
description: Retrieves the system AppPatch directory.
ms.assetid: 1c79411f-1f90-4b90-84c7-24a34cf0d91d
title: SdbGetAppPatchDir function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbGetAppPatchDir
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbGetAppPatchDir function

Retrieves the system AppPatch directory.

## Syntax


```C++
void WINAPI SdbGetAppPatchDir(
  _In_opt_ HSDB   hSDB,
  _Out_    LPTSTR szAppPatchPath,
  _In_     DWORD  cchSize
);
```



## Parameters

<dl> <dt>

*hSDB* \[in, optional\]
</dt> <dd>

A handle to the shim database returned by the [**SdbInitDatabase**](sdbinitdatabase.md) function.

</dd> <dt>

*szAppPatchPath* \[out\]
</dt> <dd>

The resulting path.

</dd> <dt>

*cchSize* \[in\]
</dt> <dd>

The size of the *szAppPatchPath* buffer, in characters. If the function fails, this parameter is set to the empty string ("").

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

[**SdbInitDatabase**](sdbinitdatabase.md)
</dt> </dl>

 

 




