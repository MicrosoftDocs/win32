---
Description: Registers an application as a client of CTL3D.
ms.assetid: 38a4a04a-6322-4eb8-b272-ae9b90f84e0f
title: Ctl3dRegister function
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Ctl3dRegister
api_type: 
- DllExport
api_location: 
- Ctl3d32.dll
---

# Ctl3dRegister function

Registers an application as a client of CTL3D.

## Syntax


```C++
BOOL Ctl3dRegister(
   HANDLE hinstApp
);
```



## Parameters

<dl> <dt>

*hinstApp* 
</dt> <dd>

A handle to the application to be registered as a client.

</dd> </dl>

## Return value

Returns **TRUE** if 3D effects are active; otherwise, it returns **FALSE**.

## Remarks

An application that uses CTL3D should call this function in WinMain.

3D effects are not available on systems that have less than VGA resolution.

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions.

## Requirements



|                |                                                                                        |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ctl3d32.dll</dt> </dl> |



 

 




