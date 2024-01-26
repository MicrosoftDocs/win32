---
description: Sets the contents of a buffer without interference from compiler optimizations in situations where the developer needs to additionally be sure that alignment faults will not be generated when accessing device memory.
ms.assetid: 188fe7b8-b989-4062-b9c6-68b9bbf2053c
title: FillDeviceMemory function (winbase.h)
ms.topic: reference
ms.date: 01/19/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FillDeviceMemory
api_type: 
- HeaderDef
api_location: 
- winbase.h
- volatileaccessu.lib
---

# FillDeviceMemory function

The **FillDeviceMemory** function sets the contents of a buffer without interference from compiler optimizations in situations where the developer needs to additionally be sure that alignment faults will not be generated when accessing device memory.

> [!IMPORTANT]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

## Parameters

### Param Destination [out]

A pointer to the starting address of the block of memory to fill.

### Param Length [in]

The size of the block of memory to fill, in bytes. This value must be less than the size of the Destination buffer.

### Param Fill [in]

The byte value with which to fill the memory block.

## Syntax

```cpp
volatile void*
  FillDeviceMemory (
    _Out_writes_bytes_all_(Length) volatile void* Destination,
    SIZE_T Length,
    INT Fill
  );
```

## Remarks

This API exists to provide [FillVolatileMemory](winbase-fillvolatilememory.md) behavior (i.e. setting the contents of a buffer without interference from compiler optimizations) in situations where the developer needs to additionally be sure that alignment faults will not be generated when accessing device memory. The API has the following properties:

- The API is not recognized as a compiler intrinsic so the compiler will never optimize away the call (either entirely or replace the call with an "equivalent" sequence of instructions). This differs from [FillMemory](/previous-versions/windows/desktop/legacy/aa366561(v=vs.85)) which is subject to a variety of compiler optimizations.
- When the call is complete, the buffer has been overwritten with the desired value. This functions memory accesses to the *Destination* will only be performed within the function (i.e. the compiler cannot move memory accesses out of this function).
- The API may perform unaligned memory accesses only if the CPU supports unaligned memory accesses on device memory. If the CPU does not support unaligned device memory accesses, only aligned accesses will be performed.
- The API may access memory locations more than once as part of its operation.

> [!NOTE]
> This function only guarantees that the CPU’s requirements for accessing memory mapped as **device memory** are respected. If a specific device has its own specific requirements for being accessed, this function should not be used (and instead, the developer must implement their own accessor functions). For example, this function makes no guarantee about the size of memory accesses generated (unless the CPU itself enforces these requirements).

> [!NOTE]
> This function works on all versions of Windows, not just the latest. You need to consume the latest SDK to get the function declaration from the `winbase.h` header. You also need the library (`volatileaccessu.lib`) from the latest SDK. However, the resulting binary will run fine on older versions of Windows.

## Example

```c
// In this scenario we are setting data on memory mapped
// as "device memory" (i.e. memory not backed by RAM). On
// some platforms like ARM64, device memory cannot tolerate
// memory accesses that are not naturally aligned (i.e. a 4-byte
// load must be 4-byte aligned). Functions like memset, FillMemory,
// and even FillVolatileMemory may perform unaligned memory accesses
// because it is typically faster to do this.
// To ensure only naturally aligned accesses happen, use FillDeviceMemory.

FillDeviceMemory(DeviceMemoryBuffer, 100, 0xAA);
```

## Requirements

**Minimum supported client:** Windows 11 Insider Preview Build TBD

**Header:** winbase.h (include Winbase.h)

**Kernel-mode library:** volatileaccessk.lib

**User-mode library:** volatileaccessu.lib

## See also

- [FillVolatileMemory](winbase-fillvolatilememory.md)
- [FillMemory](/previous-versions/windows/desktop/legacy/aa366561(v=vs.85))
