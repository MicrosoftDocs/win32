---
description: Represents the index of a texture slice.
MS-HAID: vspixengine.PixEngineTextureSliceIndex
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: PixEngineTextureSliceIndex structure
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 127765F7-4EBF-4B66-9491-A6FE9DC673C8
api_name: 
 - PixEngineTextureSliceIndex
api_type: 
 - HeaderDef
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.pixenginetexturesliceindex"></span>PixEngineTextureSliceIndex structure

Represents the index of a texture slice

## Syntax


```C++
} PixEngineTextureSliceIndex;
```

## Members

**arrayIndex**  
When the texture is a texture array, the array index of the slice.

**mipmapLevel**  
The mipmap level of the slice.

**sampleIndex**  
The sample index of the slice.

**zSlice**  
The depth (z) of the slice.

## Requirements

<table><colgroup><col  /><col  /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



