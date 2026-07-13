---
description: Fills a block of memory with zeros in a way that is guaranteed to be secure.
ms.assetid: c4cea049-d189-4592-8e08-37ae7121a2ad
title: SecureZeroMemory2 function (winbase.h)
ms.topic: reference
ms.date: 01/19/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SecureZeroMemory2
api_type: 
- HeaderDef
api_location: 
- winbase.h
- volatileaccessu.lib
---

# SecureZeroMemory2 function

The **SecureZeroMemory2** function fills a block of memory with zeros in a way that is guaranteed to be secure.

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
  SecureZeroMemory2 (
    _Out_writes_bytes_all_(Length) volatile void* Destination,
    SIZE_T Length
  );
```

## Remarks

This API is a convenience wrapper around [FillVolatileMemory](winbase-fillvolatilememory.md) and is identical to [ZeroVolatileMemory](winbase-zerovolatilememory.md). See the remarks of **FillVolatileMemory** for more information.

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
// (the former two are convienence wrappers around the latter). These
// calls will not be optimized away by the compiler.
// Note that SecureZeroMemory2 performs better than the old
// SecureZeroMemory API.

SecureZeroMemory2(&SensitiveData, sizeof(SensitiveData));
```

## Requirements

**Minimum supported client:** Windows 11 Insider Preview Build TBD

**Header:** winbase.h (include Winbase.h)

**Kernel-mode library:** volatileaccessk.lib

**User-mode library:** volatileaccessu.lib

## See also

- [SecureZeroMemory](/previous-versions/windows/desktop/legacy/aa366877(v=vs.85))
- [FillVolatileMemory](winbase-fillvolatilememory.md)
- [ZeroVolatileMemory](winbase-zerovolatilememory.md)
