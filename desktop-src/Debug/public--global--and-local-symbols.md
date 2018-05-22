---
Description: 'The symbol handling capabilities of the DbgHelp API have evolved over the years.'
ms.assetid: '6dc41682-6104-418b-b045-7afe8c2b11e9'
title: 'Public, Global, and Local Symbols'
---

# Public, Global, and Local Symbols

The symbol handling capabilities of the DbgHelp API have evolved over the years. To ensure that your code works in a variety of scenarios and provides full details on the symbols, use the newest functions whenever possible. For example, [**SymEnumSymbols**](symenumsymbols.md) replaces [**SymEnumerateSymbols64**](symenumeratesymbols64.md), [**SymFromName**](symfromname.md) replaces [**SymGetSymFromName64**](symgetsymfromname64.md), and [**SymFromAddr**](symfromaddr.md) replaces [**SymGetSymFromAddr64**](symgetsymfromaddr64.md).

## Public Symbols

Initial versions of DbgHelp.dll supported examining only public symbols. These symbols are generated for any item in the code that must be exposed between different source files. They also include all items that are exported out of the module.

The symbols are either embedded in the image, or stored separately in a .dbg or .pdb file. The only information stored is the symbol name and address. The names are available as decorated names. To view undecorated names, call the [**SymSetOptions**](symsetoptions.md) function with SYMOPT\_UNDNAME, or use the [**UnDecorateSymbolName**](undecoratesymbolname.md) function.

Note that the DbgHelp API was not initially designed to support multiple instances of the same symbol within a module. This is because public symbols are restricted to unique names within a module. Therefore, [**SymGetSymFromName64**](symgetsymfromname64.md) returns only the first symbol that matches. To retrieve all symbols that match, call [**SymEnumSymbols**](symenumsymbols.md).

## Global and Local Symbols

Newer versions of DbgHelp.dll support global and local symbols when using .pdb files. These new versions include static functions, functions scoped within a source file, function parameters, and local variables. When DbgHelp searches for a symbol, it checks the global and local symbol tables before checking the public symbol table. This is because there is more information available for these types of symbols than is available for public symbols.

Global and local symbols are stored with undecorated names. Therefore, the SYMOPT\_UNDNAME flag has no effect. To get decorated symbol names, you must use the SYMOPT\_PUBLICS\_ONLY flag. This causes DbgHelp to search only the public symbols.

To view local symbols or function parameters, call the [**SymSetContext**](symsetcontext.md) function with the **InstructionOffset** member of the [**IMAGEHLP\_STACK\_FRAME**](imagehlp-stack-frame-str.md) structure set to the address of any function symbol. Subsequent calls to [**SymFromName**](symfromname.md) and [**SymEnumSymbols**](symenumsymbols.md) can operate within the context of this address. To do so, set the *BaseOfDll* parameter to **NULL** and omit the module specifier from the *Name* or *Mask* parameter. This forces DbgHelp to search for matching symbols within the scope indicated by **SymSetContext**.

To determine if a symbol is a parameter, check the **Flags** member of the [**SYMBOL\_INFO**](symbol-info-str.md) structure. If the symbol is a parameter, the member contains SYMFLAG\_PARAMETER. If it is a local symbol, the member contains SYMFLAG\_LOCAL.

 

 



