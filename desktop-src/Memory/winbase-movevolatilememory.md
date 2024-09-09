---
description: Function that copies the contents of a source memory block to a destination memory block and supports overlapping source and destination memory blocks.
ms.assetid: fac1f6d4-fc56-404b-b879-1e32cd7e06ac
title: MoveVolatileMemory function (winbase.h)
ms.topic: reference
ms.date: 01/19/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MoveVolatileMemory
api_type: 
- HeaderDef
api_location: 
- winbase.h
- volatileaccessu.lib
---

# MoveVolatileMemory function

Copies the contents of a source memory block to a destination memory block, and supports overlapping source and destination memory blocks.

> [!IMPORTANT]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

## Parameters

### Param Destination [out]

A pointer to the starting address of the copied block's destination.

### Param Source [in]

A pointer to the starting address of the block of memory to copy.

### Param Length [in]

The size of the block of memory to copy, in bytes.

## Syntax

```cpp
volatile void* __cdecl
  MoveVolatileMemory (
    _Out_writes_bytes_all_(Length) volatile void* Destination,
    _In_reads_bytes_(Length) volatile const void* Source,
    SIZE_T Length
  );
```

## Remarks

This API exists to provide [MoveMemory](/previous-versions/windows/desktop/legacy/aa366788(v=vs.85)) behavior (i.e., copying memory from one location to another) in situations where the developer needs to be sure that the copy operation occurs (i.e., is not subject to compiler optimizations). Unlike [CopyVolatileMemory](winbase-copyvolatilememory.md), this API handles cases where the *Source* and *Destination* buffer overlap.

The API has the following properties:

- The API is not recognized as a compiler intrinsic so the compiler will never optimize away the call (either entirely or replace the call with an "equivalent" sequence of instructions). This differs from **MoveMemory** which is subject to a variety of compiler optimizations.
- When the call returns, the data has been copied from *Source* to *Destination*. This functions memory accesses to the *Source* and *Destination* will only be performed within the function (i.e. the compiler cannot move memory accesses out of this function).
- The API may perform unaligned memory accesses if the platform allows for it.
- The API may access memory locations more than once as part of its copy operation.
- Similar to **MoveMemory** in that it supports copy operations when *Source* and *Destination* overlap each other

> [!NOTE]
> This function works on all versions of Windows, not just the latest. You need to consume the latest SDK to get the function declaration from the `winbase.h` header. You also need the library (`volatileaccessu.lib`) from the latest SDK. However, the resulting binary will run fine on older versions of Windows.

## Example

```c
HEADER MyHeader;
UCHAR RawBuffer[100];

// Ensure that the shared memory (which could be constantly changing)
// is copied in to the local MyHeader variable.
// Note that the compiler is allowed to optimize away calls to
// MoveMemory/RtlMoveMemory so those functions are not guaranteed to actually
// make a local copy of data.
//
// MoveVolatileMemory does handle
// buffers that overlap with each other (MoveMemory semantics).
// Assume SharedMemory points to virtual memory that is also mapped in an untrusted process.
// Assume that untrusted process is changing the memory contents while you are accessing it.
PVOID SharedMemory;

MoveVolatileMemory(&MyHeader, SharedMemory, sizeof(MyHeader));

if (MyHeader.Size < 100) {
  // Because MyHeader is local and we are guaranteed we actually made
  // a local copy, we can be sure that the "Size" value will not change
  // between the previous bounds check and the below call to RtlFillMemory.
  // If RtlMoveMemory/RtlMoveMemory had been used to copy the data, it is possible
  // that a compiler may optimize away the call to MoveMemory and instead fetch
  // the “size” field of MyHeader directly from untrusted memory two times.
  // The first time it would be fetched for the bounds check, and the second
  // time it is fetched is for the call to FillMemory. It is possible the memory
  // could have changed between the two accesses resulting in the size check
  // being ineffective.

  FillMemory (RawBuffer, MyHeader.Size, 0);
}
```

## Requirements

**Minimum supported client:** Windows 11 Insider Preview Build TBD

**Header:** winbase.h (include Winbase.h)

**Kernel-mode library:** volatileaccessk.lib

**User-mode library:** volatileaccessu.lib

## See also

- [MoveMemory](/previous-versions/windows/desktop/legacy/aa366788(v=vs.85))
- [CopyVolatileMemory](winbase-copyvolatilememory.md)
