---
description: Examines the Dos format file name and determines if it is a Dos device name.
title: RtlIsDosDeviceName_U function
ms.topic: reference
ms.date: 08/30/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RtlIsDosDeviceName_U
api_type: 
- DllExport
api_location: 
- ntdll.dll
---

# RtlIsDosDeviceName_U function

Examines the Dos format file name and determines if it is a Dos device name.

## Syntax


```C++
ULONG RtlIsDosDeviceName_U(
    __in PCWSTR DosFileName
)
```

## Parameters

### isProcessorMode

A Boolean pointer provided by the calling application. After successful execution, this variable will indicate whether the OS is in processor mode or controller mode.

## Return value

| Value | Description |
|-------|-------------|
| 0 | Specified Dos file name is not the name of a Dos device. |
| > 0 | Specified Dos file name is the name of a Dos device and the return value is a ULONG where the high order 16 bits is the offset in the input buffer where the dos device name beings and the low order 16 bits is the length of the device name the length of the name (excluding any optional trailing colon). |

## Remarks

Valid Dos device names are:

- LPTn
- COMn
- PRN
- AUX
- NUL
- CON
- CONIN$
- CONOUT$

When n is a digit.  Trailing colon is ignored if present.


This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions. The API is exported from ntdll.dll.



## Requirements

| Requirement | Value |
|-----------------------------------|-------------------------------------------------------------------------------------------------------|
| DLL                   | ntdll.dll              |




 
