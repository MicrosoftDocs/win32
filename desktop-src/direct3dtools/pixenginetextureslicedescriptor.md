---
Description: Represents a description of a texture slice.
MS-HAID: vspixengine.PixEngineTextureSliceDescriptor
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: PixEngineTextureSliceDescriptor structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# <span id="vspixengine.pixenginetextureslicedescriptor"></span>PixEngineTextureSliceDescriptor structure

Represents a description of a texture slice.

## Syntax


```C++
} PixEngineTextureSliceDescriptor;
```

## Members

**width**  
The width (number of samples in the X axis) of the slice.

**height**  
The height (number of samples in the Y axis) of the slice.

**blockRowBytes**  
The number of bytes per row in each block.

**offset**  
The offset of the slice within the whole texture.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



