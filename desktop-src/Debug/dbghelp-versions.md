---
Description: The DbgHelp library is implemented by DbgHelp.dll.
ms.assetid: 8ef1740d-c791-4fbd-8297-7207a987c09d
title: DbgHelp Versions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

[**EnumerateLoadedModulesEx**](/windows/win32/Dbghelp/nf-dbghelp-enumerateloadedmodulesex?branch=master)  
[**SymAddSourceStream**](/windows/win32/Dbghelp/nf-dbghelp-symaddsourcestream?branch=master)  
[**SymEnumTypesByName**](/windows/win32/Dbghelp/nf-dbghelp-symenumtypesbyname?branch=master)  
[**SymGetOmaps**](/windows/win32/Dbghelp/nf-dbghelp-symgetomaps?branch=master)  
[**SymGetSourceVarFromToken**](/windows/win32/Dbghelp/nf-dbghelp-symgetsourcevarfromtoken?branch=master)  
[**SymSetScopeFromAddr**](/windows/win32/Dbghelp/nf-dbghelp-symsetscopefromaddr?branch=master)  
[**SymSetScopeFromIndex**](/windows/win32/Dbghelp/nf-dbghelp-symsetscopefromindex?branch=master)  
</dl>

## Version 6.6

The following functions were added to DbgHelp version 6.6.<dl>

[**SymFindDebugInfoFile**](/windows/win32/Dbghelp/nf-dbghelp-symfinddebuginfofile?branch=master)  
[**SymFindExecutableImage**](/windows/win32/Dbghelp/nf-dbghelp-symfindexecutableimage?branch=master)  
[**SymSrvGetFileIndexInfo**](/windows/win32/Dbghelp/nf-dbghelp-symsrvgetfileindexinfo?branch=master)  
</dl>

## Version 6.5

The following function was added to DbgHelp version 6.5.<dl>

[**SymRefreshModuleList**](/windows/win32/Dbghelp/nf-dbghelp-symrefreshmodulelist?branch=master)  
</dl>

The following structures were added to DbgHelp version 6.5.<dl>

[**MINIDUMP\_HANDLE\_DESCRIPTOR\_2**](/windows/win32/minidumpapiset/ns-minidumpapiset-_minidump_handle_descriptor_2?branch=master)  
[**MINIDUMP\_HANDLE\_OBJECT\_INFORMATION**](/windows/win32/minidumpapiset/ns-minidumpapiset-_minidump_handle_object_information?branch=master)  
[**MINIDUMP\_HANDLE\_OPERATION\_LIST**](/windows/win32/minidumpapiset/ns-minidumpapiset-_minidump_handle_operation_list?branch=master)  
[**MINIDUMP\_IO\_CALLBACK**](/windows/win32/minidumpapiset/ns-minidumpapiset-_minidump_io_callback?branch=master)  
[**MINIDUMP\_MISC\_INFO\_2**](/windows/win32/minidumpapiset/ns-minidumpapiset-_minidump_misc_info_2?branch=master)  
[**MINIDUMP\_READ\_MEMORY\_FAILURE\_CALLBACK**](/windows/win32/minidumpapiset/ns-minidumpapiset-_minidump_read_memory_failure_callback?branch=master)  
</dl>

## Version 6.4

The following function was added to DbgHelp version 6.4.<dl>

[**SymEnumSourceLines**](/windows/win32/DbgHelp/nf-dbghelp-symenumsourcelines?branch=master)  
</dl>

## Version 6.3

DbgHelp version 6.3 adds Unicode support to many of the existing functions. To enable this support, define DBGHELP\_TRANSLATE\_TCHAR at the top of each source file or when you compile your application.

The following functions were added to DbgHelp version 6.3.<dl>

[**SymEnumProcesses**](/windows/win32/DbgHelp/nf-dbghelp-symenumprocesses?branch=master)  
[**SymGetSymbolFile**](/windows/win32/Dbghelp/nf-dbghelp-symgetsymbolfile?branch=master)  
[**SymGetTypeInfoEx**](/windows/win32/Dbghelp/nf-dbghelp-symgettypeinfoex?branch=master)  
[**SymSrvDeltaName**](/windows/win32/DbgHelp/nf-dbghelp-symsrvdeltaname?branch=master)  
[**SymSrvGetFileIndexes**](/windows/win32/DbgHelp/nf-dbghelp-symsrvgetfileindexes?branch=master)  
[**SymSrvGetFileIndexString**](/windows/win32/DbgHelp/nf-dbghelp-symsrvgetfileindexstring?branch=master)  
[**SymSrvGetSupplement**](/windows/win32/DbgHelp/nf-dbghelp-symsrvgetsupplement?branch=master)  
[**SymSrvIsStore**](/windows/win32/DbgHelp/nf-dbghelp-symsrvisstore?branch=master)  
[**SymSrvStoreFile**](/windows/win32/DbgHelp/nf-dbghelp-symsrvstorefile?branch=master)  
[**SymSrvStoreSupplement**](/windows/win32/DbgHelp/nf-dbghelp-symsrvstoresupplement?branch=master)  
</dl>

The following structures were added to DbgHelp version 6.3.<dl>

[**MINIDUMP\_MEMORY\_INFO**](/windows/win32/minidumpapiset/ns-minidumpapiset-_minidump_memory_info?branch=master)  
[**MINIDUMP\_MEMORY\_INFO\_LIST**](/windows/win32/minidumpapiset/ns-minidumpapiset-_minidump_memory_info_list?branch=master)  
[**MINIDUMP\_THREAD\_INFO**](/windows/win32/minidumpapiset/ns-minidumpapiset-_minidump_thread_info?branch=master)  
[**MINIDUMP\_THREAD\_INFO\_LIST**](/windows/win32/minidumpapiset/ns-minidumpapiset-_minidump_thread_info_list?branch=master)  
</dl>

