---
description: An enum containing flags used to describe a pixel history result. See PixelHistoryOperation.
MS-HAID: vspixengine.PIXELHISTORYFLAGS
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: PIXELHISTORYFLAGS enumeration
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: BDB88A2D-016A-4E15-B47A-870A2959E943
api_name: 
 - PIXELHISTORYFLAGS
api_type: 
 - HeaderDef
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.pixelhistoryflags"></span>PIXELHISTORYFLAGS enumeration

An enum containing flags used to describe a pixel history result. See PixelHistoryOperation.

## Syntax


```C++
};
```

## Constants

<span id="PHF_INITIALVALUE"></span><span id="phf_initialvalue"></span>**PHF\_INITIALVALUE**  
A flag that corresponds to the initial color value (prior to frame).

<span id="PHF_CLEAR"></span><span id="phf_clear"></span>**PHF\_CLEAR**  
A flag that corresponds to the clear color result.

<span id="PHF_DRAW"></span><span id="phf_draw"></span>**PHF\_DRAW**  
A flag that corresponds to the draw color result.

<span id="PHF_FINALVALUE"></span><span id="phf_finalvalue"></span>**PHF\_FINALVALUE**  
A flag that corresponds to the final color result.

<span id="PHF_HASCOLOR"></span><span id="phf_hascolor"></span>**PHF\_HASCOLOR**  
A flag that corresponds to whether the color result is present in the PixelHistoryOperation struct.

<span id="PHF_HASFBCOLOR"></span><span id="phf_hasfbcolor"></span>**PHF\_HASFBCOLOR**  
A flag that corresponds to whether the final buffer color result is present in the PixelHistoryOperation struct.

<span id="PHF_ERROR"></span><span id="phf_error"></span>**PHF\_ERROR**  

<span id="PHF_VERTEXPROCESSINGSKIPPED"></span><span id="phf_vertexprocessingskipped"></span>**PHF\_VERTEXPROCESSINGSKIPPED**  
Not used.

<span id="PHF_MODIFYRESOURCE"></span><span id="phf_modifyresource"></span>**PHF\_MODIFYRESOURCE**  

<span id="PHF_CANNOTRUNFULLDEPTHSTENCILTEST"></span><span id="phf_cannotrunfulldepthstenciltest"></span>**PHF\_CANNOTRUNFULLDEPTHSTENCILTEST**  
A flag that corresponds to not being able to run the depth or stencil test.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



