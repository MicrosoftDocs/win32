---
description: Removes an entry from an I/O completion object. 
title: NtRemoveIoCompletion function
ms.topic: reference
ms.date: 08/30/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtRemoveIoCompletion
api_type: 
- DllExport
api_location: 
- ntdll.dll
---

# NtRemoveIoCompletion function

Removes an entry from an I/O completion object. If there are currently no entries available, then the calling thread waits for an entry.

## Syntax


```cpp
NTSTATUS NtRemoveIoCompletion (
    __in HANDLE IoCompletionHandle,
    __out PVOID *KeyContext,
    __out PVOID *ApcContext,
    __out PIO_STATUS_BLOCK IoStatusBlock,
    __in_opt PLARGE_INTEGER Timeout
    )
```

## Parameters

### IoCompletionHandle [in]

A handle to an I/O completion object.

### KeyContext [out]

A pointer to a variable that receives the key context that was specified when the I/O completion object was associated with a file object.

### ApcContext [out]

A pointer to a variable that receives the context that was specified when the I/O operation was issued.

### IoStatusBlock [out]

A pointer to a variable that receives the I/O completion status.

### Timeout [in, optional]

A pointer to an optional time out value.

## Return value

An NTSTATUS code. For more information, see [Using NTSTATUS values](/windows-hardware/drivers/kernel/using-ntstatus-values).

## Remarks

IO_STATUS_BLOCK has the following definition.

```cpp
typedef struct _IO_STATUS_BLOCK {  
    union {  
        NTSTATUS Status;  
        PVOID Pointer;  
    } DUMMYUNIONNAME;  
  
    ULONG_PTR Information;  
} IO_STATUS_BLOCK, *PIO_STATUS_BLOCK;  
```

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions. The API is exported from ntdll.dll.


## Requirements

| Requirement | Value |
|-----------------------------------|-------------------------------------------------------------------------------------------------------|
| DLL                   | ntdll.dll              |




 
