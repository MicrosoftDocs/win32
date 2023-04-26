---
description: Creates a delta between the source and target (provided as buffers) and returns the output delta as an MSDelta-allocated buffer. (CreateDeltaW)
title: CreateDeltaW function
ms.topic: reference
ms.date: 12/03/2020
ms.keywords: CreateDeltaW
req.header: msdelta.h
req.dll: msdelta.dll
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CreateDeltaW
api_type: 
- DllExport
api_location: 
- msdelta.dll
---

# CreateDeltaB function

Creates a delta between the source and target (provided as buffers) and returns the output delta as an MSDelta-allocated buffer.

> [!NOTE]
> You must call [DeltaFree](msdelta-deltafree.md) to free the output buffer after this function has completed.

## Syntax

```cpp
BOOL  WINAPI  CreateDeltaW(
           DELTA_FILE_TYPE  FileTypeSet,
           DELTA_FLAG_TYPE  SetFlags,
           DELTA_FLAG_TYPE  ResetFlags,
           DELTA_INPUT      Source,
           DELTA_INPUT      Target,
           DELTA_INPUT      SourceOptions,
           DELTA_INPUT      TargetOptions,
           DELTA_INPUT      GlobalOptions,
    const  FILETIME        *lpTargetFileTime,
           ALG_ID           HashAlgId,
           LPDELTA_OUTPUT   lpDelta
    );
```

## Parameters

*FileTypeSet*

[in] The [DELTA_FILE_TYPE](/previous-versions/bb417345(v=msdn.10)#file-type-sets) value that indicates the file type set to be used for the create process.

*SetFlags*

[in] One or more [DELTA_FLAG_TYPE](/previous-versions/bb417345(v=msdn.10)#delta_flag_type-flags) values that specify the flags to be used during the create process, in addition to the default flags.

*ResetFlags*

[in] One or more [DELTA_FLAG_TYPE](/previous-versions/bb417345(v=msdn.10)#delta_flag_type-flags) values that specify the default flags to be reset during the create process.

*Source*

[in] A [DELTA_INPUT](/previous-versions/bb417345(v=msdn.10)#delta-input-structure) structure containing a pointer to the file path containing the source data.

*Target*

[in] A [DELTA_INPUT](/previous-versions/bb417345(v=msdn.10)#delta-input-structure) structure containing a pointer to the file path containing the target data.

*SourceOptions*

[in] Reserved. Pass a [DELTA_INPUT](/previous-versions/bb417345(v=msdn.10)#delta-input-structure) structure with *Editable* set to **FALSE**, *lpStart* set to **NULL** and *uSize* set to 0.

*TargetOptions*

[in] Reserved. Pass a [DELTA_INPUT](/previous-versions/bb417345(v=msdn.10)#delta-input-structure) structure with *Editable* set to **FALSE**, *lpStart* set to **NULL** and *uSize* set to 0.

*GlobalOptions*

[in] Reserved. Pass a [DELTA_INPUT](/previous-versions/bb417345(v=msdn.10)#delta-input-structure) structure with *lpStart* set to **NULL** and *uSize* set to 0.

*lpTargetFileTime*

[in] The time stamp set on the target file after delta apply. If **NULL**, the target timestamp will be the current time during the create process.

*HashAlgId*

[in] ALG_ID of the algorithm to be used to generate the target signature. Some special values are:

- 0 = No signature
- 32 = 32-bit CRC defined in msdelta.dll

*lpDelta*

[out] Pointer to the [DELTA_OUTPUT](/previous-versions/bb417345(v=msdn.10)#delta-output-structure) structure where the delta is to be written.

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
