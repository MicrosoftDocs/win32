---
description: To free all the memory used by the symbol handler for a process, use the SymCleanup function.
ms.assetid: d442b2f2-9225-43fd-bd25-274322857834
title: Symbol Handler Cleanup
ms.topic: article
ms.date: 05/31/2018
---

# Symbol Handler Cleanup

To free all the memory used by the symbol handler for a process, use the [**SymCleanup**](/windows/desktop/api/Dbghelp/nf-dbghelp-symcleanup) function. This function enumerates all loaded modules, frees each module, and frees the memory allocated for the list of modules. After you call **SymCleanup**, you cannot use the process handle in the symbol handling functions until you call the [**SymInitialize**](/windows/desktop/api/Dbghelp/nf-dbghelp-syminitialize) function.

 

 



