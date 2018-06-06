---
Description: Enables a debugger to examine dynamic function table information.
ms.assetid: 32fd0dfd-ca7c-45e4-9d59-2b3318d7e13d
title: RtlGetFunctionTableListHead function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RtlGetFunctionTableListHead function

\[This function may be changed or removed from Windows without further notice.\]

Enables a debugger to examine dynamic function table information.

## Syntax


```C++
PLIST_ENTRY RtlGetFunctionTableListHead(void);
```



## Parameters

This function has no parameters.

## Return value

Returns a pointer to the head of the function table list.

## Remarks

Note that the Windows Driver Kit (WDK) header file Ntdef.h is required for some definitions. The associated import library, Ntdll.lib, is available in the WDK. You can also use the [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) functions to dynamically link to Ntdll.dll.

## Requirements



|                |                                                                                      |
|----------------|--------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ntdll.dll</dt> </dl> |



 

 




