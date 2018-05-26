---
Description: The following are the DbgHelp functions.
ms.assetid: 7b28f70b-2d97-4cc2-8064-dfb806f9cffa
title: DbgHelp Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DbgHelp Functions

The following are the DbgHelp functions.

## General

The following are general helper functions:

<dl>

[**EnumDirTree**](/windows/win32/Dbghelp/nf-dbghelp-enumdirtree?branch=master)  
[**ImagehlpApiVersion**](/windows/win32/Dbghelp/nf-dbghelp-imagehlpapiversion?branch=master)  
[**ImagehlpApiVersionEx**](/windows/win32/Dbghelp/nf-dbghelp-imagehlpapiversionex?branch=master)  
[**MakeSureDirectoryPathExists**](/windows/win32/Dbghelp/nf-dbghelp-makesuredirectorypathexists?branch=master)  
[**SearchTreeForFile**](/windows/win32/Dbghelp/nf-dbghelp-searchtreeforfile?branch=master)  
</dl>

## Debugger

The debugging service functions are the functions most suited for use by a debugger or the debugging code in an application. These functions can be used in concert with the symbol handler functions for easier use.

<dl>

[**EnumerateLoadedModules64**](/windows/win32/Dbghelp/nf-dbghelp-enumerateloadedmodules?branch=master)  
[**EnumerateLoadedModulesEx**](/windows/win32/Dbghelp/nf-dbghelp-enumerateloadedmodulesex?branch=master)  
[**FindDebugInfoFile**](/windows/win32/Dbghelp/nf-dbghelp-finddebuginfofile?branch=master)  
[**FindDebugInfoFileEx**](/windows/win32/Dbghelp/nf-dbghelp-finddebuginfofileex?branch=master)  
[**FindExecutableImage**](/windows/win32/Dbghelp/nf-dbghelp-findexecutableimage?branch=master)  
[**FindExecutableImageEx**](/windows/win32/Dbghelp/nf-dbghelp-findexecutableimageex?branch=master)  
[**StackWalk64**](/windows/win32/DbgHelp/nf-dbghelp-stackwalk?branch=master)  
[**SymSetParentWindow**](/windows/win32/Dbghelp/nf-dbghelp-symsetparentwindow?branch=master)  
[**UnDecorateSymbolName**](/windows/win32/Dbghelp/nf-dbghelp-undecoratesymbolname?branch=master)  
</dl>

## Image Access

The image access functions access the data in an executable image. The functions provide high-level access to the base of images and very specific access to the most common parts of an image's data.

<dl>

[**GetTimestampForLoadedLibrary**](/windows/win32/Dbghelp/nf-dbghelp-gettimestampforloadedlibrary?branch=master)  
[**ImageDirectoryEntryToData**](/windows/win32/Dbghelp/nf-dbghelp-imagedirectoryentrytodata?branch=master)  
[**ImageDirectoryEntryToDataEx**](/windows/win32/Dbghelp/nf-dbghelp-imagedirectoryentrytodataex?branch=master)  
[**ImageNtHeader**](/windows/win32/Dbghelp/nf-dbghelp-imagentheader?branch=master)  
[**ImageRvaToSection**](/windows/win32/Dbghelp/nf-dbghelp-imagervatosection?branch=master)  
[**ImageRvaToVa**](/windows/win32/Dbghelp/nf-dbghelp-imagervatova?branch=master)  
</dl>

## Symbol Handler

The [symbol handler](symbol-handling.md) functions give applications easy and portable access to the symbolic debugging information of an image. These functions should be used exclusively to ensure access to symbolic information. This is necessary because these functions isolate the application from the symbol format.

<dl>

