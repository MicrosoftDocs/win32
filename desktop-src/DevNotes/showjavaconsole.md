---
description: The ShowJavaConsole function is a debugging aid for Java developers. Applets (or other Java code) running within Internet Explorer can use it to display error messages and other information.
ms.assetid: 070dd833-f8cc-403e-afbf-325648760d5f
title: ShowJavaConsole function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- extern
api_type: 
- DllExport
api_location: 
- Msjava.dll
---

# ShowJavaConsole function

The **ShowJavaConsole** function is a debugging aid for Java developers. Applets (or other Java code) running within Internet Explorer can use it to display error messages and other information.

## Syntax


```C++
void extern ShowJavaConsole(void);
```



## Parameters

This function has no parameters.

<dl></dl>

## Return value

This function does not return a value.

## Remarks

Calling **ShowJavaConsole** causes the Java virtual machine (VM) to display the Java console window. The Java console window itself can display debugging output from Java code running in the calling process. Typically, this would be used only by an application hosting the Java VM. There is only a single Java console window per process; multiple calls to the API result in the same window being displayed. In other words, if the console window is already displayed, nothing happens; if the window has not been displayed, or the user has closed it, then the window pops up.

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|---------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Msjava.dll</dt> </dl> |



 

 
