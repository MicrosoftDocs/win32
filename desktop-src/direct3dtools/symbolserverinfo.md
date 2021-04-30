---
description: Represents information about the debug symbol server.
MS-HAID: vspixengine.SymbolServerInfo
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: SymbolServerInfo structure
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: D57D87E4-BA94-4C6F-9D5F-999C61F4DD6F
api_name: 
 - SymbolServerInfo
api_type: 
 - HeaderDef
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.symbolserverinfo"></span>SymbolServerInfo structure

Represents information about the debug symbol server.

## Syntax


```C++
} SymbolServerInfo;
```

## Members

**symbolPath**  
A COM string containing the path of the symbol server.

**symbolCacheDir**  
A COM string containing the cache directory of the symbol server.

**publicSymbolServerName**  
A COM string containing the public name of the symbol server.

**symbolExcludeList**  
A COM string that specifies the list of symbols to exclude.

**symbolIncludeList**  
A COM string that specifies the list of symbols to include.

**useExcludeList**  
true if the exclude list is ignored; otherwise, false.

**useMSSymbolServer**  
true if using Microsoft symbol server; otherwise, false.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



