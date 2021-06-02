---
description: Represents information about a particular.
MS-HAID: vspixengine.PixelHistoryIntersection
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: PixelHistoryIntersection structure
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: D67A116D-B1D0-4E88-A2FF-611CDF4003B2
api_name: 
 - PixelHistoryIntersection
api_type: 
 - HeaderDef
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.pixelhistoryintersection"></span>PixelHistoryIntersection structure

Represents information about a particular

## Syntax


```C++
} PixelHistoryIntersection;
```

## Members

**frameNumber**  
The frame of the graphics event assocaited with this operation.

**eid**  
The ID of the graphics event associated with this operation.

**renderTargetPtr**  
The render target originally associated (inside the captured application) with this operation.

**eventType**  
The kind of event associated with this operation (specifically, whether this event is a draw call).

**point**  
The coordinates of the pixel in the framebuffer.

**bAssemblerStageGeneratesInstanceID**  
true if the input assembler generates instance IDs; otherwise false.

**flags**  
A combination of PIXELHISTORYFLAGS values. For more information, see the PIXELHISTORYFLAGS enumeration.

**fbInitialRed**  
Framebuffer: value of red color component of framebuffer before any pixel shader output is merged; that is, at the beginning of this frame.

**fbInitialGreen**  
Framebuffer: value of green color component of framebuffer before any pixel shader output is merged; that is, at the beginning of this frame.

**fbInitialBlue**  
Framebuffer: value of blue color component of framebuffer before any pixel shader output is merged; that is, at the beginning of this frame.

**fbInitialAlpha**  
Framebuffer: value of alpha color component of framebuffer before any pixel shader output is merged; that is, at the beginning of this frame.

**LabelFBInitialRed**  
A COM string containing the name of the label associated with the red color component of the framebuffer before any pixel shading; that is, at the beginning of this frame.

**LabelFBInitialGreen**  
A COM string containing the name of the label associated with the green color component of the framebuffer before any pixel shading; that is, at the beginning of this frame.

**LabelFBInitialBlue**  
A COM string containing the name of the label associated with the blue color component of the framebuffer before any pixel shading; that is, at the beginning of this frame.

**LabelFBInitialAlpha**  
A COM string containing the name of the label associated with the alpha color component of the framebuffer before any pixel shading; that is, at the beginning of this frame.

**fbRed**  
Framebuffer: value of red color component of framebuffer after all pixel shader output is merged; that is, the final framebuffer color.

**fbGreen**  
Framebuffer: value of green color component of framebuffer after all pixel shader output is merged; that is, the final framebuffer color.

**fbBlue**  
Framebuffer: value of blue color component of framebuffer after all pixel shader output is merged; that is, the final framebuffer color.

**fbAlpha**  
Framebuffer: value of alpha color component of framebuffer after all pixel shader output is merged; that is, the final framebuffer color.

**LabelFBRed**  
A COM string containing the name of the label associated with the red color component of the framebuffer after all pixel shading; that is, the final framebuffer color.

**LabelFBGreen**  
A COM string containing the name of the label associated with the green color component of the framebuffer after all pixel shading; that is, the final framebuffer color.

**LabelFBBlue**  
A COM string containing the name of the label associated with the blue color component of the framebuffer after all pixel shading; that is, the final framebuffer color.

**LabelFBAlpha**  
A COM string containing the name of the label associated with the alpha color component of the framebuffer after all pixel shading; that is, the final framebuffer color.

**pixelKillReason**  
Specifies the reason that the pixel's color contribution was killed.

**HResult**  
If an error occurred, contains the DirectX HRESULT that specifies the error.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



