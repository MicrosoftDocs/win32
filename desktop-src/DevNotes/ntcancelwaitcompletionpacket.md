---
description: Cancels an active wait completion association if it has not been picked up from the completion port.
title: NtCancelWaitCompletionPacket function
ms.topic: reference
ms.date: 08/30/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtCancelWaitCompletionPacket
api_type: 
- DllExport
api_location: 
- ntdll.dll
---

# NtCancelWaitCompletionPacket function

Cancels an active wait completion association if it has not been picked up from the completion port.

## Syntax


```cpp
NTSTATUS NtCancelWaitCompletionPacket (
    _In_ HANDLE WaitCompletionPacketHandle,
    _In_ BOOLEAN RemoveSignaledPacket
    )
```

## Parameters

### WaitCompletionPacketHandle [in]

A handle to a wait completion packet.

### RemoveSignaledPacket [in]

a boolean which determines whether this function will attempt to cancel a packet from an IO completion object queue.

## Return value

An NTSTATUS code. For more information, see [Using NTSTATUS values](/windows-hardware/drivers/kernel/using-ntstatus-values).

| Value | Description |
|-------|-------------|
| STATUS_SUCCESS | Success |
| STATUS_PENDING | The wait completion may be pending and the packet cannot be immediately reused. | 
| STATUS_CANCELLED | The packet has already been completed or if has never been associated. |

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions. The API is exported from ntdll.dll.


## Requirements

| Requirement | Value |
|-----------------------------------|-------------------------------------------------------------------------------------------------------|
| DLL                   | ntdll.dll              |




 
