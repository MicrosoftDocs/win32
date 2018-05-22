---
Description: 'The following are the DbgHelp functions.'
ms.assetid: '7b28f70b-2d97-4cc2-8064-dfb806f9cffa'
title: DbgHelp Functions
---

# DbgHelp Functions

The following are the DbgHelp functions.

## General

The following are general helper functions:

<dl>

[**EnumDirTree**](enumdirtree.md)  
[**ImagehlpApiVersion**](imagehlpapiversion.md)  
[**ImagehlpApiVersionEx**](imagehlpapiversionex.md)  
[**MakeSureDirectoryPathExists**](makesuredirectorypathexists.md)  
[**SearchTreeForFile**](searchtreeforfile.md)  
</dl>

## Debugger

The debugging service functions are the functions most suited for use by a debugger or the debugging code in an application. These functions can be used in concert with the symbol handler functions for easier use.

<dl>

[**EnumerateLoadedModules64**](enumerateloadedmodules64.md)  
[**EnumerateLoadedModulesEx**](enumerateloadedmodulesex.md)  
[**FindDebugInfoFile**](finddebuginfofile.md)  
[**FindDebugInfoFileEx**](finddebuginfofileex.md)  
[**FindExecutableImage**](findexecutableimage.md)  
[**FindExecutableImageEx**](findexecutableimageex.md)  
[**StackWalk64**](stackwalk64.md)  
[**SymSetParentWindow**](symsetparentwindow.md)  
[**UnDecorateSymbolName**](undecoratesymbolname.md)  
</dl>

## Image Access

The image access functions access the data in an executable image. The functions provide high-level access to the base of images and very specific access to the most common parts of an image's data.

<dl>

[**GetTimestampForLoadedLibrary**](gettimestampforloadedlibrary.md)  
[**ImageDirectoryEntryToData**](imagedirectoryentrytodata.md)  
[**ImageDirectoryEntryToDataEx**](imagedirectoryentrytodataex.md)  
[**ImageNtHeader**](imagentheader.md)  
[**ImageRvaToSection**](imagervatosection.md)  
[**ImageRvaToVa**](imagervatova.md)  
</dl>

## Symbol Handler

The [symbol handler](symbol-handling.md) functions give applications easy and portable access to the symbolic debugging information of an image. These functions should be used exclusively to ensure access to symbolic information. This is necessary because these functions isolate the application from the symbol format.

<dl>

[**SymAddSourceStream**](symaddsourcestream.md)  
[**SymAddSymbol**](symaddsymbol.md)  
[**SymCleanup**](symcleanup.md)  
[**SymDeleteSymbol**](symdeletesymbol.md)  
[**SymEnumerateModules64**](symenumeratemodules64.md)  
[**SymEnumLines**](symenumlines.md)  
[**SymEnumProcesses**](symenumprocesses.md)  
[**SymEnumSourceFiles**](symenumsourcefiles.md)  
[**SymEnumSourceLines**](symenumsourcelines.md)  
[**SymEnumSymbols**](symenumsymbols.md)  
[**SymEnumSymbolsForAddr**](symenumsymbolsforaddr.md)  
[**SymEnumTypes**](symenumtypes.md)  
[**SymEnumTypesByName**](symenumtypesbyname.md)  
[**SymFindDebugInfoFile**](symfinddebuginfofile.md)  
[**SymFindExecutableImage**](symfindexecutableimage.md)  
[**SymFindFileInPath**](symfindfileinpath.md)  
[**SymFromAddr**](symfromaddr.md)  
[**SymFromIndex**](symfromindex.md)  
[**SymFromName**](symfromname.md)  
[**SymFromToken**](symfromtoken.md)  
[**SymFunctionTableAccess64**](symfunctiontableaccess64.md)  
[**SymGetFileLineOffsets64**](symgetfilelineoffsets64.md)  
[**SymGetHomeDirectory**](symgethomedirectory.md)  
[**SymGetLineFromAddr64**](symgetlinefromaddr64.md)  
[**SymGetLineFromName64**](symgetlinefromname64.md)  
[**SymGetLineNext64**](symgetlinenext64.md)  
[**SymGetLinePrev64**](symgetlineprev64.md)  
[**SymGetModuleBase64**](symgetmodulebase64.md)  
[**SymGetModuleInfo64**](symgetmoduleinfo64.md)  
[**SymGetOmaps**](symgetomaps.md)  
[**SymGetOptions**](symgetoptions.md)  
[**SymGetScope**](symgetscope.md)  
[**SymGetSearchPath**](symgetsearchpath.md)  
[**SymGetSymbolFile**](symgetsymbolfile.md)  
[**SymGetTypeFromName**](symgettypefromname.md)  
[**SymGetTypeInfo**](symgettypeinfo.md)  
[**SymGetTypeInfoEx**](symgettypeinfoex.md)  
[**SymInitialize**](syminitialize.md)  
[**SymLoadModule64**](symloadmodule64.md)  
[**SymLoadModuleEx**](symloadmoduleex.md)  
[**SymMatchFileName**](symmatchfilename.md)  
[**SymMatchString**](symmatchstring.md)  
[**SymNext**](symnext.md)  
[**SymPrev**](symprev.md)  
[**SymRefreshModuleList**](symrefreshmodulelist.md)  
[**SymRegisterCallback64**](symregistercallback64.md)  
[**SymRegisterFunctionEntryCallback64**](symregisterfunctionentrycallback64.md)  
[**SymSearch**](symsearch.md)  
[**SymSetContext**](symsetcontext.md)  
[**SymSetHomeDirectory**](symsethomedirectory.md)  
[**SymSetOptions**](symsetoptions.md)  
[**SymSetScopeFromAddr**](symsetscopefromaddr.md)  
[**SymSetScopeFromIndex**](symsetscopefromindex.md)  
[**SymSetSearchPath**](symsetsearchpath.md)  
[**SymUnDName64**](symundname64.md)  
[**SymUnloadModule64**](symunloadmodule64.md)  
</dl>

