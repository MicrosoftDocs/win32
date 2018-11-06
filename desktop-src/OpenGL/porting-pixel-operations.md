---
title: Porting Pixel Operations
description: Porting Pixel Operations
ms.assetid: 57917f33-daf5-4db6-9583-ab596deab91a
keywords:
- IRIS GL porting,pixels
- porting from IRIS GL,pixels
- porting to OpenGL from IRIS GL,pixels
- OpenGL porting from IRIS GL,pixels
- pixels,porting from IRIS GL
ms.topic: article
ms.date: 05/31/2018
---

# Porting Pixel Operations

When porting code that involves pixel operations, keep the following points in mind:

-   Logical pixel operations are not applied to RGBA color buffers. For more information, see [**glLogicOp**](gllogicop.md).
-   In general, IRIS GL uses the format ABGR for pixels, whereas OpenGL uses RGBA. You can change the format with [**glPixelStore**](glpixelstore-functions.md).
-   When porting **lrectwrite** functions, be careful to note where **lrectwrite** is writing (for example, it could be writing to the depth buffer).

OpenGL gives you some additional flexibility in pixel operations. The following table lists IRIS GL functions for pixel operations and their equivalent OpenGL functions.



| IRIS GL function                                   | OpenGL function                                                                           | Meaning                                                                 |
|----------------------------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| **lrectread**, **rectread**,**readRGB**<br/> | [**glReadPixels**](glreadpixels.md)                                                      | Reads a block of pixels from the framebuffer.                           |
| **lrectwrite**, **rectwrite**                      | [**glDrawPixels**](gldrawpixels.md)                                                      | Writes a block of pixels to the framebuffer.                            |
| **rectcopy**                                       | [**glCopyPixels**](glcopypixels.md)                                                      | Copies pixels in the framebuffer.                                       |
| **rectzoom**                                       | [**glPixelZoom**](glpixelzoom.md)                                                        | Specifies pixel zoom factors for **glDrawPixels** and **glCopyPixels**. |
| **cmov**                                           | [glRasterPos](glrasterpos-functions.md)                                                  | Specifies raster position for pixel operations.                         |
| **readsource**                                     | [**glReadBuffer**](glreadbuffer.md)                                                      | Selects a color buffer source for pixels.                               |
| **pixmode**                                        | [**glPixelStore**](glpixelstore-functions.md),[**glPixelTransfer**](glpixeltransfer.md) | Sets pixel storage modes.Set pixel transfer modes.                      |
| **logicop**                                        | [**glLogicOp**](gllogicop.md)                                                            | Specifies a logical operation for pixel writes.                         |
|                                                    | [**glEnable**](glenable.md) ( GL\_LOGIC\_OP )                                            | Turns on pixel logic operations.                                        |



 

For a complete list of possible logical operations, see [**glLogicOp**](gllogicop.md).

This IRIS GL code sample shows a typical pixel write:

``` syntax
unsigned long *packedRaster; 
.. 
packedRaster[k] = 0x00000000; 
.. 
lrectwrite(0, 0, xSize, ySize, packedRaster);
```

The preceding code looks like this when translated to OpenGL:

``` syntax
glRasterPos2i( 0, 0); 
glDrawPixels( xSize + 1, ySize + 1, GL_RGBA, GL_UNSIGNED_BYTE, packedRaster);
```

 

 





