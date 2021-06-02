---
description: The ThunkConnect32 function is used by 16-bit device drivers (for MS-DOS) that call into the 32-bit kernel.
ms.assetid: 3376ca67-04ea-4765-a2f4-15a84d5c84d4
title: ThunkConnect32 function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ThunkConnect32
api_type: 
- DllExport
api_location: 
- Kernel32.dll
---

# ThunkConnect32 function

\[This function was supported for backward compatibility, but is not present in current versions of Windows. New device drivers should be 32- or 64-bit and do not need this function.\]

The **ThunkConnect32** function is used by 16-bit device drivers (for MS-DOS) that call into the 32-bit kernel.

## Syntax


```C++
BOOL ThunkConnect32(
   LPVOID lpThunkData32,
   LPSTR  pszThunkData16Name,
   LPSTR  pszDll16,
   LPSTR  pszDll32,
   HANDLE hInstance,
   DWORD  dwReason
);
```



## Parameters

<dl> <dt>

*lpThunkData32* 
</dt> <dd>

Ignored.

</dd> <dt>

*pszThunkData16Name* 
</dt> <dd>

Ignored.

</dd> <dt>

*pszDll16* 
</dt> <dd>

Ignored.

</dd> <dt>

*pszDll32* 
</dt> <dd>

Ignored.

</dd> <dt>

*hInstance* 
</dt> <dd>

Ignored.

</dd> <dt>

*dwReason* 
</dt> <dd>

Ignored.

</dd> </dl>

## Return value

Always returns **FALSE**.

## Requirements



| Requirement | Value |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Kernel32.dll</dt> </dl> |



 

 




