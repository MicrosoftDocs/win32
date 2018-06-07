---
Description: Automatically subclasses and adds 3D effects to all dialog boxes in the application.
ms.assetid: 96555052-c564-4cc7-9b24-e527f8e2f879
title: Ctl3dAutoSubclass function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Ctl3dAutoSubclass function

Automatically subclasses and adds 3D effects to all dialog boxes in the application.

## Syntax


```C++
PUBLIC BOOL FAR PASCAL Ctl3dAutoSubclass(
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

Returns **TRUE** unless one of the following conditions exists, in which case it returns **FALSE**:

-   CTL3D is running under Windows version 3.0 or earlier.
-   CTL3D does not have space available in its tables for the current application. CTL3D can service up to 32 applications at the same time.
-   CTL3D cannot install its CBT hook.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                        |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ctl3d32.dll</dt> </dl> |



 

 




