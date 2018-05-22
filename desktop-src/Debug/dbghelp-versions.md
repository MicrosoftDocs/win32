---
Description: 'The DbgHelp library is implemented by DbgHelp.dll.'
ms.assetid: '8ef1740d-c791-4fbd-8297-7207a987c09d'
title: DbgHelp Versions
---

# DbgHelp Versions

The DbgHelp library is implemented by DbgHelp.dll. Although this DLL is included in all supported versions of Windows, it is rarely the most current version of DbgHelp available. Furthermore, the version of DbgHelp that ships in Windows has reduced functionality from the other releases-- specifically, it lacks support for Symbol Server and Source Server.

The most current versions of DbgHelp.dll, SymSrv.dll, and SrcSrv.dll are available as a part of the [Debugging Tools For Windows](Http://go.microsoft.com/fwlink/p/?linkid=84137) package. The redistribution policies for these included DLLs were specifically designed to make it as easy as possible for people to include these files in their own packages and releases.

> \[!Caution\]  
> Users should never attempt to install the [Debugging Tools For Windows](Http://go.microsoft.com/fwlink/p/?linkid=84137) versions of DbgHelp.dll into the Windows system directories because they are untested in this scenario and likely to destabilize the system. There are separate X64 and X86 versions of the debugging package and both are necessary for people interested in supporting both platforms.

 

To obtain the latest version of DbgHelp.dll, go to [http://www.microsoft.com/whdc/devtools/debugging/default.mspx](Http://go.microsoft.com/fwlink/p/?linkid=84137) and download Debugging Tools for Windows. Refer to [Calling the DbgHelp Library](calling-the-dbghelp-library.md) for information on proper installation.

> [!Note]  
> The DbgHelp.dll file that ships in Windows is not redistributable.

 

Many versions of DbgHelp include additional functionality. To ensure that the correct version of DbgHelp is available for your application, review the Requirements information in the specific API reference documentation.

## Supported Versions

The following is a summary of the released versions of DbgHelp, in reverse chronological order.



| Version | Date stamp | Distribution Vehicle             |
|---------|------------|----------------------------------|
| 6.12    | 02/01/2010 | Debugging Tools for Windows 6.12 |
| 6.11    | 02/25/2009 | Debugging Tools for Windows 6.11 |
| 6.10    | 09/08/2008 | Debugging Tools for Windows 6.10 |
| 6.9     | 03/20/2008 | Debugging Tools for Windows 6.9  |
| 6.8     | 10/07/2007 | Debugging Tools for Windows 6.8  |
| 6.6     | 7/10/2006  | Debugging Tools for Windows 6.6  |
| 6.5     | 5/24/2005  | Debugging Tools for Windows 6.5  |
| 6.4     | 1/10/2005  | Debugging Tools for Windows 6.4  |
| 6.3     | 5/24/2004  | Debugging Tools for Windows 6.3  |
| 6.2     | 7/11/2003  | Debugging Tools for Windows 6.2  |
| 6.1     |            | Debugging Tools for Windows 6.1  |
| 6.0     |            | Debugging Tools for Windows 6.0  |
| 4.0     |            | Debugging Tools for Windows 4.0  |
| 3.0     |            | Debugging Tools for Windows 3.0  |
| 2.0     |            | Debugging Tools for Windows 2.0  |
| 1.0     |            | Debugging Tools for Windows 1.0  |



 

## Version 6.8

The following functions were added to DbgHelp version 6.8.<dl>

[**EnumerateLoadedModulesEx**](enumerateloadedmodulesex.md)  
[**SymAddSourceStream**](symaddsourcestream.md)  
[**SymEnumTypesByName**](symenumtypesbyname.md)  
[**SymGetOmaps**](symgetomaps.md)  
[**SymGetSourceVarFromToken**](symgetsourcevarfromtoken.md)  
[**SymSetScopeFromAddr**](symsetscopefromaddr.md)  
[**SymSetScopeFromIndex**](symsetscopefromindex.md)  
</dl>

## Version 6.6

The following functions were added to DbgHelp version 6.6.<dl>

[**SymFindDebugInfoFile**](symfinddebuginfofile.md)  
[**SymFindExecutableImage**](symfindexecutableimage.md)  
[**SymSrvGetFileIndexInfo**](symsrvgetfileindexinfo.md)  
</dl>

## Version 6.5

The following function was added to DbgHelp version 6.5.<dl>

[**SymRefreshModuleList**](symrefreshmodulelist.md)  
</dl>

The following structures were added to DbgHelp version 6.5.<dl>

[**MINIDUMP\_HANDLE\_DESCRIPTOR\_2**](minidump-handle-descriptor-2.md)  
[**MINIDUMP\_HANDLE\_OBJECT\_INFORMATION**](minidump-handle-object-information.md)  
[**MINIDUMP\_HANDLE\_OPERATION\_LIST**](minidump-handle-operation-list.md)  
[**MINIDUMP\_IO\_CALLBACK**](minidump-io-callback.md)  
[**MINIDUMP\_MISC\_INFO\_2**](minidump-misc-info-2.md)  
[**MINIDUMP\_READ\_MEMORY\_FAILURE\_CALLBACK**](minidump-read-memory-failure-callback.md)  
</dl>

## Version 6.4

The following function was added to DbgHelp version 6.4.<dl>

[**SymEnumSourceLines**](symenumsourcelines.md)  
</dl>

## Version 6.3

DbgHelp version 6.3 adds Unicode support to many of the existing functions. To enable this support, define DBGHELP\_TRANSLATE\_TCHAR at the top of each source file or when you compile your application.

The following functions were added to DbgHelp version 6.3.<dl>

[**SymEnumProcesses**](symenumprocesses.md)  
[**SymGetSymbolFile**](symgetsymbolfile.md)  
[**SymGetTypeInfoEx**](symgettypeinfoex.md)  
[**SymSrvDeltaName**](symsrvdeltaname.md)  
[**SymSrvGetFileIndexes**](symsrvgetfileindexes.md)  
[**SymSrvGetFileIndexString**](symsrvgetfileindexstring.md)  
[**SymSrvGetSupplement**](symsrvgetsupplement.md)  
[**SymSrvIsStore**](symsrvisstore.md)  
[**SymSrvStoreFile**](symsrvstorefile.md)  
[**SymSrvStoreSupplement**](symsrvstoresupplement.md)  
</dl>

The following structures were added to DbgHelp version 6.3.<dl>

[**MINIDUMP\_MEMORY\_INFO**](minidump-memory-info-str.md)  
[**MINIDUMP\_MEMORY\_INFO\_LIST**](minidump-memory-info-list-str.md)  
[**MINIDUMP\_THREAD\_INFO**](minidump-thread-info-str.md)  
[**MINIDUMP\_THREAD\_INFO\_LIST**](minidump-thread-info-list-str.md)  
</dl>

DbgHelp 6.3 also supports [Source Server](source-server-and-source-indexing.md).

## Version 6.2

The following functions were added to DbgHelp version 6.2.<dl>

[**SymEnumSourceFiles**](symenumsourcefiles.md)  
[**SymFromIndex**](symfromindex.md)  
[**SymGetScope**](symgetscope.md)  
[**SymGetSourceFile**](symgetsourcefile.md)  
[**SymGetSourceFileFromToken**](symgetsourcefilefromtoken.md)  
[**SymGetSourceFileToken**](symgetsourcefiletoken.md)  
[**SymMatchString**](symmatchstring.md)  
[**SymNext**](symnext.md)  
[**SymPrev**](symprev.md)  
[**SymSearch**](symsearch.md)  
</dl>

## Version 6.1

The following functions were added to DbgHelp version 6.1.<dl>

[**SymEnumLines**](symenumlines.md)  
[**SymFromToken**](symfromtoken.md)  
[**SymGetHomeDirectory**](symgethomedirectory.md)  
[**SymSetHomeDirectory**](symsethomedirectory.md)  
</dl>

## Versions 5.2 and 6.0

The following functions were added to DbgHelp versions 5.2 and 6.0.<dl>

[**EnumDirTree**](enumdirtree.md)  
[**SymAddSymbol**](symaddsymbol.md)  
[**SymDeleteSymbol**](symdeletesymbol.md)  
[**SymEnumSymbolsForAddr**](symenumsymbolsforaddr.md)  
[**SymLoadModuleEx**](symloadmoduleex.md)  
[**SymSetParentWindow**](symsetparentwindow.md)  
</dl>

The following structures were added to DbgHelp version 5.2 and 6.0.<dl>

[**MINIDUMP\_MISC\_INFO**](minidump-misc-info-str.md)  
[**MINIDUMP\_UNLOADED\_MODULE**](minidump-unloaded-module-str.md)  
[**MINIDUMP\_UNLOADED\_MODULE\_LIST**](minidump-unloaded-module-list-str.md)  
[**MODLOAD\_DATA**](modload-data-str.md)  
</dl>

## Versions 4.0 and 5.1

The following functions were added to DbgHelp versions 4.0 and 5.1.<dl>

[**MiniDumpReadDumpStream**](minidumpreaddumpstream.md)  
[**MiniDumpWriteDump**](minidumpwritedump.md)  
[**SymbolServer**](base.symbolserver)  
[**SymbolServerClose**](base.symbolserverclose)  
[**SymbolServerGetOptions**](base.symbolservergetoptions)  
[**SymbolServerSetOptions**](base.symbolserversetoptions)  
[**SymEnumSymbols**](symenumsymbols.md)  
[**SymEnumTypes**](symenumtypes.md)  
[**SymFindFileInPath**](symfindfileinpath.md)  
[**SymFromAddr**](symfromaddr.md)  
[**SymFromName**](symfromname.md)  
[**SymGetFileLineOffsets64**](symgetfilelineoffsets64.md)  
[**SymGetTypeFromName**](symgettypefromname.md)  
[**SymGetTypeInfo**](symgettypeinfo.md)  
[**SymSetContext**](symsetcontext.md)  
</dl>

 

 



