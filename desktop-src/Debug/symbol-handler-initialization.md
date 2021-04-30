---
description: The symbol handler is designed to track various sets of symbol files.
ms.assetid: 1bd7ac25-e46d-442b-b365-52edcd8bf922
title: Symbol Handler Initialization
ms.topic: article
ms.date: 05/31/2018
---

# Symbol Handler Initialization

The symbol handler is designed to track various sets of symbol files.

To initialize the symbol handler, call the [**SymInitialize**](/windows/desktop/api/Dbghelp/nf-dbghelp-syminitialize) function. The *hProcess* parameter can be a unique arbitrary number, a value returned from the [**GetCurrentProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentprocess) function, or the identifier of any running process. The *fInvadeProcess* parameter indicates whether the symbol handler should enumerate the modules loaded by the process and load symbols for each of its modules. If *fInvadeProcess* is **TRUE**, the *hProcess* parameter must be the value returned from **GetCurrentProcess** or the identifier of an existing process. To refresh this list, use the [**SymRefreshModuleList**](/windows/desktop/api/Dbghelp/nf-dbghelp-symrefreshmodulelist) function.

Using *fInvadeProcess* is a simple way to load all symbol files for a process. However, the symbol handler will not attempt to load symbols for modules subsequently loaded by the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) function. You must use the [**SymLoadModuleEx**](/windows/desktop/api/Dbghelp/nf-dbghelp-symloadmoduleex) function in this case.

 

 