[**SymAddSourceStream**](/windows/win32/Dbghelp/nf-dbghelp-symaddsourcestream?branch=master)  
[**SymAddSymbol**](/windows/win32/Dbghelp/nf-dbghelp-symaddsymbol?branch=master)  
[**SymCleanup**](/windows/win32/Dbghelp/nf-dbghelp-symcleanup?branch=master)  
[**SymDeleteSymbol**](/windows/win32/Dbghelp/nf-dbghelp-symdeletesymbol?branch=master)  
[**SymEnumerateModules64**](/windows/win32/Dbghelp/nf-dbghelp-symenumeratemodules?branch=master)  
[**SymEnumLines**](/windows/win32/Dbghelp/nf-dbghelp-symenumlines?branch=master)  
[**SymEnumProcesses**](/windows/win32/DbgHelp/nf-dbghelp-symenumprocesses?branch=master)  
[**SymEnumSourceFiles**](/windows/win32/DbgHelp/nf-dbghelp-symenumsourcefiles?branch=master)  
[**SymEnumSourceLines**](/windows/win32/DbgHelp/nf-dbghelp-symenumsourcelines?branch=master)  
[**SymEnumSymbols**](/windows/win32/Dbghelp/nf-dbghelp-symenumsymbols?branch=master)  
[**SymEnumSymbolsForAddr**](/windows/win32/Dbghelp/nf-dbghelp-symenumsymbolsforaddr?branch=master)  
[**SymEnumTypes**](/windows/win32/Dbghelp/nf-dbghelp-symenumtypes?branch=master)  
[**SymEnumTypesByName**](/windows/win32/Dbghelp/nf-dbghelp-symenumtypesbyname?branch=master)  
[**SymFindDebugInfoFile**](/windows/win32/Dbghelp/nf-dbghelp-symfinddebuginfofile?branch=master)  
[**SymFindExecutableImage**](/windows/win32/Dbghelp/nf-dbghelp-symfindexecutableimage?branch=master)  
[**SymFindFileInPath**](/windows/win32/DbgHelp/nf-dbghelp-symfindfileinpath?branch=master)  
[**SymFromAddr**](/windows/win32/Dbghelp/nf-dbghelp-symfromaddr?branch=master)  
[**SymFromIndex**](/windows/win32/Dbghelp/nf-dbghelp-symfromindex?branch=master)  
[**SymFromName**](/windows/win32/Dbghelp/nf-dbghelp-symfromname?branch=master)  
[**SymFromToken**](/windows/win32/Dbghelp/nf-dbghelp-symfromtoken?branch=master)  
[**SymFunctionTableAccess64**](/windows/win32/Dbghelp/nf-dbghelp-symfunctiontableaccess?branch=master)  
[**SymGetFileLineOffsets64**](/windows/win32/Dbghelp/nf-dbghelp-symgetfilelineoffsets64?branch=master)  
[**SymGetHomeDirectory**](/windows/win32/Dbghelp/nf-dbghelp-symgethomedirectory?branch=master)  
[**SymGetLineFromAddr64**](/windows/win32/Dbghelp/nf-dbghelp-symgetlinefromaddr?branch=master)  
[**SymGetLineFromName64**](/windows/win32/Dbghelp/nf-dbghelp-symgetlinefromname?branch=master)  
[**SymGetLineNext64**](/windows/win32/Dbghelp/nf-dbghelp-symgetlinenext?branch=master)  
[**SymGetLinePrev64**](/windows/win32/Dbghelp/nf-dbghelp-symgetlineprev?branch=master)  
[**SymGetModuleBase64**](/windows/win32/Dbghelp/nf-dbghelp-symgetmodulebase?branch=master)  
[**SymGetModuleInfo64**](/windows/win32/Dbghelp/nf-dbghelp-symgetmoduleinfo?branch=master)  
[**SymGetOmaps**](/windows/win32/Dbghelp/nf-dbghelp-symgetomaps?branch=master)  
[**SymGetOptions**](/windows/win32/Dbghelp/nf-dbghelp-symgetoptions?branch=master)  
[**SymGetScope**](/windows/win32/Dbghelp/nf-dbghelp-symgetscope?branch=master)  
[**SymGetSearchPath**](/windows/win32/Dbghelp/nf-dbghelp-symgetsearchpath?branch=master)  
[**SymGetSymbolFile**](/windows/win32/Dbghelp/nf-dbghelp-symgetsymbolfile?branch=master)  
[**SymGetTypeFromName**](/windows/win32/Dbghelp/nf-dbghelp-symgettypefromname?branch=master)  
[**SymGetTypeInfo**](/windows/win32/Dbghelp/nf-dbghelp-symgettypeinfo?branch=master)  
[**SymGetTypeInfoEx**](/windows/win32/Dbghelp/nf-dbghelp-symgettypeinfoex?branch=master)  
[**SymInitialize**](/windows/win32/Dbghelp/nf-dbghelp-syminitialize?branch=master)  
[**SymLoadModule64**](/windows/win32/Dbghelp/nf-dbghelp-symloadmodule?branch=master)  
[**SymLoadModuleEx**](/windows/win32/Dbghelp/nf-dbghelp-symloadmoduleex?branch=master)  
[**SymMatchFileName**](/windows/win32/Dbghelp/nf-dbghelp-symmatchfilename?branch=master)  
[**SymMatchString**](/windows/win32/DbgHelp/nf-dbghelp-symmatchstring?branch=master)  
[**SymNext**](/windows/win32/DbgHelp/nf-dbghelp-symnext?branch=master)  
[**SymPrev**](/windows/win32/DbgHelp/nf-dbghelp-symprev?branch=master)  
[**SymRefreshModuleList**](/windows/win32/Dbghelp/nf-dbghelp-symrefreshmodulelist?branch=master)  
[**SymRegisterCallback64**](/windows/win32/Dbghelp/nf-dbghelp-symregistercallback?branch=master)  
[**SymRegisterFunctionEntryCallback64**](/windows/win32/Dbghelp/nf-dbghelp-symregisterfunctionentrycallback?branch=master)  
[**SymSearch**](/windows/win32/Dbghelp/nf-dbghelp-symsearch?branch=master)  
[**SymSetContext**](/windows/win32/Dbghelp/nf-dbghelp-symsetcontext?branch=master)  
[**SymSetHomeDirectory**](/windows/win32/Dbghelp/nf-dbghelp-symsethomedirectory?branch=master)  
[**SymSetOptions**](/windows/win32/Dbghelp/nf-dbghelp-symsetoptions?branch=master)  
[**SymSetScopeFromAddr**](/windows/win32/Dbghelp/nf-dbghelp-symsetscopefromaddr?branch=master)  
[**SymSetScopeFromIndex**](/windows/win32/Dbghelp/nf-dbghelp-symsetscopefromindex?branch=master)  
[**SymSetSearchPath**](/windows/win32/Dbghelp/nf-dbghelp-symsetsearchpath?branch=master)  
[**SymUnDName64**](/windows/win32/Dbghelp/nf-dbghelp-symundname?branch=master)  
[**SymUnloadModule64**](/windows/win32/Dbghelp/nf-dbghelp-symunloadmodule?branch=master)  
</dl>

