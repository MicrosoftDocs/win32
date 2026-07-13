---
description: Converts a DOS path name to an NT path name.
title: RtlDosPathNameToNtPathName_U_WithStatus function
ms.topic: reference
ms.date: 08/30/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RtlDosPathNameToNtPathName_U_WithStatus
api_type: 
- DllExport
api_location: 
- ntdll.dll
---

# RtlDosPathNameToNtPathName_U_WithStatus function

Converts a DOS path name to an NT path name.

## Syntax


```cpp
NTSTATUS RtlDosPathNameToNtPathName_U_WithStatus(
    __in PCWSTR DosFileName,
    __out PUNICODE_STRING NtFileName,
    __deref_opt_out_opt PWSTR *FilePart,
    __reserved PVOID Reserved
    )
```

## Parameters

### DosFileName [in]

A pointer to a DOS file name path.

### PUNICODE_STRING [out]

A pointer to a reference-counted Unicode string structure containing a Win32-style NT path name.

### FilePart [out, optional]

If present, supplies a pointer to a variable which, on success, receives a pointer to the base name portion of the output NT path name.

### Reserved

Reserved.

## Return value

An NTSTATUS code. For more information, see [Using NTSTATUS values](/windows-hardware/drivers/kernel/using-ntstatus-values).

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions. The API is exported from ntdll.dll.


## Requirements

| Requirement | Value |
|-----------------------------------|-------------------------------------------------------------------------------------------------------|
| DLL                   | ntdll.dll              |




 
