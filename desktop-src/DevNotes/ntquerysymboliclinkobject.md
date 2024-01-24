---
description: Retrieves the target of a symbolic link.
ms.assetid: 10a6676c-96f7-4758-8868-bbccd37b5019
title: NtQuerySymbolicLinkObject function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtQuerySymbolicLinkObject
api_type: 
- DllExport
api_location: 
- Ntdll.dll
---

# NtQuerySymbolicLinkObject function

\[This function may be altered or unavailable in the future.\]

Retrieves the target of a symbolic link.

## Syntax


```C++
NTSTATUS WINAPI NtQuerySymbolicLinkObject(
  _In_      HANDLE          LinkHandle,
  _Inout_   PUNICODE_STRING LinkTarget,
  _Out_opt_ PULONG          ReturnedLength
);
```



## Parameters

<dl> <dt>

*LinkHandle* \[in\]
</dt> <dd>

A handle to the symbolic link object.

</dd> <dt>

*LinkTarget* \[in, out\]
</dt> <dd>

A pointer to an initialized Unicode string that receives the target of the symbolic link. The **MaximumLength** and **Buffer** members must be set if the call fails.

</dd> <dt>

*ReturnedLength* \[out, optional\]
</dt> <dd>

A pointer to a variable that receives the length of the Unicode string returned in the *LinkTarget* parameter. If the function returns **STATUS\_BUFFER\_TOO\_SMALL**, this variable receives the required buffer size.

</dd> </dl>

## Return value

The function returns **STATUS\_SUCCESS** or an error status.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|--------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ntdll.dll</dt> </dl> |



## See also

<dl> <dt>

[**NtOpenSymbolicLinkObject**](ntopensymboliclinkobject.md)
</dt> </dl>

 

 
