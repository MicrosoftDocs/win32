---
title: Porting Color Calls
description: The following table lists IRIS GL color functions and their equivalent OpenGL functions.
ms.assetid: 4ca6c311-d6c8-4d10-9e9c-770a8e6de4bb
keywords:
- IRIS GL porting,color
- porting from IRIS GL,color
- porting to OpenGL from IRIS GL,color
- OpenGL porting from IRIS GL,color
ms.topic: article
ms.date: 05/31/2018
---

# Porting Color Calls

The following table lists IRIS GL color functions and their equivalent OpenGL functions.



| IRIS GL function                  | OpenGL function                                                                                                                               | Meaning                                              |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| **c**                             | [glColor](glcolor-functions.md)                                                                                                              | Sets RGB color.                                      |
| **color**                         | [glIndex](glindex-functions.md)                                                                                                              | Sets the color index.                                |
| **getcolor**                      | [**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) ( GL\_CURRENT\_INDEX )                                               | Returns the current color index.                     |
| **getmcolor**                     |                                                                                                                                               | Gets a copy of the RGB values for a color map entry. |
| **gRGBcolor**                     | **glGet**( GL\_CURRENT\_COLOR )                                                                                                               | Gets the current RGB color values.                   |
| **mapcolor**                      |                                                                                                                                               |                                                      |
| **RGBcolor**                      | **glColor**                                                                                                                                   | Sets RGB color.                                      |
| **writemask**                     | [**glIndexMask**](glindexmask.md)                                                                                                            | Sets the color-index mode color mask.                |
| **wmpackRGBwritemask**<br/> | [**glColorMask**](glcolormask.md)                                                                                                            | Sets the RGB color mode mask.                        |
| **getwritemask**                  | [**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) ( GL\_COLOR\_WRITEMASK )**glGet**( GL\_INDEX\_WRITEMASK )<br/> | Gets the color mask.                                 |
| **gRGBmask**                      | **glGet**( GL\_COLOR\_WRITEMASK )                                                                                                             | Gets the color mask.                                 |
| **zwritemask**                    | [**glDepthMask**](gldepthmask.md)                                                                                                            |                                                      |



 

> [!Note]
>
> Be careful when replacing **zwritemask** with [**glDepthMask**](gldepthmask.md); **glDepthMask** takes a Boolean argument, whereas **zwritemask** takes a bit field.

 

If you want to use multiple color maps, you need to use the appropriate Windows color map functions. Therefore, **multimap**, **onemap**, **getcmmode**, **setmap**, and **getmap** have no OpenGL equivalents.

 

 





