---
Description: 'A decorated symbol name includes characters that distinguish how a public symbol has been declared.'
ms.assetid: 'f02fa21d-3fe9-4838-a938-3136c34bc0e8'
title: Decorated Symbol Names
---

# Decorated Symbol Names

A decorated symbol name includes characters that distinguish how a public symbol has been declared. For \_\_stdcall functions, names include the "@" character and a decimal number that specifies the number of bytes in its function parameters. For example, the decorated name of the [**LoadLibrary**](base.loadlibrary) function is LoadLibrary@4. For C++ functions the name decoration is more complex and varies from compiler to compiler.

To retrieve the undecorated symbol name, use the [**UnDecorateSymbolName**](undecoratesymbolname.md) function. Alternatively, you can call the [**SymSetOptions**](symsetoptions.md) function to request that the symbol handler always present symbols with undecorated names. You must set this option before loading the symbols because the symbol handler creates the symbol name tables at load time.

 

 