## Symbol Server

The [symbol server](symbol-servers-and-symbol-stores.md) enables debuggers to automatically retrieve the correct symbol files without product names, releases, or build numbers. The following functions are used with the symbol server.

<dl>

[**SymSrvDeltaName**](/windows/win32/DbgHelp/nf-dbghelp-symsrvdeltaname?branch=master)  
[**SymSrvGetFileIndexes**](/windows/win32/DbgHelp/nf-dbghelp-symsrvgetfileindexes?branch=master)  
[**SymSrvGetFileIndexInfo**](/windows/win32/Dbghelp/nf-dbghelp-symsrvgetfileindexinfo?branch=master)  
[**SymSrvGetFileIndexString**](/windows/win32/DbgHelp/nf-dbghelp-symsrvgetfileindexstring?branch=master)  
[**SymSrvGetSupplement**](/windows/win32/DbgHelp/nf-dbghelp-symsrvgetsupplement?branch=master)  
[**SymSrvIsStore**](/windows/win32/DbgHelp/nf-dbghelp-symsrvisstore?branch=master)  
[**SymSrvStoreFile**](/windows/win32/DbgHelp/nf-dbghelp-symsrvstorefile?branch=master)  
[**SymSrvStoreSupplement**](/windows/win32/DbgHelp/nf-dbghelp-symsrvstoresupplement?branch=master)  
</dl>

## User-mode Minidump Files

The minidump functions provide a way for applications to produce crashdump files that contain a useful subset of the entire process context; this is known as a [minidump file](minidump-files.md). The following functions are used with minidump files.

<dl>

[**MiniDumpCallback**](/windows/win32/minidumpapiset/nc-minidumpapiset-minidump_callback_routine?branch=master)  
[**MiniDumpReadDumpStream**](/windows/win32/minidumpapiset/nf-minidumpapiset-minidumpreaddumpstream?branch=master)  
[**MiniDumpWriteDump**](/windows/win32/minidumpapiset/nf-minidumpapiset-minidumpwritedump?branch=master)  
</dl>

## Source Server

[Source server](source-server-and-source-indexing.md) enables a client to retrieve the exact version of the source files that were used to build an application. The following functions are used with source server.

-   [**SymGetSourceFile**](/windows/win32/Dbghelp/nf-dbghelp-symgetsourcefile?branch=master)
-   [**SymEnumSourceFileTokens**](/windows/win32/Dbghelp/nf-dbghelp-symenumsourcefiletokens?branch=master)
-   [**SymEnumSourceFileTokensProc**](/windows/win32/Dbghelp/nc-dbghelp-penumsourcefiletokenscallback?branch=master)
-   [**SymGetSourceFileFromToken**](/windows/win32/Dbghelp/nf-dbghelp-symgetsourcefilefromtoken?branch=master)
-   [**SymGetSourceFileToken**](/windows/win32/Dbghelp/nf-dbghelp-symgetsourcefiletoken?branch=master)
-   [**SymGetSourceVarFromToken**](/windows/win32/Dbghelp/nf-dbghelp-symgetsourcevarfromtoken?branch=master)

## Obsolete Functions

<dl>

[**MapDebugInformation**](/windows/win32/Dbghelp/nf-dbghelp-mapdebuginformation?branch=master)  
[**SymEnumerateSymbols64**](/windows/win32/Dbghelp/nf-dbghelp-symenumeratesymbols?branch=master)  
[**SymGetSymFromAddr64**](/windows/win32/Dbghelp/nf-dbghelp-symgetsymfromaddr?branch=master)  
[**SymGetSymFromName64**](/windows/win32/Dbghelp/nf-dbghelp-symgetsymfromname?branch=master)  
[**SymGetSymNext64**](/windows/win32/Dbghelp/nf-dbghelp-symgetsymnext?branch=master)  
[**SymGetSymPrev64**](/windows/win32/Dbghelp/nf-dbghelp-symgetsymprev?branch=master)  
[**UnMapDebugInformation**](/windows/win32/Dbghelp/nf-dbghelp-unmapdebuginformation?branch=master)  
</dl>

 

 



