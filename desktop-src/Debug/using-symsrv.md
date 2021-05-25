---
description: Using SymSrv
ms.assetid: d400f222-c50c-4c7b-8f8a-0c3ed3bba3b9
title: Using SymSrv
ms.topic: article
ms.date: 05/31/2018
---

# Using SymSrv

SymSrv delivers symbol files from centralized symbol stores. These stores can contain any number of symbol files, corresponding to any number of programs or operating systems. The stores can also contain binary files, which are particularly useful when debugging minidump files.

The stores can contain the actual symbol and binary files or simply pointers to symbol files. If the store contains pointers, SymSrv will retrieve the actual files directly from their sources.

SymSrv can also separate a large symbol store into a smaller subset that is appropriate for a specialized debugging task.

Finally, SymSrv can obtain symbol files from an HTTP or HTTPS source using the logon information provided by the operating system. SymSrv supports HTTPS sites protected by smartcards, certificates, and regular logins and passwords.

## Setting the Symbol Path

As described in [Symbol Paths](symbol-paths.md), the symbol path (\_NT\_SYMBOL\_PATH environment variable) can be made up of several path elements separated by semicolons. If any one or more of these path elements begins with the text "srv\*", then the element is a symbol server and will use SymSrv to locate symbol files.

> [!Note]  
> If the "srv\*" text is not specified but the actual path element is a symbol server store, then the symbol handler will act as if "srv\*" were specified. The symbol handler makes this determination by searching for the existence of a file called "pingme.txt" in the root directory of the specified path.

 

Just as symbol paths are made up of symbol path elements separated by semicolons, symbol servers are made up of symbol store elements separated by asterisks. There can be up to 10 symbol stores after the "srv\*" prefix. Stores listed to the left of the list are called *downstream* stores and stores to the right are called *upstream* stores.

<dl> srv\**SymbolStore*  
srv\**SymbolStore1*\**SymbolStoreN*  
</dl>

If only one symbol store element is included in the path, then SymSrv will attempt to use the any requested file directly from that store.

If there are two symbol stores in the path, SymSrv looks for the symbol file in the leftmost symbol store. If the file is there, it is used. If it is not there, SymSrv looks in the symbol store immediately to the right. If the file is there, it is copied to the left store and opened from there.

If there are more than two stores, this behavior continues to the right until the file is found or there are no more stores in the list.

The file is never opened from any store but the leftmost store. If the file is found anywhere else in the chain, it is copied to every store to the left of it. This copy process is called "cascading" and provides certain benefits that will clarfied later in this document.

## Types of Symbol Stores

The following table displays examples of the supported symbol store types.

|  Symbol store type       |  Description |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \\\\server\\share          | A fully qualified UNC path to a share on a remote server.                                                                                                                                                                                                                                                                                                 |
| c:\\LocalCache             | A path to a directory on the client computer.                                                                                                                                                                                                                                                                                                             |
| https://InternetSite        | The URL to a web site hosting the symbols. Must be the rightmost store in the list and should not be the only store in the list.                                                                                                                                                                                                                          |
| https://SecureInternetSite | The URL to a secure web site hosting the symbols. This can support passwords, Windows login credentials, certificates, and smartcards. Must be the rightmost store in the list and should not be the only store in the list.                                                                                                                              |
| <blank>              | If there is no text between two asterisks, this indicates the *default downstream store*. The location is set by calling [**SymSetHomeDirectory**](/windows/desktop/api/Dbghelp/nf-dbghelp-symsethomedirectory). The default value is a directory named "sym" immediately below the program directory of the calling application. This is sometimes referred to as the *default local cache*. |



 

Because an HTTP-based symbol store cannot be written to, it must be the rightmost store in the list. If an HTTP-based symbol store was located in the middle or the left of the store list, it would not be possible to copy any found files to it and the chain would be broken. Furthermore, because the symbol handler cannot open a file from a web site, an HTTP-based store should not be the leftmost or only store on the list. If SymSrv is ever presented with this symbol path, it will attempt to recover by copying the file to the default downstream store and open it from there, regardless of whether the default downstream store is indicated in the symbol path or not.

## Examples

To use SymSrv with a symbol store on \\\\mybuilds\\mysymbols, set the following symbol path:

**set \_NT\_SYMBOL\_PATH= srv\*\\\\mybuilds\\mysymbols**

To set the symbol path so that the debugger will copy symbol files from a symbol store on \\\\mybuilds\\mysymbols to your local directory c:\\localsymbols, use:

**set \_NT\_SYMBOL\_PATH=srv\*c:\\localsymbols\*\\\\mybuilds\\mysymbols**

To set the symbol path so that the debugger will copy symbol files from a symbol store on \\\\mybuilds\\mysymbols to the default downstream store (typically c:\\debuggers\\sym), use:

**set \_NT\_SYMBOL\_PATH=srv\*\*\\\\mybuilds\\mysymbols**

To use a cascading store, set the following symbol path:

**set \_NT\_SYMBOL\_PATH = srv\*c:\\localsymbols\*\\\\NearbyServer\\store\*https://DistantServer**

