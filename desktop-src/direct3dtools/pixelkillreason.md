---
description: An enum used to indicate why a pixel was rejected.
MS-HAID: vspixengine.PIXELKILLREASON
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: PIXELKILLREASON enumeration
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 43836288-554B-430C-861D-AAC58DE3B282
api_name: 
 - PIXELKILLREASON
api_type: 
 - HeaderDef
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.pixelkillreason"></span>PIXELKILLREASON enumeration

An enum used to indicate why a pixel was rejected.

## Syntax


```C++
};
```

## Constants

<span id="PKR_NONE"></span><span id="pkr_none"></span>**PKR\_NONE**  
A value that indicates that the pixel was not rejected.

<span id="PKR_SHADERKILL"></span><span id="pkr_shaderkill"></span>**PKR\_SHADERKILL**  
A value that indicates that the pixel was rejected because the shader didn't run.

<span id="PKR_SCISSORTEST"></span><span id="pkr_scissortest"></span>**PKR\_SCISSORTEST**  
A value that indicates that the pixel was rejected because the scissor test failed.

<span id="PKR_ALPHATEST"></span><span id="pkr_alphatest"></span>**PKR\_ALPHATEST**  
A value that indicates that the pixel was rejected because the alpha test failed.

<span id="PKR_STENCILTEST"></span><span id="pkr_stenciltest"></span>**PKR\_STENCILTEST**  
A value that indicates that the pixel was rejected because the stencil test failed.

<span id="PKR_DEPTHTEST"></span><span id="pkr_depthtest"></span>**PKR\_DEPTHTEST**  
A value that indicates that the pixel was rejected because the depth test failed.

<span id="PKR_NOTCOMPUTABLE"></span><span id="pkr_notcomputable"></span>**PKR\_NOTCOMPUTABLE**  
A value that indicates that the pixel history can't be computed.

<span id="PKR_ERROR"></span><span id="pkr_error"></span>**PKR\_ERROR**  
A value that indicates that the pixel was rejected because of a general error.

<span id="PKR_NOINTERSECTION"></span><span id="pkr_nointersection"></span>**PKR\_NOINTERSECTION**  
A value that indicates that the pixel was rejected because the draw call does not intersect the pixel.

<span id="PKR_OCCLUDED"></span><span id="pkr_occluded"></span>**PKR\_OCCLUDED**  
A value that indicates that the pixel was rejected because the draw was occluded.

<span id="PKR_DEPTHSTENCILTEST"></span><span id="pkr_depthstenciltest"></span>**PKR\_DEPTHSTENCILTEST**  
A value that indicates that the pixel was rejected because the depth and stencil test failed.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



