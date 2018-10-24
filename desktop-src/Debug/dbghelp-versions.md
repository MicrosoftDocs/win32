---
Description: The DbgHelp library is implemented by DbgHelp.dll.
ms.assetid: 8ef1740d-c791-4fbd-8297-7207a987c09d
title: DbgHelp Versions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

[**EnumerateLoadedModulesEx**](/windows/desktop/api/Dbghelp/nf-dbghelp-enumerateloadedmodulesex)  
[**SymAddSourceStream**](/windows/desktop/api/Dbghelp/nf-dbghelp-symaddsourcestream)  
[**SymEnumTypesByName**](/windows/desktop/api/Dbghelp/nf-dbghelp-symenumtypesbyname)  
[**SymGetOmaps**](/windows/desktop/api/Dbghelp/nf-dbghelp-symgetomaps)  
[**SymGetSourceVarFromToken**](/windows/desktop/api/Dbghelp/nf-dbghelp-symgetsourcevarfromtoken)  
[**SymSetScopeFromAddr**](/windows/desktop/api/Dbghelp/nf-dbghelp-symsetscopefromaddr)  
[**SymSetScopeFromIndex**](/windows/desktop/api/Dbghelp/nf-dbghelp-symsetscopefromindex)  
</dl>

## Version 6.6

The following functions were added to DbgHelp version 6.6.<dl>

[**SymFindDebugInfoFile**](/windows/desktop/api/Dbghelp/nf-dbghelp-symfinddebuginfofile)  
[**SymFindExecutableImage**](/windows/desktop/api/Dbghelp/nf-dbghelp-symfindexecutableimage)  
[**SymSrvGetFileIndexInfo**](/windows/desktop/api/Dbghelp/nf-dbghelp-symsrvgetfileindexinfo)  
</dl>

## Version 6.5

The following function was added to DbgHelp version 6.5.<dl>

[**SymRefreshModuleList**](/windows/desktop/api/Dbghelp/nf-dbghelp-symrefreshmodulelist)  
</dl>

The following structures were added to DbgHelp version 6.5.<dl>

[**MINIDUMP\_HANDLE\_DESCRIPTOR\_2**](/windows/desktop/api/minidumpapiset/ns-minidumpapiset-_minidump_handle_descriptor_2)  
[**MINIDUMP\_HANDLE\_OBJECT\_INFORMATION**](/windows/desktop/api/minidumpapiset/ns-minidumpapiset-_minidump_handle_object_information)  
[**MINIDUMP\_HANDLE\_OPERATION\_LIST**](/windows/desktop/api/minidumpapiset/ns-minidumpapiset-_minidump_handle_operation_list)  
[**MINIDUMP\_IO\_CALLBACK**](/windows/desktop/api/minidumpapiset/ns-minidumpapiset-_minidump_io_callback)  
[**MINIDUMP\_MISC\_INFO\_2**](/windows/desktop/api/minidumpapiset/ns-minidumpapiset-_minidump_misc_info_2)  
[**MINIDUMP\_READ\_MEMORY\_FAILURE\_CALLBACK**](/windows/desktop/api/minidumpapiset/ns-minidumpapiset-_minidump_read_memory_failure_callback)  
</dl>

## Version 6.4

The following function was added to DbgHelp version 6.4.<dl>

[**SymEnumSourceLines**](/windows/desktop/api/DbgHelp/nf-dbghelp-symenumsourcelines)  
</dl>

## Version 6.3

DbgHelp version 6.3 adds Unicode support to many of the existing functions. To enable this support, define DBGHELP\_TRANSLATE\_TCHAR at the top of each source file or when you compile your application.

The following functions were added to DbgHelp version 6.3.<dl>

[**SymEnumProcesses**](/windows/desktop/api/DbgHelp/nf-dbghelp-symenumprocesses)  
[**SymGetSymbolFile**](/windows/desktop/api/Dbghelp/nf-dbghelp-symgetsymbolfile)  
[**SymGetTypeInfoEx**](/windows/desktop/api/Dbghelp/nf-dbghelp-symgettypeinfoex)  
[**SymSrvDeltaName**](/windows/desktop/api/DbgHelp/nf-dbghelp-symsrvdeltaname)  
[**SymSrvGetFileIndexes**](/windows/desktop/api/DbgHelp/nf-dbghelp-symsrvgetfileindexes)  
[**SymSrvGetFileIndexString**](/windows/desktop/api/DbgHelp/nf-dbghelp-symsrvgetfileindexstring)  
[**SymSrvGetSupplement**](/windows/desktop/api/DbgHelp/nf-dbghelp-symsrvgetsupplement)  
[**SymSrvIsStore**](/windows/desktop/api/DbgHelp/nf-dbghelp-symsrvisstore)  
[**SymSrvStoreFile**](/windows/desktop/api/DbgHelp/nf-dbghelp-symsrvstorefile)  
[**SymSrvStoreSupplement**](/windows/desktop/api/DbgHelp/nf-dbghelp-symsrvstoresupplement)  
</dl>

The following structures were added to DbgHelp version 6.3.<dl>

[**MINIDUMP\_MEMORY\_INFO**](/windows/desktop/api/minidumpapiset/ns-minidumpapiset-_minidump_memory_info)  
[**MINIDUMP\_MEMORY\_INFO\_LIST**](/windows/desktop/api/minidumpapiset/ns-minidumpapiset-_minidump_memory_info_list)  
[**MINIDUMP\_THREAD\_INFO**](/windows/desktop/api/minidumpapiset/ns-minidumpapiset-_minidump_thread_info)  
[**MINIDUMP\_THREAD\_INFO\_LIST**](/windows/desktop/api/minidumpapiset/ns-minidumpapiset-_minidump_thread_info_list)  
</dl>

