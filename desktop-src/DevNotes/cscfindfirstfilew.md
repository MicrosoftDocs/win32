---
description: Searches for a file in the Offline Files cache that meets the specified criteria.
ms.assetid: 09de6c55-fc37-4c0a-b5a0-ea73f06793d5
title: CSCFindFirstFileW function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSCFindFirstFileW
api_type: 
- DllExport
api_location: 
- Cscmig.dll
---

# CSCFindFirstFileW function

\[This function is not supported and should not be used.\]

Searches for a file in the Offline Files cache that meets the specified criteria.

## Syntax


```C++
HANDLE WINAPI CSCFindFirstFileW(
  _In_  LPCWSTR          lpszFileName,
  _Out_ WIN32_FIND_DATAW *lpFind32,
  _Out_ LPDWORD          lpdwStatus,
  _Out_ LPDWORD          lpdwPinCount,
  _Out_ LPDWORD          lpdwHintFlags,
  _Out_ FILETIME         *lpOrgFileTime
);
```



## Parameters

<dl> <dt>

*lpszFileName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that specifies a valid UNC directory or path.

</dd> <dt>

*lpFind32* \[out\]
</dt> <dd>

A pointer to the [**WIN32\_FIND\_DATA**](/windows/win32/api/minwinbase/ns-minwinbase-win32_find_dataa) structure that receives information about the file or subdirectory.

</dd> <dt>

*lpdwStatus* \[out\]
</dt> <dd>

An NTSTATUS code that indicates the status of the call.

</dd> <dt>

*lpdwPinCount* \[out\]
</dt> <dd>

This parameter is nonzero if the file has been made available offline or 0 otherwise.

</dd> <dt>

*lpdwHintFlags* \[out\]
</dt> <dd>

This parameter can be one of the following values.



| Value                                                                                                                                                                                                                                                                                | Meaning                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="FLAG_CSC_HINT_PIN_USER"></span><span id="flag_csc_hint_pin_user"></span><dl> <dt>**FLAG\_CSC\_HINT\_PIN\_USER**</dt> <dt>0x01</dt> </dl>                                | A user has made the file available offline.<br/>                                                                                                |
| <span id="FLAG_CSC_HINT_PIN_INHERIT_USER"></span><span id="flag_csc_hint_pin_inherit_user"></span><dl> <dt>**FLAG\_CSC\_HINT\_PIN\_INHERIT\_USER**</dt> <dt>0x02</dt> </dl>       | A user has made the parent available offline and marked the parent such that its children are available offline.<br/>                           |
| <span id="FLAG_CSC_HINT_PIN_INHERIT_SYSTEM"></span><span id="flag_csc_hint_pin_inherit_system"></span><dl> <dt>**FLAG\_CSC\_HINT\_PIN\_INHERIT\_SYSTEM**</dt> <dt>0x04</dt> </dl> | An administrator or group policy has made the parent available offline and marked the parent such that its children are available offline.<br/> |
| <span id="FLAG_CSC_HINT_PIN_SYSTEM"></span><span id="flag_csc_hint_pin_system"></span><dl> <dt>**FLAG\_CSC\_HINT\_PIN\_SYSTEM**</dt> <dt>0x10</dt> </dl>                          | An administrator or group policy has made the file available offline.<br/>                                                                      |



 

</dd> <dt>

*lpOrgFileTime* \[out\]
</dt> <dd>

A pointer to a [**FILETIME**](/windows/win32/api/minwinbase/ns-minwinbase-filetime) structure to receive the date and time information for the file or subdirectory.

</dd> </dl>

## Return value

If the function succeeds, the return value is a search handle used in a subsequent call to [**CSCFindNextFileW**](cscfindnextfilew.md) or [**CSCFindClose**](cscfindclose.md).

If the function fails, the return value is **INVALID\_HANDLE\_VALUE**.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|---------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Cscmig.dll</dt> </dl> |



 

 
