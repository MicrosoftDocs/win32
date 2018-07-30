---
Description: Represents a description of a texture format.
MS-HAID: vspixengine.PixEngineTextureFormatDesc
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: PixEngineTextureFormatDesc structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# <span id="vspixengine.pixenginetextureformatdesc"></span>PixEngineTextureFormatDesc structure

Represents a description of a texture format.

## Syntax


```C++
} PixEngineTextureFormatDesc;
```

## Members

**dxgiFormat**  
The DXGI format of the texture.

**dataFormat**  
The data format of the texture.

**blockBytes**  
The number of bytes in a data block.

**blockHeight**  
The height (number samples in the Y axis) of the block.

**blockWidth**  
The width (number of samples in the X axis) of the block.

**channelX**  
Describes properties of the X channel. For more information, see the PixEngineChannelDescription structure.

**channelY**  
Describes properties of the Y channel. For more information, see the PixEngineChannelDescription structure.

**channelZ**  
Describes properties of the Z channel. For more information, see the PixEngineChannelDescription structure.

**channelW**  
Describes properties of the W channel. For more information, see the PixEngineChannelDescription structure.

**swizzle**  
Describes the swizzle (channel-swapping) applied to the sample.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



