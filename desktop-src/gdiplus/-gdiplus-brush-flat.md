---
description: Windows GDI+ exposes a flat API that consists of about 600 functions, which are implemented in Gdiplus.dll and declared in Gdiplusflat.h.
ms.assetid: def64d31-9a4b-4365-a618-b87735ce38f1
title: Brush Functions (GDI+)
ms.topic: article
ms.date: 05/31/2018
---

# Brush Functions (GDI+)

Windows GDI+ exposes a flat API that consists of about 600 functions, which are implemented in Gdiplus.dll and declared in Gdiplusflat.h. The functions in the GDI+ flat API are wrapped by a collection of about 40 C++ classes. It is recommended that you do not directly call the functions in the flat API. Whenever you make calls to GDI+, you should do so by calling the methods and functions provided by the C++ wrappers. Microsoft Product Support Services will not provide support for code that calls the flat API directly. For more information on using these wrapper methods, see [GDI+ Flat API](-gdiplus-flatapi-flat.md).

The following flat API functions are wrapped by the [**Brush**](/windows/desktop/api/gdiplusbrush/nl-gdiplusbrush-brush) C++ class.

## Brush Functions and Corresponding Wrapper Methods



| Flat function                                                                        | Wrapper method                                          | Description                                                                                                                                          |
|--------------------------------------------------------------------------------------|---------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| GpStatus WINGDIPAPI GdipCloneBrush(GpBrush \*brush, GpBrush \*\*cloneBrush)          | [**Brush::Clone**](/windows/desktop/api/Gdiplusbrush/nf-gdiplusbrush-brush-clone)     | The [**Brush::Clone**](/windows/desktop/api/Gdiplusbrush/nf-gdiplusbrush-brush-clone) method creates a new [**Brush**](/windows/desktop/api/gdiplusbrush/nl-gdiplusbrush-brush) object based on this brush. |
| GpStatus WINGDIPAPI GdipDeleteBrush(GpBrush \*brush)                                 | virtual ~Brush()                                        | Cleans up resources used by a [**Brush**](/windows/desktop/api/gdiplusbrush/nl-gdiplusbrush-brush) object.                                                                    |
| GpStatus WINGDIPAPI GdipGetBrushType(GpBrush \*brush, GpBrushType \*type)<br/> | [**Brush::GetType**](/windows/desktop/api/Gdiplusbrush/nf-gdiplusbrush-brush-gettype) | The [**Brush::GetType**](/windows/desktop/api/Gdiplusbrush/nf-gdiplusbrush-brush-gettype) method gets the type of this brush.                                                      |



 

 

 




