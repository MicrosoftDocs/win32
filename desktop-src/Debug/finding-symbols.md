---
description: After a symbol file has been loaded into the symbol handler, an application can use the symbol locator functions to return symbol information for a specified address.
ms.assetid: bfc068e1-eced-4ab2-80a3-acc2ed07c841
title: Finding Symbols
ms.topic: article
ms.date: 05/31/2018
---

# Finding Symbols

After a symbol file has been loaded into the symbol handler, an application can use the symbol locator functions to return symbol information for a specified address. These functions can also find a source code file name and line number location for an address.

## Enumerating Symbol Files

To retrieve a list of all symbol files loaded by module name, call the [**SymEnumerateModules64**](/windows/desktop/api/Dbghelp/nf-dbghelp-symenumeratemodules) function. For an example, see [Enumerating Symbol Modules](enumerating-symbol-modules.md). To retrieve a list of symbols for a given module, call the [**SymEnumSymbols**](/windows/desktop/api/Dbghelp/nf-dbghelp-symenumsymbols) function. For an example, see [Enumerating Symbols](enumerating-symbols.md).

## Retrieving Symbols by Address

To retrieve symbolic information for a specific address, use the [**SymFromAddr**](/windows/desktop/api/Dbghelp/nf-dbghelp-symfromaddr) function. This function retrieves information and stores it in a [**SYMBOL\_INFO**](/windows/desktop/api/DbgHelp/ns-dbghelp-symbol_info) structure. Because symbol names are variable in length, you must provide additional buffer space following the **SYMBOL\_INFO** structure declaration. For an example, see [Retrieving Symbol Information by Address](retrieving-symbol-information-by-address.md).

Note that the address does not need to be on a symbol boundary. If the address comes after the beginning of a symbol but before the end of the symbol (the beginning of the symbol plus the symbol size), the function will locate the symbol.

## Retrieving Symbols by Symbol Name

To retrieve symbolic information in a [**SYMBOL\_INFO**](/windows/desktop/api/DbgHelp/ns-dbghelp-symbol_info) structure for a specific module and symbol name, use the [**SymFromName**](/windows/desktop/api/Dbghelp/nf-dbghelp-symfromname) function. If deferred symbol loading is set, **SymFromName** will attempt to load the symbol file for a module if it has not already been loaded. To specify a module name along with a symbol name, use the syntax *Module*!*SymName*. The "!" character delimits the module name from the symbol name. For an example, see [Retrieving Symbol Information by Name](retrieving-symbol-information-by-name.md).

## Retrieving Line Numbers by Address

To retrieve the source code location for a specific address, use the [**SymGetLineFromAddr64**](/windows/desktop/api/Dbghelp/nf-dbghelp-symgetlinefromaddr) function. This function fills an [**IMAGEHLP\_LINE64**](/windows/desktop/api/DbgHelp/ns-dbghelp-imagehlp_line) structure that includes the source file name and line number location referred to by the specified address. For an example, see [Retrieving Symbol Information by Address](retrieving-symbol-information-by-address.md).

## Retrieving Line Numbers by Symbol Name

To retrieve source code location for a specific symbol name, use the [**SymGetLineFromName64**](/windows/desktop/api/Dbghelp/nf-dbghelp-symgetlinefromname) function. This function is similar to [**SymGetSymFromName64**](/windows/desktop/api/Dbghelp/nf-dbghelp-symgetsymfromname), but retrieves an [**IMAGEHLP\_LINE64**](/windows/desktop/api/DbgHelp/ns-dbghelp-imagehlp_line) structure. To use [**SymGetLineFromAddr64**](/windows/desktop/api/Dbghelp/nf-dbghelp-symgetlinefromaddr) or **SymGetLineFromName64**, you must set the load lines option (SYMOPT\_LOAD\_LINES) using the [**SymSetOptions**](/windows/desktop/api/Dbghelp/nf-dbghelp-symsetoptions) function. For an example, see [Retrieving Symbol Information by Name](retrieving-symbol-information-by-name.md).

 

 



