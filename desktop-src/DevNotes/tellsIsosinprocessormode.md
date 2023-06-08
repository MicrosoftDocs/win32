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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions. The API is exported from DiagnosticDatasettings.dll

## Requirements

| Requirement | Value |
|-----------------------------------|-------------------------------------------------------------------------------------------------------|
| DLL                   | DiagnosticDatasettings.dll              |



 

 
