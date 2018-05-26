---
Description: A decorated symbol name includes characters that distinguish how a public symbol has been declared.
ms.assetid: f02fa21d-3fe9-4838-a938-3136c34bc0e8
title: Decorated Symbol Names
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Decorated Symbol Names

A decorated symbol name includes characters that distinguish how a public symbol has been declared. For \_\_stdcall functions, names include the "@" character and a decimal number that specifies the number of bytes in its function parameters. For example, the decorated name of the [**LoadLibrary**](base.loadlibrary) function is LoadLibrary@4. For C++ functions the name decoration is more complex and varies from compiler to compiler.

To retrieve the undecorated symbol name, use the [**UnDecorateSymbolName**](/windows/win32/Dbghelp/nf-dbghelp-undecoratesymbolname?branch=master) function. Alternatively, you can call the [**SymSetOptions**](/windows/win32/Dbghelp/nf-dbghelp-symsetoptions?branch=master) function to request that the symbol handler always present symbols with undecorated names. You must set this option before loading the symbols because the symbol handler creates the symbol name tables at load time.

 

 



