---
description: Represents a description of a texture slice.
MS-HAID: vspixengine.PixEngineTextureSliceDescriptor
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: PixEngineTextureSliceDescriptor structure
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 1A183AFB-0BEF-4474-A60C-DBCFA4B34604
api_name: 
 - PixEngineTextureSliceDescriptor
api_type: 
 - HeaderDef
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

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

 

 



