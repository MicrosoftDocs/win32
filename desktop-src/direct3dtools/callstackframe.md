---
description: Represents information about a frame on the callstack.
MS-HAID: vspixengine.CallStackFrame
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: CallStackFrame structure
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 50941BA0-968D-4341-8BF5-854FBDE8BD0C
api_name: 
 - CallStackFrame
api_type: 
 - HeaderDef
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

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

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



