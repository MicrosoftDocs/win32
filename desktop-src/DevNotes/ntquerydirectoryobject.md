---
description: Retrieves information about the specified directory object.
ms.assetid: a2c67c4d-4753-4d47-a404-31d067a78bf4
title: NtQueryDirectoryObject function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtQueryDirectoryObject
api_type: 
- DllExport
api_location: 
- Ntdll.dll
---

# NtQueryDirectoryObject function

\[This function may be altered or unavailable in the future.\]

Retrieves information about the specified directory object.

## Syntax


```C++
NTSTATUS WINAPI NtQueryDirectoryObject(
  _In_      HANDLE  DirectoryHandle,
  _Out_opt_ PVOID   Buffer,
  _In_      ULONG   Length,
  _In_      BOOLEAN ReturnSingleEntry,
  _In_      BOOLEAN RestartScan,
  _Inout_   PULONG  Context,
  _Out_opt_ PULONG  ReturnLength
);
```



## Parameters

<dl> <dt>

*DirectoryHandle* \[in\]
</dt> <dd>

A handle to the directory object.

</dd> <dt>

*Buffer* \[out, optional\]
</dt> <dd>

A pointer to a buffer that receives the directory information. This buffer receives one or more **OBJECT\_DIRECTORY\_INFORMATION** structures, the last one being **NULL**, followed by strings that contain the names of the directory entries. For more information, see Remarks.

</dd> <dt>

*Length* \[in\]
</dt> <dd>

The size of the user-supplied output buffer, in bytes.

</dd> <dt>

*ReturnSingleEntry* \[in\]
</dt> <dd>

Indicates whether the function should return only a single entry.

</dd> <dt>

*RestartScan* \[in\]
</dt> <dd>

Indicates whether to restart the scan or continue the enumeration using the information passed in the *Context* parameter.

</dd> <dt>

*Context* \[in, out\]
</dt> <dd>

The enumeration context.

</dd> <dt>

*ReturnLength* \[out, optional\]
</dt> <dd>

A pointer to a variable that receives the length of the directory information returned in the output buffer, in bytes.

</dd> </dl>

## Return value

The function returns **STATUS\_SUCCESS** or an error status.

## Remarks

The following is the definition of the **OBJECT\_DIRECTORY\_INFORMATION** structure.

``` syntax
typedef struct _OBJECT_DIRECTORY_INFORMATION {
    UNICODE_STRING Name;
    UNICODE_STRING TypeName;
} OBJECT_DIRECTORY_INFORMATION, *POBJECT_DIRECTORY_INFORMATION;
```

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|--------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ntdll.dll</dt> </dl> |



## See also

<dl> <dt>

[**NtOpenDirectoryObject**](ntopendirectoryobject.md)
</dt> </dl>

 

 
