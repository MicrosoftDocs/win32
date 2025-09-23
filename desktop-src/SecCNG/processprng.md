---
description: Retrieves a specified number of random bytes from the user-mode per-processor random number generator.
ms.assetid: 5226f843-b919-4a23-86c1-ff85cec7184c
title: ProcessPrng function
ms.topic: reference
ms.date: 07/14/2025
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ProcessPrng
api_type: 
- DllExport
api_location: 
- BCryptPrimitives.dll
---

# ProcessPrng function

The **ProcessPrng** function retrieves a specified number of random bytes from the user-mode per-processor random number generator.

## Syntax

```C++
BOOL ProcessPrng(
  _Out_ PBYTE  pbData,
        SIZE_T cbData
);
```

## Parameters

*pbData* `[out]`

A pointer to a buffer that receives the retrieved bytes.

*cbData*

The number of bytes to retrieve.

## Return value

Always returns **TRUE**.

## Requirements

| Requirement | Value |
|--------|--------|
| Minimum supported client | Windows 8 \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 R2 \[desktop apps only\] |
| DLL | `BCryptPrimitives.dll` |
| APISet | `CngRngExt` |
