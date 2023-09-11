---
description: Creates a wait completion association for the target object.
title: NtAssociateWaitCompletionPacket function
ms.topic: reference
ms.date: 08/30/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtAssociateWaitCompletionPacket
api_type: 
- DllExport
api_location: 
- ntdll.dll
---

# NtAssociateWaitCompletionPacket function

Creates a wait completion association for the target object.

## Syntax


```cpp
NTSTATUS NtAssociateWaitCompletionPacket (
    _In_ HANDLE WaitCompletionPacketHandle,
    _In_ HANDLE IoCompletionHandle,
    _In_ HANDLE TargetObjectHandle,
    _In_opt_ PVOID KeyContext,
    _In_opt_ PVOID ApcContext,
    _In_ NTSTATUS IoStatus,
    _In_ ULONG_PTR IoStatusInformation,
    _Out_opt_ PBOOLEAN AlreadySignaled
    )
```

## Parameters

### WaitCompletionPacketHandle [in]

A handle to a wait completion packet which describes the association. This object must not be in use.

### IoCompletionHandle [in]

A handle to an IO completion object which will receive a notification when the object becomes signaled.

### TargetObjectHandle [in]

A handle to a waitable object for which notifications are to be received.

### KeyContext [in]

Supplies the key context that is returned during a call to [NtRemoveIoCompletion](ntremoveiocompletion.md).

### ApcContext [in]

The apc context that is returned during a call to **NtRemoveIoCompletion**.

### IoStatus [in]

The IoStatus->Status data that is returned during a call to **NtRemoveIoCompletion**.

### IoStatusInformation [in]

The IoStatus->Information data that is returned during a call to NtRemoveIoCompletion.

### AlreadySignaled [out]

An optional pointer to a boolean variable that receives an indication of whether the target object was already signaled at the time of the association when this function succeeds.


## Return value

An NTSTATUS code. For more information, see [Using NTSTATUS values](/windows-hardware/drivers/kernel/using-ntstatus-values).

## Remarks

When the object is signaled, a packet is queued to the supplied completion port and the supplied values will be conveyed to a caller of [NtRemoveIoCompletion](ntremoveiocompletion.md). When the packet is picked up, the association must be reestablished by calling this function again. An error is returned if the wait completion packet is already in use for an association.


This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions. The API is exported from ntdll.dll.


## Requirements

| Requirement | Value |
|-----------------------------------|-------------------------------------------------------------------------------------------------------|
| DLL                   | ntdll.dll              |




 
