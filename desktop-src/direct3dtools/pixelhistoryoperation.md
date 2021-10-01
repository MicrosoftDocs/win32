---
description: Represents information about pixel history.
MS-HAID: vspixengine.PixelHistoryOperation
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: PixelHistoryOperation structure
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 59DC72FC-3865-48D3-9F92-9BE93DCA093B
api_name: 
 - PixelHistoryOperation
api_type: 
 - HeaderDef
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.pixelhistoryoperation"></span>PixelHistoryOperation structure

Represents information about pixel history.

## Syntax


```C++
} PixelHistoryOperation;
```

## Members

**eid**  
The ID of the graphics event associated with this operation.

**PCP**  
Packed calls associated with this operation.

**renderTargetPtr**  
The render target originally associated (inside the captured application) with this operation.

**iPrim**  
The index of the actual primitive associated witht his operation.

**numPrims**  
The total number of primitives associated with this operation.

**numVertsPerPrim**  
The number of vertices per primitive.

**iInstance**  
When rendering instances, the instance number of the actual instance associated with this operation.

**iInstanceCount**  
When rendering instances, the total number of instances associated with this operation.

**bAssemblerStageGeneratesInstanceID**  
true if the input assembler generates instance IDs; otherwise false.

**flags**  
A combination of PIXELHISTORYFLAGS values. For more information, see the PIXELHISTORYFLAGS enumeration.

**pVSFile**  
A FILEPTR for the pixel shader byte stream. This is passed back in order to debug.

**pGSFile**  
A FILEPTR for the geometry shader byte stream. This is passed back in order to debug.

**pPSFile**  
A FILEPTR for the pixel shader byte stream. This is passed back in order to debug.

**pHSFile**  
A FILEPTR for the hull shader byte stream. This is passed back in order to debug.

**pDSFile**  
A FILEPTR for the domain shader byte stream. This is passed back in order to debug.

**pCSFile**  
A FILEPTR for the compute shader byte stream. This is passed back in order to debug.

**VertexShaderFile**  
A COM string containing the filepath of the vertex shader source file.

**PixelShaderFile**  
A COM string containing the filepath of the pixel shader source file.

**GeometryShaderFile**  
A COM string containing the filepath of the geometry shader source file.

**HullShaderFile**  
A COM string containing the filepath of the hull shader source file.

**DomainShaderFile**  
A COM string containing the filepath of the domain shader source file.

**psRed**  
Pixel shader output: value of red color component.

**psGreen**  
Pixel shader output: value of green color component.

**psBlue**  
Pixel shader output: value of blue color component

**psAlpha**  
Pixel shader output: value of alpha color component

**LabelPSRed**  
A COM string containing the name of the label associated with the red color component of the pixel shader output.

**LabelPSGreen**  
A COM string containing the name of the label associated with the green color component of the pixel shader output.

**LabelPSBlue**  
A COM string containing the name of the label associated with the blue color component of the pixel shader output.

**LabelPSAlpha**  
A COM string containing the name of the label associated with the alpha color component of the pixel shader output.

**pixelKillReason**  
Pixel shader output: reason the pixel output was killed.

**pixelOccluded**  
true if the pixel is occluded; otherwise, false.

**fbRed**  
Framebuffer: value of red color component of framebuffer before pixel shader output is merged.

**fbGreen**  
Framebuffer: value of green color component of framebuffer before pixel shader output is merged.

**fbBlue**  
Framebuffer: value of blue color component of framebuffer before pixel shader output is merged.

**fbAlpha**  
Framebuffer: value of alpha color component of framebuffer before pixel shader output is merged.

**LabelFBRed**  
A COM string containing the name of the label associated with the red color component of the framebuffer.

**LabelFBGreen**  
A COM string containing the name of the label associated with the green color component of the framebuffer.

**LabelFBBlue**  
A COM string containing the name of the label associated with the blue color component of the framebuffer.

**LabelFBAlpha**  
A COM string containing the name of the label associated with the alpha color component of the framebuffer.

**topology**  
The vertex topology of the draw calls (triangle list, triangle strip, etc).

**vertices**  
A COM string containing the vertex buffer starting at this primitive. The vertex buffer follows the input layout format specified in the pipeline stage.

**vertexSize**  
The size of a single vertex in bytes.

**InputLayout**  
A COM string containing a sequence of InputLayoutStruct structures associated with the draw call.

**HResult**  
The DirectX Hresult. In the event of a problem this can be used to display the error.

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



