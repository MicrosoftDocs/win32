---
description: Verifies whether the operating system is in processor mode or controller mode.
title: TelIsOsInProcessorMode function
ms.topic: reference
ms.date: 06/08/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TelIsOsInProcessorMode
api_type: 
- DllExport
api_location: 
- DiagnosticDatasettings.dll
---

# TelIsOsInProcessorMode function

Verifies whether the operating system is in processor mode or controller mode.

## Syntax


```C++
HRESULT WINAPI TelIsOsInProcessorMode(
    _Out_ BOOL* isProcessorMode)
```

## Parameters

### isProcessorMode

A Boolean pointer provided by the calling application. After successful execution, this variable will indicate whether the OS is in processor mode or controller mode.

## Return value

An HRESULT.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions. The API is exported from DiagnosticDatasettings.dll.

This API is supported on Enterprise, Professional, and Education SKUs starting with Windows 11 build 22000. The API was introduced in [KB5019274](https://support.microsoft.com/topic/january-19-2023-kb5019274-os-build-22000-1516-preview-ace2511d-586e-41b0-b213-3a89d97565a4).

## Requirements

| Requirement | Value |
|-----------------------------------|-------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11 build 22000                                             |
| DLL                   | DiagnosticDatasettings.dll              |




 
