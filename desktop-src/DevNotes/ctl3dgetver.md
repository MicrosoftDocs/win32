---
description: Indicates the version of CTL3D that is currently running.
ms.assetid: 38c0842c-417f-4ca1-acc2-3bbadf45c804
title: Ctl3dGetVer function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Ctl3dGetVer
api_type: 
- DllExport
api_location: 
- Ctl3d32.dll
---

# Ctl3dGetVer function

Indicates the version of CTL3D that is currently running.

## Syntax


```C++
WORD Ctl3dGetVer(void);
```



## Parameters

This function has no parameters.

## Return value

Returns a value that contains the major version number in the high-order byte and the minor version number in the low-order byte.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ctl3d32.dll</dt> </dl> |



 

 
