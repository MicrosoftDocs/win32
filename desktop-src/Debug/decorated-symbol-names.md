---
description: A decorated symbol name includes characters that distinguish how a public symbol has been declared.
ms.assetid: f02fa21d-3fe9-4838-a938-3136c34bc0e8
title: Decorated Symbol Names
ms.topic: article
ms.date: 05/31/2018
---

# Decorated Symbol Names

A decorated symbol name includes characters that distinguish how a public symbol has been declared. For \_\_stdcall functions, names include the "@" character and a decimal number that specifies the number of bytes in its function parameters. For example, the decorated name of the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) function is LoadLibrary@4. For C++ functions the name decoration is more complex and varies from compiler to compiler.

To retrieve the undecorated symbol name, use the [**UnDecorateSymbolName**](/windows/desktop/api/Dbghelp/nf-dbghelp-undecoratesymbolname) function. Alternatively, you can call the [**SymSetOptions**](/windows/desktop/api/Dbghelp/nf-dbghelp-symsetoptions) function to request that the symbol handler always present symbols with undecorated names. You must set this option before loading the symbols because the symbol handler creates the symbol name tables at load time.

 

 