DbgHelp 6.3 also supports [Source Server](source-server-and-source-indexing.md).

## Version 6.2

The following functions were added to DbgHelp version 6.2.<dl>

[**SymEnumSourceFiles**](/windows/win32/DbgHelp/nf-dbghelp-symenumsourcefiles?branch=master)  
[**SymFromIndex**](/windows/win32/Dbghelp/nf-dbghelp-symfromindex?branch=master)  
[**SymGetScope**](/windows/win32/Dbghelp/nf-dbghelp-symgetscope?branch=master)  
[**SymGetSourceFile**](/windows/win32/Dbghelp/nf-dbghelp-symgetsourcefile?branch=master)  
[**SymGetSourceFileFromToken**](/windows/win32/Dbghelp/nf-dbghelp-symgetsourcefilefromtoken?branch=master)  
[**SymGetSourceFileToken**](/windows/win32/Dbghelp/nf-dbghelp-symgetsourcefiletoken?branch=master)  
[**SymMatchString**](/windows/win32/DbgHelp/nf-dbghelp-symmatchstring?branch=master)  
[**SymNext**](/windows/win32/DbgHelp/nf-dbghelp-symnext?branch=master)  
[**SymPrev**](/windows/win32/DbgHelp/nf-dbghelp-symprev?branch=master)  
[**SymSearch**](/windows/win32/Dbghelp/nf-dbghelp-symsearch?branch=master)  
</dl>

## Version 6.1

The following functions were added to DbgHelp version 6.1.<dl>

[**SymEnumLines**](/windows/win32/Dbghelp/nf-dbghelp-symenumlines?branch=master)  
[**SymFromToken**](/windows/win32/Dbghelp/nf-dbghelp-symfromtoken?branch=master)  
[**SymGetHomeDirectory**](/windows/win32/Dbghelp/nf-dbghelp-symgethomedirectory?branch=master)  
[**SymSetHomeDirectory**](/windows/win32/Dbghelp/nf-dbghelp-symsethomedirectory?branch=master)  
</dl>

## Versions 5.2 and 6.0

The following functions were added to DbgHelp versions 5.2 and 6.0.<dl>

[**EnumDirTree**](/windows/win32/Dbghelp/nf-dbghelp-enumdirtree?branch=master)  
[**SymAddSymbol**](/windows/win32/Dbghelp/nf-dbghelp-symaddsymbol?branch=master)  
[**SymDeleteSymbol**](/windows/win32/Dbghelp/nf-dbghelp-symdeletesymbol?branch=master)  
[**SymEnumSymbolsForAddr**](/windows/win32/Dbghelp/nf-dbghelp-symenumsymbolsforaddr?branch=master)  
[**SymLoadModuleEx**](/windows/win32/Dbghelp/nf-dbghelp-symloadmoduleex?branch=master)  
[**SymSetParentWindow**](/windows/win32/Dbghelp/nf-dbghelp-symsetparentwindow?branch=master)  
</dl>

The following structures were added to DbgHelp version 5.2 and 6.0.<dl>

[**MINIDUMP\_MISC\_INFO**](/windows/win32/minidumpapiset/ns-minidumpapiset-_minidump_misc_info?branch=master)  
[**MINIDUMP\_UNLOADED\_MODULE**](/windows/win32/minidumpapiset/ns-minidumpapiset-_minidump_unloaded_module?branch=master)  
[**MINIDUMP\_UNLOADED\_MODULE\_LIST**](/windows/win32/minidumpapiset/ns-minidumpapiset-_minidump_unloaded_module_list?branch=master)  
[**MODLOAD\_DATA**](/windows/win32/DbgHelp/ns-dbghelp-_modload_data?branch=master)  
</dl>

## Versions 4.0 and 5.1

The following functions were added to DbgHelp versions 4.0 and 5.1.<dl>

[**MiniDumpReadDumpStream**](/windows/win32/minidumpapiset/nf-minidumpapiset-minidumpreaddumpstream?branch=master)  
[**MiniDumpWriteDump**](/windows/win32/minidumpapiset/nf-minidumpapiset-minidumpwritedump?branch=master)  
[**SymbolServer**](base.symbolserver)  
[**SymbolServerClose**](base.symbolserverclose)  
[**SymbolServerGetOptions**](base.symbolservergetoptions)  
[**SymbolServerSetOptions**](base.symbolserversetoptions)  
[**SymEnumSymbols**](/windows/win32/Dbghelp/nf-dbghelp-symenumsymbols?branch=master)  
[**SymEnumTypes**](/windows/win32/Dbghelp/nf-dbghelp-symenumtypes?branch=master)  
[**SymFindFileInPath**](/windows/win32/DbgHelp/nf-dbghelp-symfindfileinpath?branch=master)  
[**SymFromAddr**](/windows/win32/Dbghelp/nf-dbghelp-symfromaddr?branch=master)  
[**SymFromName**](/windows/win32/Dbghelp/nf-dbghelp-symfromname?branch=master)  
[**SymGetFileLineOffsets64**](/windows/win32/Dbghelp/nf-dbghelp-symgetfilelineoffsets64?branch=master)  
[**SymGetTypeFromName**](/windows/win32/Dbghelp/nf-dbghelp-symgettypefromname?branch=master)  
[**SymGetTypeInfo**](/windows/win32/Dbghelp/nf-dbghelp-symgettypeinfo?branch=master)  
[**SymSetContext**](/windows/win32/Dbghelp/nf-dbghelp-symsetcontext?branch=master)  
</dl>

 

 



