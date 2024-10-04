---
description: Enables a debugger to examine dynamic function table information.
ms.assetid: 32fd0dfd-ca7c-45e4-9d59-2b3318d7e13d
title: RtlGetFunctionTableListHead function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RtlGetFunctionTableListHead
api_type: 
- DllExport
api_location: 
- Ntdll.dll
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

Returns a pointer to the head of the function table linked list. Nodes in this list are of type [**DYNAMIC\_FUNCTION\_TABLE**](dynamic_function_table_type.md). A debugger can walk all the entries in this list to find all of the function tables in a target process.

## Remarks

Note that the Windows Driver Kit (WDK) header file Ntdef.h is required for some definitions. The associated import library, Ntdll.lib, is available in the WDK. You can also use the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Ntdll.dll.

## Requirements



| Requirement | Value |
|----------------|--------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ntdll.dll</dt> </dl> |



 

 
