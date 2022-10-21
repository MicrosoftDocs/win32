---
description: Retrieves a specified number of random bytes from the system random number generator.
ms.assetid: 5226f843-b919-4a23-86c1-ff85cec7184c
title: ProcessPrng function
ms.topic: reference
ms.date: 10/21/2022
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
  _Out_ pbyte  pbData,
  _In_  size_t cbData
);
```

## Parameters

<dl> <dt>

*pbData* \[out\]
</dt> <dd>

A pointer to a buffer that receives the retrieved bytes.

</dd> <dt>

*cbData* \[in\]
</dt> <dd>

The number of bytes to retrieve.

</dd> </dl>

## Return value

Always returns **TRUE**.

## Requirements

| Requirement | Value |
|--------|--------|
| Minimum supported client | Windows Vista with SP1 \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
| DLL                      | BCryptPrimitives.dll |
