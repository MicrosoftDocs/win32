---
description: Represents a pipeline stage, including details of the shader used.
MS-HAID: vspixengine.PipeLineStage
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: PipeLineStage structure
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 616103CB-777E-4AA8-8B70-E19B1A2D667C
api_name: 
 - PipeLineStage
api_type: 
 - HeaderDef
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.pipelinestage"></span>PipeLineStage structure

Represents a pipeline stage, including details of the shader used.

## Syntax


```C++
} PipeLineStage;
```

## Members

**StageId**  
The ID of the pipeline stage.

**Debuggable**  
true if the pipeline stage supports debugging; otherwise, false.

**StageName**  
A COM string containing the name of the pipeline stage.

**GuaranteedOutput**  
true if the pipeline stage always has pipeline output; otherwise, false.

**DebugEntryPoint**  
A COM string containing the name of the shader entry point, if there is one.

**ShaderFile**  
A COM string containing the filepath of the shader source file.

**ShaderByteStreamPtr**  
A FILEPTR for the shader byte stream. This is passed back in order to debug.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



