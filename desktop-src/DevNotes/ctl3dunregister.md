---
description: Unregisters an application as a client of CTL3D.
ms.assetid: 21990A79-F90D-4AE1-AB02-2B33583B47F5
title: Ctl3dUnregister function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Ctl3dUnregister
api_type: 
- DllExport
api_location: 
- Ctl3d32.dll
---

# Ctl3dUnregister function

Unregisters an application as a client of CTL3D.

## Syntax


```C++
BOOL Ctl3dUnregister(
   HANDLE hinstApp
);
```



## Parameters

<dl> <dt>

*hinstApp* 
</dt> <dd>

A handle to the application to be unregistered as a client.

</dd> </dl>

## Return value

Returns **TRUE** if the application is unregistered as a client of CTL3D; otherwise, it returns **FALSE**.

## Remarks

An application that uses CTL3D should call this function in WinMain.

3D effects are not available on systems that have less than VGA resolution.

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ctl3d32.dll</dt> </dl> |



 

 
