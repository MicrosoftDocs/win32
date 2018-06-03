---
title: symbols
description: Enables and configures symbol decoding support.
ms.assetid: 1a49cb0b-5757-4625-b555-0b7bb0c75a1d
keywords:
- symbols Windows Performance Analyzer
topic_type:
- apiref
api_name:
- symbols
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# symbols

Enables and configures symbol decoding support.

``` syntax
-symbols [cacheonly] [verbose] [dbghelplog]
```

## Parameters

<dl> <dt>

<span id="_______cacheonly_______"></span><span id="_______CACHEONLY_______"></span> **cacheonly** 
</dt> <dd>

Use the symcache, but not DbgHelp. This option is used to speed up symbol decoding for traces with many binary images missing symbol files once all interesting symbol files have been transcoded.

</dd> <dt>

<span id="_______verbose______"></span><span id="_______VERBOSE______"></span> **verbose** 
</dt> <dd>

Verbose mode. Print configuration.

</dd> <dt>

<span id="_______dbghelplog______"></span><span id="_______DBGHELPLOG______"></span> **dbghelplog** 
</dt> <dd>

Enable DbgHelp debug log on **stderr**.

If action symbols is not specified on the command line, symbol decoding is disabled.

The symbol decoding support uses the following environment variables for further configuration of DbgHelp and SymCache:



|                                  |                                                                                                                                                                                    |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \_NT\_SYMBOL\_PATH <br/>   | Specifies the path DbgHelp should search to locate symbols files (.PDB) corresponding to binary images files used in the trace. See Note below regarding this variable.<br/> |
| \_NT\_SYMCACHE\_PATH <br/> | Specifies the path to the local symcache directory. By default, \\SymCache will be used.<br/>                                                                                |



 

</dd> </dl>

### Comments

For symbol decoding, the trace must be a kernel trace (or a user trace processed in conjunction with a kernel trace) that has the PROC\_THREAD+LOADER kernel flags enabled and has been stopped and merged with -d or merged with -merge on the same machine it was taken on. \[xperf performs a special image identification process during its custom trace merge.\]

Microsoft Symbol Server-based configuration set \_NT\_SYMBOL\_PATH=srv\*%SystemDrive%\\symbols\*http://msdl.microsoft.com/download/symbols

Configure SymCache to always use the System drive: set \_NT\_SYMCACHE\_PATH=%SystemDrive%\\SymCache

If you have any non-Microsoft applications installed, add the path to their symbols to the path for OS symbols: set \_NT\_SYMBOL\_PATH=srv\*%SystemDrive%\\symbols\*http://msdl.microsoft.com/download/symbols;C:\\MyPrivates.

 

 





