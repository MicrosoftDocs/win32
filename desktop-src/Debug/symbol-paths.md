---
description: The DbgHelp library uses the symbol search path to locate debug symbols (.pdb and .dbg files). The search path can be made up of one or more path elements separated by semicolons.
ms.assetid: 3527f589-285b-4cdf-b024-17920971a904
title: Symbol Paths
ms.topic: article
ms.date: 05/31/2018
---

# Symbol Paths

The DbgHelp library uses the symbol search path to locate debug symbols (.pdb and .dbg files). The search path can be made up of one or more path elements separated by semicolons.

## Specifying Search Paths

To specify where the symbol handler will search disk directories for symbol files, call the [**SymSetSearchPath**](/windows/desktop/api/Dbghelp/nf-dbghelp-symsetsearchpath) function. Alternatively, you can specify a symbol search path in the *UserSearchPath* parameter of the [**SymInitialize**](/windows/desktop/api/Dbghelp/nf-dbghelp-syminitialize) function.

The *UserSearchPath* parameter in [**SymInitialize**](/windows/desktop/api/Dbghelp/nf-dbghelp-syminitialize) and the *SearchPath* parameter in [**SymSetSearchPath**](/windows/desktop/api/Dbghelp/nf-dbghelp-symsetsearchpath) take a pointer to a null-terminated string that specifies a path, or series of paths separated by a semicolon. The symbol handler uses these paths to search for symbol files. If this parameter is **NULL**, the symbol handler searches the directory that contains the module for which symbols are being searched. Otherwise, if this parameter is specified as a non-**NULL** value, the symbol handler first searches the paths set by the application before searching the module directory. If you set the \_NT\_SYMBOL\_PATH or \_NT\_ALT\_SYMBOL\_PATH environment variable, the symbol handler searches for symbol files in the following order:

1. The \_NT\_SYMBOL\_PATH environment variable.
2. The \_NT\_ALT\_SYMBOL\_PATH environment variable.
3. The directory that contains the corresponding module.

To retrieve the search paths, call the [**SymGetSearchPath**](/windows/desktop/api/Dbghelp/nf-dbghelp-symgetsearchpath) function.

The search path for program database (.pdb) files is different than the path for debug (.dbg) files. The algorithm is determined by the functionality of the symbol library. By default, Microsoft Visual C/C++ creates Microsoft format symbols, strips them from the image, and places them in a separate .pdb file. Typically, the .pdb file will be located in the directory that contains the executable image. Visual C/C++ embeds the absolute path to the .pdb file in the executable image. If the symbol handler cannot find the .pdb file in that location or if the .pdb file was moved to another directory, the symbol handler will locate the .pdb file using the search path described for .dbg files.

## Path Element Types

There are three types of path elements.

### Standard Path Element

A standard path element is searched by looking in the root of the directory specified by the path element. The symbol handler also looks in a subdirectory of "symbols" that matches the file extension of the module that symbols are being looked for. This is typically "dll", "exe", or "sys". Lastly, it looks in a subdirectory called "symbols" with a directory of the same name as the extension. For example, if the symbol path element is "c:\\mySymbols" and the file that symbols are being searched for is "boo.dll", then the following directories would be searched.

- c:\\mySymbols  
- c:\\mySymbols\\dll  
- c:\\mySymbols\\symbols\\dll  

The symbol handler uses this logic to search any path element that does not meet the criteria to be a *symbol server* or *cache* (described below).

### Symbol Server Path Element

A *symbol server* path element uses special technology that can locate a symbol that is an exact match for the module in question. See [Using SymSrv](using-symsrv.md) for more details.

The symbol handler treats a path element as a symbol server if it begins with the text, "srv\*".

> [!Note]  
> If the "srv\*" text is not specified but the actual path element is a symbol server store, then the symbol handler will act as if "srv\*" were specified. The symbol handler makes this determination by searching for the existence of a file called "pingme.txt" in the root directory of the specified path.

 

### Cache Path Element

A *cache* path element is a variation on a symbol server path element.

This directory is searched like any other symbol server. However, if the symbol is not found here and it is found in a path element farther down the chain of the symbol path, then the symbol will be copied and stored in the symbol server specified in this element.

The symbol handler treats a path element as a cache element if it begins with the text, "cache\*". To specify a cache in "c:\\myCache", use a symbol path element of "cache\*c:\\myCache".

## Example Search Path

To see how this works, set this search path.

`cache*c:\myCache;srv*\\symbols\symbols`

<!-- 
See example from [Symbol path for Windows debuggers](/windows-hardware/drivers/debugger/symbol-path)
cache*c:\MySymbols;srv*https://msdl.microsoft.com/download/symbols
-->

The following is a listing of the symbol handler's verbose output while searching for ntdll.pdb, using the above listed search path.

```
DBGHELP: .\ntdll.pdb - file not found
DBGHELP: .\dll\ntdll.pdb - file not found
DBGHELP: .\symbols\dll\ntdll.pdb - file not found
SYMSRV: c:\myCache\ntdll.pdb\0F7FCF88442F4B0E9FB51DC4A754D9DE2\ntdll.pdb not found
SYMSRV: ntdll.pdb from \\symbols\symbols: 10497024 bytes - copied
DBGHELP: c:\myCache\ntdll.pdb\0F7FCF88442F4B0E9FB51DC4A754D9DE2\ntdll.pdb already cached
DBGHELP: ntdll - private symbols & lines
c:\myCache\ntdll.pdb\0F7FCF88442F4B0E9FB51DC4A754D9DE2\ntdll.pdb
```

The first three lines of output show the symbol handler processing the first path element of `.`. This is a standard path element.

The fourth line shows the symbol handler using the symbol server to look for the file in the second path element of `cache*c:\myCache` which is a cache path element.

The fifth line shows the file is found in the third path element of `srv*\\symbols\symbols`, which is a symbol server path element.

The sixth line shows that the file is copied to the cache.

The last two lines that the file is opened from the cache.
