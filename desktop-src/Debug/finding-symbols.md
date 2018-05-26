---
Description: After a symbol file has been loaded into the symbol handler, an application can use the symbol locator functions to return symbol information for a specified address.
ms.assetid: bfc068e1-eced-4ab2-80a3-acc2ed07c841
title: Finding Symbols
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Finding Symbols

After a symbol file has been loaded into the symbol handler, an application can use the symbol locator functions to return symbol information for a specified address. These functions can also find a source code file name and line number location for an address.

## Enumerating Symbol Files

To retrieve a list of all symbol files loaded by module name, call the [**SymEnumerateModules64**](/windows/win32/Dbghelp/nf-dbghelp-symenumeratemodules?branch=master) function. For an example, see [Enumerating Symbol Modules](enumerating-symbol-modules.md). To retrieve a list of symbols for a given module, call the [**SymEnumSymbols**](/windows/win32/Dbghelp/nf-dbghelp-symenumsymbols?branch=master) function. For an example, see [Enumerating Symbols](enumerating-symbols.md).

## Retrieving Symbols by Address

To retrieve symbolic information for a specific address, use the [**SymFromAddr**](/windows/win32/Dbghelp/nf-dbghelp-symfromaddr?branch=master) function. This function retrieves information and stores it in a [**SYMBOL\_INFO**](/windows/win32/DbgHelp/ns-dbghelp-_symbol_info?branch=master) structure. Because symbol names are variable in length, you must provide additional buffer space following the **SYMBOL\_INFO** structure declaration. For an example, see [Retrieving Symbol Information by Address](retrieving-symbol-information-by-address.md).

Note that the address does not need to be on a symbol boundary. If the address comes after the beginning of a symbol but before the end of the symbol (the beginning of the symbol plus the symbol size), the function will locate the symbol.

## Retrieving Symbols by Symbol Name

To retrieve symbolic information in a [**SYMBOL\_INFO**](/windows/win32/DbgHelp/ns-dbghelp-_symbol_info?branch=master) structure for a specific module and symbol name, use the [**SymFromName**](/windows/win32/Dbghelp/nf-dbghelp-symfromname?branch=master) function. If deferred symbol loading is set, **SymFromName** will attempt to load the symbol file for a module if it has not already been loaded. To specify a module name along with a symbol name, use the syntax *Module*!*SymName*. The "!" character delimits the module name from the symbol name. For an example, see [Retrieving Symbol Information by Name](retrieving-symbol-information-by-name.md).

## Retrieving Line Numbers by Address

To retrieve the source code location for a specific address, use the [**SymGetLineFromAddr64**](/windows/win32/Dbghelp/nf-dbghelp-symgetlinefromaddr?branch=master) function. This function fills an [**IMAGEHLP\_LINE64**](/windows/win32/DbgHelp/ns-dbghelp-_imagehlp_line?branch=master) structure that includes the source file name and line number location referred to by the specified address. For an example, see [Retrieving Symbol Information by Address](retrieving-symbol-information-by-address.md).

## Retrieving Line Numbers by Symbol Name

To retrieve source code location for a specific symbol name, use the [**SymGetLineFromName64**](/windows/win32/Dbghelp/nf-dbghelp-symgetlinefromname?branch=master) function. This function is similar to [**SymGetSymFromName64**](/windows/win32/Dbghelp/nf-dbghelp-symgetsymfromname?branch=master), but retrieves an [**IMAGEHLP\_LINE64**](/windows/win32/DbgHelp/ns-dbghelp-_imagehlp_line?branch=master) structure. To use [**SymGetLineFromAddr64**](/windows/win32/Dbghelp/nf-dbghelp-symgetlinefromaddr?branch=master) or **SymGetLineFromName64**, you must set the load lines option (SYMOPT\_LOAD\_LINES) using the [**SymSetOptions**](/windows/win32/Dbghelp/nf-dbghelp-symsetoptions?branch=master) function. For an example, see [Retrieving Symbol Information by Name](retrieving-symbol-information-by-name.md).

 

 



