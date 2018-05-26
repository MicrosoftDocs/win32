---
Description: Windows GDI+ exposes a flat API that consists of about 600 functions, which are implemented in Gdiplus.dll and declared in Gdiplusflat.h.
ms.assetid: b427b8ab-66fd-4f57-b08e-5f337a9ac9af
title: SolidBrush Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SolidBrush Functions

Windows GDI+ exposes a flat API that consists of about 600 functions, which are implemented in Gdiplus.dll and declared in Gdiplusflat.h. The functions in the GDI+ flat API are wrapped by a collection of about 40 C++ classes. We recommend not to call the functions in the flat API directly. Whenever you make calls to GDI+, we recommend that you do so by calling the methods and functions provided by the C++ wrappers. Microsoft Product Support Services will not provide support for code that calls the flat API directly. For more info on using these wrapper methods, see [GDI+ Flat API](-gdiplus-flatapi-flat.md).

The following flat API functions are wrapped by the [**SolidBrush**](/windows/win32/gdiplusbrush/nl-gdiplusbrush-solidbrush?branch=master) C++ class.

## Brush Functions and Corresponding Wrapper Methods



| Flat function                                                                               | Wrapper method                                                                                       | Remarks                                                                                 |
|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| **GpStatus WINGDIPAPI GdipCreateSolidFill(ARGB color, GpSolidFill \*\*brush)**<br/>   | [**SolidBrush::SolidBrush(IN const Color& color)**](/windows/win32/Gdiplusbrush/nf-gdiplusbrush-solidbrush-solidbrush(const solidbrush &)?branch=master) | Creates a [**SolidBrush**](/windows/win32/gdiplusbrush/nl-gdiplusbrush-solidbrush?branch=master) object based on a color |
| **GpStatus WINGDIPAPI GdipSetSolidFillColor(GpSolidFill \*brush, ARGB color)**<br/>   | [**SolidBrush::SetColor(IN const Color& color)**](/windows/win32/Gdiplusbrush/nf-gdiplusbrush-solidbrush-setcolor?branch=master)     | Sets the color of this solid brush                                                      |
| **GpStatus WINGDIPAPI GdipGetSolidFillColor(GpSolidFill \*brush, ARGB \*color)**<br/> | [**SolidBrush::GetColor(OUT Color\* color) const**](/windows/win32/Gdiplusbrush/nf-gdiplusbrush-solidbrush-getcolor?branch=master)   | Gets the color of this solid brush                                                      |



 

 

 