## Symbol Server

The [symbol server](symbol-servers-and-symbol-stores.md) enables debuggers to automatically retrieve the correct symbol files without product names, releases, or build numbers. The following functions are used with the symbol server.

<dl>

[**SymSrvDeltaName**](symsrvdeltaname.md)  
[**SymSrvGetFileIndexes**](symsrvgetfileindexes.md)  
[**SymSrvGetFileIndexInfo**](symsrvgetfileindexinfo.md)  
[**SymSrvGetFileIndexString**](symsrvgetfileindexstring.md)  
[**SymSrvGetSupplement**](symsrvgetsupplement.md)  
[**SymSrvIsStore**](symsrvisstore.md)  
[**SymSrvStoreFile**](symsrvstorefile.md)  
[**SymSrvStoreSupplement**](symsrvstoresupplement.md)  
</dl>

## User-mode Minidump Files

The minidump functions provide a way for applications to produce crashdump files that contain a useful subset of the entire process context; this is known as a [minidump file](minidump-files.md). The following functions are used with minidump files.

<dl>

[**MiniDumpCallback**](minidumpcallback.md)  
[**MiniDumpReadDumpStream**](minidumpreaddumpstream.md)  
[**MiniDumpWriteDump**](minidumpwritedump.md)  
</dl>

## Source Server

[Source server](source-server-and-source-indexing.md) enables a client to retrieve the exact version of the source files that were used to build an application. The following functions are used with source server.

-   [**SymGetSourceFile**](symgetsourcefile.md)
-   [**SymEnumSourceFileTokens**](symenumsourcefiletokens.md)
-   [**SymEnumSourceFileTokensProc**](symenumsourcefiletokensproc.md)
-   [**SymGetSourceFileFromToken**](symgetsourcefilefromtoken.md)
-   [**SymGetSourceFileToken**](symgetsourcefiletoken.md)
-   [**SymGetSourceVarFromToken**](symgetsourcevarfromtoken.md)

## Obsolete Functions

<dl>

[**MapDebugInformation**](mapdebuginformation.md)  
[**SymEnumerateSymbols64**](symenumeratesymbols64.md)  
[**SymGetSymFromAddr64**](symgetsymfromaddr64.md)  
[**SymGetSymFromName64**](symgetsymfromname64.md)  
[**SymGetSymNext64**](symgetsymnext64.md)  
[**SymGetSymPrev64**](symgetsymprev64.md)  
[**UnMapDebugInformation**](unmapdebuginformation.md)  
</dl>

 

 



