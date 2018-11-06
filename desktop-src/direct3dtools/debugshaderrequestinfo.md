---
Description: Represents information about a shader debugger request.
MS-HAID: vspixengine.DebugShaderRequestInfo
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: DebugShaderRequestInfo structure
ms.topic: structure
ms.date: 05/31/2018
---

# <span id="vspixengine.debugshaderrequestinfo"></span>DebugShaderRequestInfo structure

Represents information about a shader debugger request.

## Syntax


```C++
} DebugShaderRequestInfo;
```

## Members

**stage**  
The pipeline stage to debug.

**eventID**  
The ID of the graphics event to debug.

**frameNumber**  
The frame to debug.

**vertex**  
The vertex to debug.

**pixel**  
The pixel to debug.

**groupCoordinates**  
The coordinates of the group to debug.

**threadCoordinates**  
The coordinates of the thread to debug

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



