---
description: The DeleteExtractedFiles function deletes the files that were extracted by the Extract function.
ms.assetid: 253e6267-d4be-46d6-bad2-2eb20bbc7e33
title: DeleteExtractedFiles function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DeleteExtractedFiles
api_type: 
- DllExport
api_location: 
- Cabinet.dll
---

# DeleteExtractedFiles function

\[This function is no longer supported, so its behavior cannot be guaranteed.\]

The **DeleteExtractedFiles** function deletes the files that were extracted by the [**Extract**](extract.md) function.

## Syntax


```C++
VOID WINAPI DeleteExtractedFiles(
   PSESSION ps
);
```



## Parameters

<dl> <dt>

*ps* 
</dt> <dd>

A pointer to a [**SESSION**](session.md) structure that contains information about the current session.

This function frees the memory in the **pFileList** member of this structure and sets **pFileList** to **NULL**.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Cabinet.dll</dt> </dl> |



## See also

<dl> <dt>

[**Extract**](extract.md)
</dt> <dt>

[**SESSION**](session.md)
</dt> </dl>

 

 
