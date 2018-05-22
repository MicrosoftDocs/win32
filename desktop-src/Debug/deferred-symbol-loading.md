---
Description: 'To conserve time and memory when working with many symbol files, use the SymSetOptions function to set the deferred symbol loading (SYMOPT\_DEFERRED\_LOADS) option.'
ms.assetid: '40c9384f-00ed-40cd-9687-b76b69e74f87'
title: Deferred Symbol Loading
---

# Deferred Symbol Loading

To conserve time and memory when working with many symbol files, use the [**SymSetOptions**](symsetoptions.md) function to set the deferred symbol loading (SYMOPT\_DEFERRED\_LOADS) option, then use the [**SymLoadModuleEx**](symloadmoduleex.md) or [**SymInitialize**](syminitialize.md) function to load symbols deferred for all modules. The symbol handler will list symbols that are available for the modules, but will not map the debug information into memory until it is requested. This is the preferred method to efficiently use debugging symbols. All functions that use symbols are affected by deferred symbol loading.

 

 



