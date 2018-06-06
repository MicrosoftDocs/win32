---
Description: Unregisters an application as a client of CTL3D.
ms.assetid: 21990A79-F90D-4AE1-AB02-2B33583B47F5
title: Ctl3dUnregister function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                        |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ctl3d32.dll</dt> </dl> |



 

 




