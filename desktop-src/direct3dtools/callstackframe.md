---
Description: Represents information about a frame on the callstack.
MS-HAID: vspixengine.CallStackFrame
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: CallStackFrame structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# <span id="vspixengine.callstackframe"></span>CallStackFrame structure

Represents information about a frame on the callstack.

## Syntax


```C++
} CallStackFrame;
```

## Members

**functionName**  
A COM string containing the name of the associated function.

**sourceFile**  
A COM string containing the filepath of the associated source file.

**moduleName**  
A COM string containing the name of the associated code module.

**lineNumber**  
The associated line number.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



