---
title: VMDisplayVideoMode enumeration
description: The VMDisplayVideoMode enumeration specifies the display video mode.
ms.assetid: d1ca8b31-1aff-4d21-b1dc-0bcf868d9733
keywords:
- VMDisplayVideoMode enumeration Virtual Server
topic_type:
- apiref
api_name:
- VMDisplayVideoMode
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
api_location:
- VsComInterfaces.h
api_type:
- HeaderDef
---

# VMDisplayVideoMode enumeration

The **VMDisplayVideoMode** enumeration specifies the display video mode.

## Syntax


```C++
typedef enum  { 
  vmVideoMode_TextMode  = 0,
  vmVideoMode_CGAMode   = 1,
  vmVideoMode_VGAMode   = 2,
  vmVideoMode_SVGAMode  = 3
} VMDisplayVideoMode;
```



## Constants

<dl> <dt>

<span id="vmVideoMode_TextMode"></span><span id="vmvideomode_textmode"></span><span id="VMVIDEOMODE_TEXTMODE"></span>**vmVideoMode\_TextMode**
</dt> <dd>

Text mode.

</dd> <dt>

<span id="vmVideoMode_CGAMode"></span><span id="vmvideomode_cgamode"></span><span id="VMVIDEOMODE_CGAMODE"></span>**vmVideoMode\_CGAMode**
</dt> <dd>

CGA mode.

</dd> <dt>

<span id="vmVideoMode_VGAMode"></span><span id="vmvideomode_vgamode"></span><span id="VMVIDEOMODE_VGAMODE"></span>**vmVideoMode\_VGAMode**
</dt> <dd>

VGA mode.

</dd> <dt>

<span id="vmVideoMode_SVGAMode"></span><span id="vmvideomode_svgamode"></span><span id="VMVIDEOMODE_SVGAMODE"></span>**vmVideoMode\_SVGAMode**
</dt> <dd>

SVGA mode.

</dd> </dl>

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



 

 





