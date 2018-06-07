---
Description: The following functions are used in dynamic linking.
ms.assetid: 29e50bd5-1712-407f-bcb3-50a0a22ab8b5
title: Dynamic-Link Library Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Dynamic-Link Library Functions

The following functions are used in dynamic linking.



| Function                                                       | Description                                                                                                                                                    |
|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddDllDirectory**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-adddlldirectory)                     | Adds a directory to the process DLL search path.                                                                                                               |
| [**DisableThreadLibraryCalls**](https://www.bing.com/search?q=**DisableThreadLibraryCalls**) | Disables thread attach and thread detach notifications for the specified DLL.                                                                                  |
| [**DllMain**](dllmain.md)                                     | An optional entry point into a DLL.                                                                                                                            |
| [**FreeLibrary**](https://www.bing.com/search?q=**FreeLibrary**)                             | Decrements the reference count of the loaded DLL. When the reference count reaches zero, the module is unmapped from the address space of the calling process. |
| [**FreeLibraryAndExitThread**](https://www.bing.com/search?q=**FreeLibraryAndExitThread**)   | Decrements the reference count of a loaded DLL by one, and then calls [**ExitThread**](https://msdn.microsoft.com/library/windows/desktop/ms682659) to terminate the calling thread.                       |
| [**GetDllDirectory**](/windows/desktop/api/WinBase/nf-winbase-getdlldirectorya)                     | Retrieves the application-specific portion of the search path used to locate DLLs for the application.                                                         |
| [**GetModuleFileName**](https://www.bing.com/search?q=**GetModuleFileName**)                 | Retrieves the fully qualified path for the file containing the specified module.                                                                               |
| [**GetModuleFileNameEx**](https://msdn.microsoft.com/library/windows/desktop/ms683198)            | Retrieves the fully qualified path for the file containing the specified module.                                                                               |
| [**GetModuleHandle**](https://www.bing.com/search?q=**GetModuleHandle**)                     | Retrieves a module handle for the specified module.                                                                                                            |
| [**GetModuleHandleEx**](https://www.bing.com/search?q=**GetModuleHandleEx**)                 | Retrieves a module handle for the specified module.                                                                                                            |
| [**GetProcAddress**](https://www.bing.com/search?q=**GetProcAddress**)                       | Retrieves the address of an exported function or variable from the specified DLL.                                                                              |
| [**LoadLibrary**](https://www.bing.com/search?q=**LoadLibrary**)                             | Maps the specified executable module into the address space of the calling process.                                                                            |
| [**LoadLibraryEx**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa)                         | Maps the specified executable module into the address space of the calling process.                                                                            |
| [**LoadPackagedLibrary**](/windows/desktop/api/Winbase/nf-winbase-loadpackagedlibrary)             | Maps the specified packaged module and its dependencies into the address space of the calling process. Only Windows Store apps can call this function.         |
| [**RemoveDllDirectory**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-removedlldirectory)               | Removes a directory that was added to the process DLL search path by using [**AddDllDirectory**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-adddlldirectory).                                         |
| [**SetDefaultDllDirectories**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-setdefaultdlldirectories)   | Specifies a default set of directories to search when the calling process loads a DLL.                                                                         |
| [**SetDllDirectory**](/windows/desktop/api/Winbase/nf-winbase-setdlldirectorya)                     | Modifies the search path used to locate DLLs for the application.                                                                                              |



 

## Obsolete Functions

These functions are provided only for compatibility with 16-bit versions of Windows.

[**LoadModule**](/windows/desktop/api/Winbase/nf-winbase-loadmodule)

 

 



