---
description: Extracts the header information from a delta.
title: ExtractPatchHeaderToFileA/W function
ms.topic: reference
ms.date: 04/17/2020
ms.keywords: ExtractPatchHeaderToFileA, ExtractPatchHeaderToFileW
req.header: patchapi.h
req.dll: mspatchc.dll
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ExtractPatchHeaderToFileW
api_type: 
- DllExport
api_location: 
- mspatchc.dll
---

# ExtractPatchHeaderToFileA/W function

The **ExtractPatchHeaderToFileA** and **ExtractPatchHeaderToFileW** functions extract the header information from a delta. The delta is provided as a file path. The output header is also written to a provided path.

## Syntax

```cpp
BOOL  PATCHAPI  ExtractPatchHeaderToFileA(
    LPCTSTR  PatchFileName,
    LPCTSTR  PatchHeaderFileName
    );

BOOL  PATCHAPI  ExtractPatchHeaderToFileW(
    LPCWSTR  PatchFileName,
    LPCWSTR  PatchHeaderFileName
    );
```

## Parameters

*PatchFileName*

The name of the delta containing the header.

*PatchHeaderFileName*

The name of the header file that is to be created.

## Return value

This function returns **TRUE** if it succeeds; otherwise, it returns **FALSE**.

## Requirements

| Requirement | Value |
|----------------|---------------------------------------------------------------------------------------|
| Header | patchapi.h |
| DLL | mspatchc.dll |
| Unicode | Implemented as ExtractPatchHeaderToFileW (Unicode) and ExtractPatchHeaderToFileA (ANSI) |

## See also

[PatchAPI](patchapi.md)
