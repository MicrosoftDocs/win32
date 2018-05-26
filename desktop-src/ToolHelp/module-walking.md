---
title: Module Walking
description: A snapshot that includes the module list for a specified process contains information about each module, executable file, or dynamic-link library (DLL), used by the specified process.
ms.assetid: 1b539e2f-1326-42aa-af58-ffd7e2833b9b
keywords:
- dynamic-link libraries
- dynamic-link libraries,enumerating DLLs
- enumerating
- enumerating,DLLs
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Module Walking

A snapshot that includes the module list for a specified process contains information about each module, executable file, or dynamic-link library (DLL), used by the specified process. You can retrieve information for the first module in the list by using the [**Module32First**](/windows/win32/TlHelp32/nf-tlhelp32-module32first?branch=master) function. After retrieving the first module in the list, you can retrieve information for subsequent modules in the list by using the [**Module32Next**](/windows/win32/TlHelp32/nf-tlhelp32-module32next?branch=master) function. **Module32First** and **Module32Next** fill a [**MODULEENTRY32**](/windows/win32/TlHelp32/ns-tlhelp32-tagmoduleentry32?branch=master) structure with information about the module.

You can retrieve an extended error status code for [**Module32First**](/windows/win32/TlHelp32/nf-tlhelp32-module32first?branch=master) and [**Module32Next**](/windows/win32/TlHelp32/nf-tlhelp32-module32next?branch=master) by using the [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) function.

> [!Note]  
> The module identifier, which is specified in the **th32ModuleID** member of [**MODULEENTRY32**](/windows/win32/TlHelp32/ns-tlhelp32-tagmoduleentry32?branch=master), only has meaning in 16-bit Windows.

 

## Related topics

<dl> <dt>

[Traversing the Module List](traversing-the-module-list.md)
</dt> </dl>

 

 




