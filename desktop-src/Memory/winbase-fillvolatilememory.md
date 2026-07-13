---
description: Fills a block of memory with the specified fill value.
ms.assetid: 98112780-221b-4ffe-997e-d4a3cd86d6d2
title: FillVolatileMemory function (winbase.h)
ms.topic: reference
ms.date: 01/19/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FillVolatileMemory
api_type: 
- HeaderDef
api_location: 
- winbase.h
- volatileaccessu.lib
---

# FillVolatileMemory function

The **FillVolatileMemory** function fills a block of memory with the specified fill value.

> [!IMPORTANT]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

## Parameters

### Param Destination [out]

A pointer to the starting address of the block of memory to fill.

### Param Length [in]

The size of the block of memory to fill, in bytes. This value must be less than the size of the *Destination* buffer.

### Param Fill [in]

The byte value with which to fill the memory block.

## Syntax

```cpp
volatile void*
  FillVolatileMemory (
    _Out_writes_bytes_all_(Length) volatile void* Destination,
    SIZE_T Length,
    INT Fill
  );
```

## Remarks

This API exists to provide [FillMemory](/previous-versions/windows/desktop/legacy/aa366561(v=vs.85)) behavior (i.e., setting the contents of a buffer) in situations where the developer needs to be sure that the setting operation occurs (i.e., is not subject to compiler optimizations). The API has the following properties:

- The API is not recognized as a compiler intrinsic so the compiler will never optimize away the call (either entirely or replace the call with an "equivalent" sequence of instructions). This differs from **FillMemory** which is subject to a variety of compiler optimizations.
- When the call returns, the buffer has been overwritten with the desired value. This functions memory accesses to the *Destination* will only be performed within the function (i.e. the compiler cannot move memory accesses out of this function).
- The API may perform unaligned memory accesses if the platform allows for it.
- The API may access memory locations more than once as part of its operation.

> [!NOTE]
> This function works on all versions of Windows, not just the latest. You need to consume the latest SDK to get the function declaration from the `winbase.h` header. You also need the library (`volatileaccessu.lib`) from the latest SDK. However, the resulting binary will run fine on older versions of Windows.

## Example

```c
UCHAR SensitiveData[100];

// Imagine we temporarily store some sensitive cryptographic
// material in a buffer.

StoreCryptographicKey(&SensitiveData);
DoCryptographicOperation(&SensitiveData);

// Now that we are done using the sensitive data we want to
// erase it from the stack. We cannot call FillMemory because
// if the compiler realizes that "SensitiveData" is not
// referenced again the compiler can remove the call to FillMemory.
// Instead we can call SecureZeroMemory2, ZeroVolatileMemory, or FillVolatileMemory
// (the former two are convenience wrappers around the latter). These
// calls will not be optimized away by the compiler.
// Note that SecureZeroMemory2 performs better than the old
// SecureZeroMemory API.

FillVolatileMemory(&SensitiveData, sizeof(SensitiveData), 0);
```

## Requirements

**Minimum supported client:** Windows 11 Insider Preview Build TBD

**Header:** winbase.h (include Winbase.h)

**Kernel-mode library:** volatileaccessk.lib

**User-mode library:** volatileaccessu.lib

## See also

- [FillMemory](/previous-versions/windows/desktop/legacy/aa366561(v=vs.85))
- [ZeroVolatileMemory](winbase-zerovolatilememory.md)
