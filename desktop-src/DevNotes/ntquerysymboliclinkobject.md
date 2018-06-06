---
Description: Retrieves the target of a symbolic link.
ms.assetid: 10a6676c-96f7-4758-8868-bbccd37b5019
title: NtQuerySymbolicLinkObject function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                      |
|----------------|--------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ntdll.dll</dt> </dl> |



## See also

<dl> <dt>

[**NtOpenSymbolicLinkObject**](ntopensymboliclinkobject.md)
</dt> </dl>

 

 




