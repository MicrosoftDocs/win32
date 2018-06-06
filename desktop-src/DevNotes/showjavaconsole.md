---
Description: The ShowJavaConsole function is a debugging aid for Java developers. Applets (or other Java code) running within Internet Explorer can use it to display error messages and other information.
ms.assetid: 070dd833-f8cc-403e-afbf-325648760d5f
title: ShowJavaConsole function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                       |
|----------------|---------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Msjava.dll</dt> </dl> |



 

 




