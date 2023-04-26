---
description: Uses the delta and source (provided as buffers) to create a new copy of the target data. The output data is returned in an MSDelta-allocated buffer. (ApplyDeltaW)
title: ApplyDeltaW function
ms.topic: reference
ms.date: 12/03/2020
ms.keywords: ApplyDeltaW
req.header: msdelta.h
req.dll: msdelta.dll
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ApplyDeltaW
api_type: 
- DllExport
api_location: 
- msdelta.dll
---

# ApplyDeltaW function

Uses the delta and source (provided as buffers) to create a new copy of the target data. The output data is returned in an MSDelta-allocated buffer.

> [!NOTE]
> You must call [DeltaFree](msdelta-deltafree.md) to free the output buffer after this function has completed.

> [!NOTE]
> If the specified delta was created using [PatchAPI](patchapi.md), and the [DELTA_APPLY_FLAG_ALLOW_PA19](/previous-versions/bb417345(v=msdn.10)#delta_flag_type-flags) flag is set, MSDelta will call PatchAPI to apply the delta.

## Syntax

```cpp
BOOL  WINAPI  ApplyDeltaW(
    DELTA_FLAG_TYPE  ApplyFlags,
    DELTA_INPUT      Source,
    DELTA_INPUT      Delta,
    LPDELTA_OUTPUT   lpTarget
   );
```

## Parameters

*ApplyFlags*

[in] Either [DELTA_FLAG_NONE](/previous-versions/bb417345(v=msdn.10)#delta_flag_type-flags) or [DELTA_APPLY_FLAG_ALLOW_PA19](/previous-versions/bb417345(v=msdn.10)#delta_flag_type-flags).

*Source*

[in] A [DELTA_INPUT](/previous-versions/bb417345(v=msdn.10)#delta-input-structure) structure containing a pointer to the file path containing the source data.

*Delta*

[in] A [DELTA_INPUT](/previous-versions/bb417345(v=msdn.10)#delta-input-structure) structure containing a pointer to the file path containing the delta data.

*lpTarget*

[out] Pointer to the [DELTA_OUTPUT](/previous-versions/bb417345(v=msdn.10)#delta-output-structure) structure where the target is to be written.

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

[DeltaFree](msdelta-deltafree.md)