In this example, SymSrv first looks for the file in c:\\localsymbols. If it is found there, it will return a path to the file. Otherwise, SymSrv looks for the file in \\\\NearbyServer\\store. If it is found there, SymSrv copies the file to c:\\localsymbols and returns a path to the file; if it is not found, SymSrv looks for the file in https://DistantServer, and if it is found there, SymSrv copies the file to \\\\NearbyServer\\store, then to c:\\localsymbols.

This last example shows how judicious design of a symbol path can be used to optimize the downloading of symbols. If you have a work site with a group of debuggers and they all need to get symbols from a distant location, you can set up a common server with a symbol store near all the debuggers. Then setup every debugger with the symbol path above. The first debugger that requires a certain version of foo.pdb will download it from https://DistantServer to \\\\NearbyServer\\store and then to its own machine in c:\\localsymbols. The next debugger that requires the same file will be able to download it from \\\\NearbyServer\\store because it was already downloaded to that location by the previous debugger. This multi-level caching saves significant time and network bandwidth.

## Microsoft Symbol Store

Microsoft provides access to an Internet symbol server that contains symbol files for the many versions of the Windows operating system. This catalog of symbols is not guaranteed to be complete, but it is extensive. Other Microsoft products are also represented.

The Internet symbol server is populated with a variety of Windows symbols for Microsoft Windows operating systems, including hot fixes, Service Packs, Security Rollup Packages, and retail releases. Symbols are also available on the server for current Betas and Release Candidates for Windows products, plus a variety of other Microsoft products, such as Microsoft Internet Explorer.

If you have access to the Internet during debugging, you can configure the debugger to download symbols as needed during a debugging session, rather than downloading symbol files separately before a debugging session. The symbols are downloaded to a directory location that you specify and then the debugger loads them from there.

The URL for the Microsoft symbol store is https://msdl.microsoft.com/download/symbols. The following example shows how to set the debugger symbol path (substitute your downstream store path for *c:\\DownstreamStore*):

``` syntax
srv*c:\DownstreamStore*https://msdl.microsoft.com/download/symbols
```

## Compressed Files

SymSrv is compatible with symbol stores that contain compressed files, as long as this compression has been preformed with the compress.exe tool that was distributed with the Windows Server 2003 Resource Kit. Compressed files should have an underscore as the last character in their file extensions (for example, module1.pd\_ or module2.db\_). For details, see [Using SymStore](using-symstore.md).

When cascading, files are not uncompressed unless the target store is the leftmost store in the path. If there is only one store in the path and it contains a compressed file, SymSrv will copy the file to the default downstream store and open it from there, even though the default downstream store is not indicated in they symbol path.

**DbgHelp 6.1 and earlier.:** If the files in the master store are compressed, you must use a downstream store. SymSrv will uncompress all files before copying them to the downstream store.

## Deleting the Cache

If you are using a downstream store as a cache, you can delete this directory at any time to save disk space.

It is possible to have a vast symbol store that includes symbol files for many different programs or Windows versions. If you upgrade the version of Windows used on your target computer, the cached symbol files will all match the earlier version. These cached files will not be of any further use, and therefore this might be a good time to delete the cache.

Debugging Tools for Windows comes with a utility called agestore.exe that will selectively remove files from a directory tree, leaving the most recently used files. This tool is designed for pruning out unused files from symbol server stores. It allows you to control many options including cut off date and directory size algorithms.

## Flat Cache Directory

It is possible to declare the default downstream store as a flat directory, rather than a standard symbol tree structure. To do so, call the [**SymSetOptions**](/windows/desktop/api/Dbghelp/nf-dbghelp-symsetoptions) function with **SYMOPT\_FLAT\_DIRECTORY** (this also sets the **SSRVOPT\_FLAT\_DEFAULT\_STORE** option in SymSrv). Be sure to call [**SymSetHomeDirectory**](/windows/desktop/api/Dbghelp/nf-dbghelp-symsethomedirectory) before doing so; otherwise, the symbol files can be written to the program directory.

## Pointer Files

SymStore can create and use files that point to a target file rather than the target file itself. If a symbol store contains such a pointer file, the default is to copy the file from the location indicated in the pointer file to the store. To configure a store such that the pointer file is copied instead of the file it points to, create a file named wantsptr.txt in the root of the target store. The contents of wantsptr.txt are not important, only the presence of the file.

## Excluding Files from Symbols List

To exclude files from a symbols search, you can specify their names in symsrv.ini or in the registry. To specify the files in symsrv.ini, create a section named Exclusions and list the files. The file names can contain wildcards, as shown in the following example:

``` syntax
[Exclusions]
dbghelp.pdb
symsrv.*
mso*
```

Symsrv.ini should be located in the same directory that symsrv.dll resides. In most installations, the file does not exist and you will need to create a new one.

Alternatively, you can store the files to be excluded in the registry. Create the following registry key: **HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Symbol Server\\Exclusions**. Store each file name as a string value (REG\_SZ) within this key. The name of the string value specifies the name of the file to be excluded. You can use the contents of the string value to store a comment describing why the file is being excluded.

## Installation

The SymSrv (symsrv.dll) symbol server is included in the Debugging Tools for Windows package. It must be installed in the same directory as the copy of dbghelp.dll that you are loading. For more details, see [Calling the DbgHelp Library](calling-the-dbghelp-library.md).

 

 



