---
Description: Enables a debugger to examine dynamic function table information.
ms.assetid: 32fd0dfd-ca7c-45e4-9d59-2b3318d7e13d
title: RtlGetFunctionTableListHead function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

Note that the Windows Driver Kit (WDK) header file Ntdef.h is required for some definitions. The associated import library, Ntdll.lib, is available in the WDK. You can also use the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions to dynamically link to Ntdll.dll.

## Requirements



|                |                                                                                      |
|----------------|--------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ntdll.dll</dt> </dl> |



 

 




