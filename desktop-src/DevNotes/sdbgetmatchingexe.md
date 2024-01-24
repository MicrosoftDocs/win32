---
description: Searches for the specified executable.
ms.assetid: 32c6b054-7e47-4427-bdfe-6b5066db4ac3
title: SdbGetMatchingExe function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbGetMatchingExe
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbGetMatchingExe function

Searches for the specified executable.

## Syntax


```C++
BOOL WINAPI SdbGetMatchingExe(
  _In_opt_ HSDB            hSDB,
  _In_     LPCTSTR         szPath,
  _In_opt_ LPCTSTR         szModuleName,
  _In_opt_ LPCTSTR         pszEnvironment,
  _In_     DWORD           dwFlags,
  _Out_    PSDBQUERYRESULT pQueryResult
);
```



## Parameters

<dl> <dt>

*hSDB* \[in, optional\]
</dt> <dd>

A handle to the shim database returned by the [**SdbInitDatabase**](sdbinitdatabase.md) function.

</dd> <dt>

*szPath* \[in\]
</dt> <dd>

The path of the executable.

</dd> <dt>

*szModuleName* \[in, optional\]
</dt> <dd>

The module name.

</dd> <dt>

*pszEnvironment* \[in, optional\]
</dt> <dd>

The environment variables to be used as search context.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

This parameter can be 0 or **SDBGMEF\_IGNORE\_ENVIRONMENT** (0x1).

</dd> <dt>

*pQueryResult* \[out\]
</dt> <dd>

An [**SDBQUERYRESULT**](sdbqueryresult.md) structure. If no match is found, the structure contains **TAGREF\_NULL**.

</dd> </dl>

## Return value

The function returns **TRUE** on success or **FALSE** on failure.

## Remarks

When you have finished with the returned [**TAGREF**](tagref.md), free it using the [**SdbReleaseMatchingExe**](sdbreleasematchingexe.md) function.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



## See also

<dl> <dt>

[**SdbInitDatabase**](sdbinitdatabase.md)
</dt> <dt>

[**SdbReleaseMatchingExe**](sdbreleasematchingexe.md)
</dt> </dl>

 

 