DbgHelp 6.3 also supports [Source Server](source-server-and-source-indexing.md).

## Version 6.2

The following functions were added to DbgHelp version 6.2.<dl>

[**SymEnumSourceFiles**](/windows/desktop/api/DbgHelp/nf-dbghelp-symenumsourcefiles)  
[**SymFromIndex**](/windows/desktop/api/Dbghelp/nf-dbghelp-symfromindex)  
[**SymGetScope**](/windows/desktop/api/Dbghelp/nf-dbghelp-symgetscope)  
[**SymGetSourceFile**](/windows/desktop/api/Dbghelp/nf-dbghelp-symgetsourcefile)  
[**SymGetSourceFileFromToken**](/windows/desktop/api/Dbghelp/nf-dbghelp-symgetsourcefilefromtoken)  
[**SymGetSourceFileToken**](/windows/desktop/api/Dbghelp/nf-dbghelp-symgetsourcefiletoken)  
[**SymMatchString**](/windows/desktop/api/DbgHelp/nf-dbghelp-symmatchstring)  
[**SymNext**](/windows/desktop/api/DbgHelp/nf-dbghelp-symnext)  
[**SymPrev**](/windows/desktop/api/DbgHelp/nf-dbghelp-symprev)  
[**SymSearch**](/windows/desktop/api/Dbghelp/nf-dbghelp-symsearch)  
</dl>

## Version 6.1

The following functions were added to DbgHelp version 6.1.<dl>

[**SymEnumLines**](/windows/desktop/api/Dbghelp/nf-dbghelp-symenumlines)  
[**SymFromToken**](/windows/desktop/api/Dbghelp/nf-dbghelp-symfromtoken)  
[**SymGetHomeDirectory**](/windows/desktop/api/Dbghelp/nf-dbghelp-symgethomedirectory)  
[**SymSetHomeDirectory**](/windows/desktop/api/Dbghelp/nf-dbghelp-symsethomedirectory)  
</dl>

## Versions 5.2 and 6.0

The following functions were added to DbgHelp versions 5.2 and 6.0.<dl>

[**EnumDirTree**](/windows/desktop/api/Dbghelp/nf-dbghelp-enumdirtree)  
[**SymAddSymbol**](/windows/desktop/api/Dbghelp/nf-dbghelp-symaddsymbol)  
[**SymDeleteSymbol**](/windows/desktop/api/Dbghelp/nf-dbghelp-symdeletesymbol)  
[**SymEnumSymbolsForAddr**](/windows/desktop/api/Dbghelp/nf-dbghelp-symenumsymbolsforaddr)  
[**SymLoadModuleEx**](/windows/desktop/api/Dbghelp/nf-dbghelp-symloadmoduleex)  
[**SymSetParentWindow**](/windows/desktop/api/Dbghelp/nf-dbghelp-symsetparentwindow)  
</dl>

The following structures were added to DbgHelp version 5.2 and 6.0.<dl>

[**MINIDUMP\_MISC\_INFO**](/windows/desktop/api/minidumpapiset/ns-minidumpapiset-_minidump_misc_info)  
[**MINIDUMP\_UNLOADED\_MODULE**](/windows/desktop/api/minidumpapiset/ns-minidumpapiset-_minidump_unloaded_module)  
[**MINIDUMP\_UNLOADED\_MODULE\_LIST**](/windows/desktop/api/minidumpapiset/ns-minidumpapiset-_minidump_unloaded_module_list)  
[**MODLOAD\_DATA**](/windows/desktop/api/DbgHelp/ns-dbghelp-_modload_data)  
</dl>

## Versions 4.0 and 5.1

The following functions were added to DbgHelp versions 4.0 and 5.1.<dl>

[**MiniDumpReadDumpStream**](/windows/desktop/api/minidumpapiset/nf-minidumpapiset-minidumpreaddumpstream)  
[**MiniDumpWriteDump**](/windows/desktop/api/minidumpapiset/nf-minidumpapiset-minidumpwritedump)  
[**SymbolServer**](https://msdn.microsoft.com/library/ms680667(v=VS.85).aspx)  
[**SymbolServerClose**](https://msdn.microsoft.com/library/ms680672(v=VS.85).aspx)  
[**SymbolServerGetOptions**](https://msdn.microsoft.com/library/ms680674(v=VS.85).aspx)  
[**SymbolServerSetOptions**](https://msdn.microsoft.com/library/ms680676(v=VS.85).aspx)  
[**SymEnumSymbols**](/windows/desktop/api/Dbghelp/nf-dbghelp-symenumsymbols)  
[**SymEnumTypes**](/windows/desktop/api/Dbghelp/nf-dbghelp-symenumtypes)  
[**SymFindFileInPath**](/windows/desktop/api/DbgHelp/nf-dbghelp-symfindfileinpath)  
[**SymFromAddr**](/windows/desktop/api/Dbghelp/nf-dbghelp-symfromaddr)  
[**SymFromName**](/windows/desktop/api/Dbghelp/nf-dbghelp-symfromname)  
[**SymGetFileLineOffsets64**](/windows/desktop/api/Dbghelp/nf-dbghelp-symgetfilelineoffsets64)  
[**SymGetTypeFromName**](/windows/desktop/api/Dbghelp/nf-dbghelp-symgettypefromname)  
[**SymGetTypeInfo**](/windows/desktop/api/Dbghelp/nf-dbghelp-symgettypeinfo)  
[**SymSetContext**](/windows/desktop/api/Dbghelp/nf-dbghelp-symsetcontext)  
</dl>

 

 



