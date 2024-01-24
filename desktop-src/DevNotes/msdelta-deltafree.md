---
description: Frees the specified memory block.
title: DeltaFree function
ms.topic: reference
ms.date: 12/03/2020
ms.keywords: DeltaFree
req.header: msdelta.h
req.dll: msdelta.dll
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DeltaFree
api_type: 
- DllExport
api_location: 
- msdelta.dll
---

# DeltaFree function

Frees the specified memory block. You must call this function after successful calls to [CreateDeltaB](msdelta-createdeltab.md) and [ApplyDeltaB](msdelta-applydeltab.md) to free the MSDelta-allocated memory buffer.

## Syntax

```cpp
BOOL  WINAPI  DeltaFree(
    LPVOID  lpMemory
    );
```

## Parameters

*lpMemory*

[in] Memory block to be freed.

## Return value

This function returns **TRUE** if it succeeds; otherwise, it returns **FALSE**. When the function returns **FALSE**, you can call [GetLastError](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) to get the corresponding Win32 system error code.

## Requirements

| Requirement | Value |
|----------------|---------------------------------------------------------------------------------------|
| Header | msdelta.h |
| DLL | msdelta.dll |
| Unicode | Not applicable |

## See also

[MSDelta](msdelta.md)

[CreateDeltaB](msdelta-createdeltab.md)

[ApplyDeltaB](msdelta-applydeltab.md)
