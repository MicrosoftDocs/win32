---
Description: To conserve time and memory when working with many symbol files, use the SymSetOptions function to set the deferred symbol loading (SYMOPT\_DEFERRED\_LOADS) option.
ms.assetid: 40c9384f-00ed-40cd-9687-b76b69e74f87
title: Deferred Symbol Loading
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Deferred Symbol Loading

To conserve time and memory when working with many symbol files, use the [**SymSetOptions**](/windows/win32/Dbghelp/nf-dbghelp-symsetoptions?branch=master) function to set the deferred symbol loading (SYMOPT\_DEFERRED\_LOADS) option, then use the [**SymLoadModuleEx**](/windows/win32/Dbghelp/nf-dbghelp-symloadmoduleex?branch=master) or [**SymInitialize**](/windows/win32/Dbghelp/nf-dbghelp-syminitialize?branch=master) function to load symbols deferred for all modules. The symbol handler will list symbols that are available for the modules, but will not map the debug information into memory until it is requested. This is the preferred method to efficiently use debugging symbols. All functions that use symbols are affected by deferred symbol loading.

 

 



