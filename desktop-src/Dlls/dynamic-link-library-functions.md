---
Description: 'The following functions are used in dynamic linking.'
ms.assetid: '29e50bd5-1712-407f-bcb3-50a0a22ab8b5'
title: 'Dynamic-Link Library Functions'
---

# Dynamic-Link Library Functions

The following functions are used in dynamic linking.



| Function                                                       | Description                                                                                                                                                    |
|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddDllDirectory**](adddlldirectory.md)                     | Adds a directory to the process DLL search path.                                                                                                               |
| [**DisableThreadLibraryCalls**](disablethreadlibrarycalls.md) | Disables thread attach and thread detach notifications for the specified DLL.                                                                                  |
| [**DllMain**](dllmain.md)                                     | An optional entry point into a DLL.                                                                                                                            |
| [**FreeLibrary**](freelibrary.md)                             | Decrements the reference count of the loaded DLL. When the reference count reaches zero, the module is unmapped from the address space of the calling process. |
| [**FreeLibraryAndExitThread**](freelibraryandexitthread.md)   | Decrements the reference count of a loaded DLL by one, and then calls [**ExitThread**](https://msdn.microsoft.com/library/windows/desktop/ms682659) to terminate the calling thread.                       |
| [**GetDllDirectory**](getdlldirectory.md)                     | Retrieves the application-specific portion of the search path used to locate DLLs for the application.                                                         |
| [**GetModuleFileName**](getmodulefilename.md)                 | Retrieves the fully qualified path for the file containing the specified module.                                                                               |
| [**GetModuleFileNameEx**](https://msdn.microsoft.com/library/windows/desktop/ms683198)            | Retrieves the fully qualified path for the file containing the specified module.                                                                               |
| [**GetModuleHandle**](getmodulehandle.md)                     | Retrieves a module handle for the specified module.                                                                                                            |
| [**GetModuleHandleEx**](getmodulehandleex.md)                 | Retrieves a module handle for the specified module.                                                                                                            |
| [**GetProcAddress**](getprocaddress.md)                       | Retrieves the address of an exported function or variable from the specified DLL.                                                                              |
| [**LoadLibrary**](loadlibrary.md)                             | Maps the specified executable module into the address space of the calling process.                                                                            |
| [**LoadLibraryEx**](loadlibraryex.md)                         | Maps the specified executable module into the address space of the calling process.                                                                            |
| [**LoadPackagedLibrary**](loadpackagedlibrary.md)             | Maps the specified packaged module and its dependencies into the address space of the calling process. Only Windows Store apps can call this function.         |
| [**RemoveDllDirectory**](removedlldirectory.md)               | Removes a directory that was added to the process DLL search path by using [**AddDllDirectory**](adddlldirectory.md).                                         |
| [**SetDefaultDllDirectories**](setdefaultdlldirectories.md)   | Specifies a default set of directories to search when the calling process loads a DLL.                                                                         |
| [**SetDllDirectory**](setdlldirectory.md)                     | Modifies the search path used to locate DLLs for the application.                                                                                              |



 

## Obsolete Functions

These functions are provided only for compatibility with 16-bit versions of Windows.

[**LoadModule**](loadmodule.md)

 

 



