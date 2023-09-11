---
description: Creates a wait completion packet object with the specified access rights and attributes.
title: NtCreateWaitCompletionPacket function
ms.topic: reference
ms.date: 08/30/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtCreateWaitCompletionPacket
api_type: 
- DllExport
api_location: 
- ntdll.dll
---

# NtCreateWaitCompletionPacket function

Creates a wait completion packet object with the specified access rights and attributes.

## Syntax


```C++
NTSTATUS NtCreateWaitCompletionPacket (
    _Out_ PHANDLE WaitCompletionPacketHandle,
    _In_ ACCESS_MASK DesiredAccess,
    _In_opt_ POBJECT_ATTRIBUTES ObjectAttributes
    )
```

## Parameters

### WaitCompletionPacketHandle [out]

A pointer to a variable that receives the wait completion packet handle.

### DesiredAccess [in]

The desired types of access for the wait completion packet.

### ObjectAttributes [in]

A pointer to an object attributes structure.

## Return value

An NTSTATUS code. For more information, see [Using NTSTATUS values](/windows-hardware/drivers/kernel/using-ntstatus-values).

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions. The API is exported from ntdll.dll.


## Requirements

| Requirement | Value |
|-----------------------------------|-------------------------------------------------------------------------------------------------------|
| DLL                   | ntdll.dll              |




 
