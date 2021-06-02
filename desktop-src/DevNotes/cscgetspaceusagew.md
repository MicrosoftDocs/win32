---
description: Retrieves information about the space used by the Offline Files cache.
ms.assetid: 3a6fa548-0e9a-4138-a5ec-cde0aeb2b811
title: CSCGetSpaceUsageW function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSCGetSpaceUsageW
api_type: 
- DllExport
api_location: 
- Cscmig.dll
---

# CSCGetSpaceUsageW function

\[This function is not supported and should not be used.\]

Retrieves information about the space used by the Offline Files cache.

## Syntax


```C++
BOOL WINAPI CSCGetSpaceUsageW(
  _Inout_ LPTSTR  lptzLocation,
  _In_    DWORD   dwSize,
  _Inout_ LPDWORD lpdwMaxSpaceHigh,
  _Inout_ LPDWORD lpdwMaxSpaceLow,
  _Inout_ LPDWORD lpdwCurrentSpaceHigh,
  _Inout_ LPDWORD lpdwCurrentSpaceLow,
  _Inout_ LPDWORD lpcntTotalFiles,
  _Inout_ LPDWORD lpcntTotalDirs
);
```



## Parameters

<dl> <dt>

*lptzLocation* \[in, out\]
</dt> <dd>

The directory location of the cache.

</dd> <dt>

*dwSize* \[in\]
</dt> <dd>

The size of the *lptzLocation* buffer, in characters.

</dd> <dt>

*lpdwMaxSpaceHigh* \[in, out\]
</dt> <dd>

The high-order **DWORD** of the maximum number of bytes available in the cache.

</dd> <dt>

*lpdwMaxSpaceLow* \[in, out\]
</dt> <dd>

The low-order **DWORD** of the maximum number of bytes available in the cache.

</dd> <dt>

*lpdwCurrentSpaceHigh* \[in, out\]
</dt> <dd>

The high-order **DWORD** of the current number of bytes available in the cache.

</dd> <dt>

*lpdwCurrentSpaceLow* \[in, out\]
</dt> <dd>

The low-order **DWORD** of the current number of bytes available in the cache.

</dd> <dt>

*lpcntTotalFiles* \[in, out\]
</dt> <dd>

The total number of files in the cache.

</dd> <dt>

*lpcntTotalDirs* \[in, out\]
</dt> <dd>

The total number of directories in the cache.

</dd> </dl>

## Return value

This function returns **TRUE** if it succeeds; otherwise, it returns **FALSE**.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|---------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Cscmig.dll</dt> </dl> |



 

 
