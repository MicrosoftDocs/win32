---
description: Returns whether a specified file is local, on a network share, or on removeable media.
title: DlpGetFileLocation function (endpointdlp.h)
ms.topic: reference
ms.date: 06/14/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpGetFileLocation
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# DlpGetFileLocation function

Returns whether a specified file is local, on a network share, or on removeable media.

## Syntax

```C++
FileLocation WINAPI DlpGetFileLocation(_In_z_ LPCWSTR destinationFilePath);
```

## Parameters

`destinationFilePath` [in]: A [fully qualified Win32 file path](https://docs.microsoft.com/windows/win32/fileio/naming-a-file) for the file to be analyzed.

## Return value

Returns the `FileLocation` of the destination file path.

## Remarks

This function can be called from multiple threads.

## Requirements


| Requirement          |    Value                   |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11, version 22H2 (10.0; Build 22621)           |
| DLL<br/>                      | EndpointDlp.dll |