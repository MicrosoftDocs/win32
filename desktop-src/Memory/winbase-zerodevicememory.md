---
description: Sets the contents of a buffer to zeros without interference from compiler optimizations in situations where the developer needs to additionally be sure that alignment faults will not be generated when accessing device memory.
ms.assetid: f55de17c-2f9f-474b-bb36-8a001c1c9388
title: ZeroDeviceMemory function (winbase.h)
ms.topic: reference
ms.date: 01/19/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ZeroDeviceMemory
api_type: 
- HeaderDef
api_location: 
- winbase.h
- volatileaccessu.lib
---

# ZeroDeviceMemory function

The **ZeroDeviceMemory** function sets the contents of a buffer to zeros without interference from compiler optimizations in situations where the developer needs to additionally be sure that alignment faults will not be generated when accessing device memory.

> [!IMPORTANT]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

## Parameters

### Param Destination [out]

A pointer to the starting address of the block of memory to fill with zeros.

### Param Length [in]

The size of the block of memory to fill with zeros, in bytes.

## Syntax

```cpp
volatile void*
  ZeroDeviceMemory (
    _Out_writes_bytes_all_(Length) volatile void* Destination,
    SIZE_T Length
  );
```

## Remarks

This API is a convenience wrapper around [FillDeviceMemory](winbase-filldevicememory.md). See the remarks of **FillDeviceMemory** for more information.

> [!NOTE]
> This function works on all versions of Windows, not just the latest. You need to consume the latest SDK to get the function declaration from the `winbase.h` header. You also need the library (`volatileaccessu.lib`) from the latest SDK. However, the resulting binary will run fine on older versions of Windows.

## Example

```c
// In this scenario we are setting data on memory mapped
// as "device memory" (i.e. memory not backed by RAM) to the value zero. On
// some platforms like ARM64, device memory cannot tolerate
// memory accesses that are not naturally aligned (i.e. a 4-byte
// load must be 4-byte aligned). Functions like memset, FillMemory,
// and even FillVolatileMemory may perform unaligned memory accesses
// because it is typically faster to do this.
// To ensure only naturally aligned accesses happen, use FillDeviceMemory.
//
// ZeroDeviceMemory is a wrapper around FillDeviceMemory that sets the memory
// to zero.

ZeroDeviceMemory(DeviceMemoryBuffer, 100);
```

## Requirements

**Minimum supported client:** Windows 11 Insider Preview Build TBD

**Header:** winbase.h (include Winbase.h)

**Kernel-mode library:** volatileaccessk.lib

**User-mode library:** volatileaccessu.lib

## See also

- [FillDeviceMemory](winbase-filldevicememory.md)
- [ZeroMemory](/previous-versions/windows/desktop/legacy/aa366920(v=vs.85))
