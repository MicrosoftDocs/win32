---
Description: Represents the index of a texture slice.
MS-HAID: vspixengine.PixEngineTextureSliceIndex
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: PixEngineTextureSliceIndex structure
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
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

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



