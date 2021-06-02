---
description: Windows GDI+ exposes a flat API that consists of about 600 functions, which are implemented in Gdiplus.dll and declared in Gdiplusflat.h.
ms.assetid: c7d9e633-8c3d-4e77-811d-306cd785a7ad
title: HatchBrush Functions
ms.topic: article
ms.date: 05/31/2018
---

# HatchBrush Functions

Windows GDI+ exposes a flat API that consists of about 600 functions, which are implemented in Gdiplus.dll and declared in Gdiplusflat.h. The functions in the GDI+ flat API are wrapped by a collection of about 40 C++ classes. It is recommended that you do not directly call the functions in the flat API. Whenever you make calls to GDI+, you should do so by calling the methods and functions provided by the C++ wrappers. Microsoft Product Support Services will not provide support for code that calls the flat API directly. For more information on using these wrapper methods, see [GDI+ Flat API](-gdiplus-flatapi-flat.md).

The following flat API functions are wrapped by the [**HatchBrush**](/windows/desktop/api/gdiplusbrush/nl-gdiplusbrush-hatchbrush) C++ class.

## HatchBrush Functions and Corresponding Wrapper Methods



| Flat function                                                                                                               | Wrapper method                                                                                                                                                                                   | Remarks                                                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| GpStatus WINGDIPAPI GdipCreateHatchBrush(GpHatchStyle hatchstyle, ARGB forecol, ARGB backcol, GpHatch \*\*brush)<br/> | [**HatchBrush::HatchBrush(IN HatchStyle hatchStyle, IN const Color& foreColor, IN const Color& backColor = Color())**](/windows/win32/api/gdiplusbrush/nf-gdiplusbrush-hatchbrush-hatchbrush(consthatchbrush_)) | Creates a [**HatchBrush**](/windows/desktop/api/gdiplusbrush/nl-gdiplusbrush-hatchbrush) object based on a hatch style, a foreground color, and a background color. |
| GpStatus WINGDIPAPI GdipGetHatchStyle(GpHatch \*brush, GpHatchStyle \*hatchstyle)<br/>                                | [**HatchStyle HatchBrush::GetHatchStyle() const**](/windows/desktop/api/Gdiplusbrush/nf-gdiplusbrush-hatchbrush-gethatchstyle)                                                                                                 | Gets the hatch style of this hatch brush.                                                                                                  |
| GpStatus WINGDIPAPI GdipGetHatchForegroundColor(GpHatch \*brush, ARGB\* forecol)<br/>                                 | [**Status HatchBrush::GetForegroundColor(OUT Color\* color) const**](/windows/desktop/api/Gdiplusbrush/nf-gdiplusbrush-hatchbrush-getforegroundcolor)                                                                    | Gets the foreground color of this hatch brush.                                                                                             |
| GpStatus WINGDIPAPI GdipGetHatchBackgroundColor(GpHatch \*brush, ARGB\* backcol)<br/>                                 | [**Status HatchBrush::GetBackgroundColor(OUT Color \*color) const**](/windows/desktop/api/Gdiplusbrush/nf-gdiplusbrush-hatchbrush-getbackgroundcolor)                                                                    | Gets the background color of this hatch brush.                                                                                             |



 

 

 
