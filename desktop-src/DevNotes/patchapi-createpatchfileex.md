---
description: Creates a delta between the specified source file and the specified target file.
title: CreatePatchFileExA/W function
ms.topic: reference
ms.date: 04/17/2020
ms.keywords: CreatePatchFileExA, CreatePatchFileExW
req.header: patchapi.h
req.dll: mspatchc.dll
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CreatePatchFileExW
api_type: 
- DllExport
api_location: 
- mspatchc.dll
---

# CreatePatchFileExA/W function

The **CreatePatchFileExA** and **CreatePatchFileExW** functions create a delta between the specified source file and the specified target file. Both the source and the target files are provided as paths. The output delta is also written to a provided path. These functions provide progress reporting during the create process.

## Syntax

```cpp
BOOL  PATCHAPI  CreatePatchFileExA(
    ULONG                     OldFileCount,
    PPATCH_OLD_FILE_INFO_A    OldFileInfoArray,
    LPCTSTR                   NewFileName,
    LPCTSTR                   PatchFileName,
    ULONG                     OptionFlags,
    PPATCH_OPTION_DATA        OptionData,
    PPATCH_PROGRESS_CALLBACK  ProgressCallback,
    PVOID                     CallbackContext
    );

BOOL  PATCHAPI  CreatePatchFileExW(
    ULONG                     OldFileCount,
    PPATCH_OLD_FILE_INFO_A    OldFileInfoArray,
    LPCWSTR                   NewFileName,
    LPCWSTR                   PatchFileName,
    ULONG                     OptionFlags,
    PPATCH_OPTION_DATA        OptionData,
    PPATCH_PROGRESS_CALLBACK  ProgressCallback,
    PVOID                     CallbackContext
    );
```

## Parameters

*OldFileCount*

The total number of source files. Used to create deltas against multiple source files (maximum 255).

*OldFileInfoArray*

Pointer to source file information array.

*NewFileName*

The name of the target file.

*PatchFileName*

The name of the delta that is created.

*OptionFlags*

Creation flags.

*ProgressCallback*

Pointer to application-defined progress callback.

*CallbackContext*

Pointer to application-defined context.

## Return value

This function returns **TRUE** if it succeeds; otherwise, it returns **FALSE**.

## Requirements

| Requirement | Value |
|----------------|---------------------------------------------------------------------------------------|
| Header | patchapi.h |
| DLL | mspatchc.dll |
| Unicode | Implemented as CreatePatchFileExW (Unicode) and CreatePatchFileExA (ANSI) |

## See also

[PatchAPI](patchapi.md)
