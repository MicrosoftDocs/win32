---
Description: Windows GDI+ exposes a flat API that consists of about 600 functions, which are implemented in Gdiplus.dll and declared in Gdiplusflat.h.
ms.assetid: 809d8b1e-ccdd-4156-b650-1bb7443a59fa
title: AdjustableArrowCap Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AdjustableArrowCap Functions

Windows GDI+ exposes a flat API that consists of about 600 functions, which are implemented in Gdiplus.dll and declared in Gdiplusflat.h. The functions in the GDI+ flat API are wrapped by a collection of about 40 C++ classes. It is recommended that you do not directly call the functions in the flat API. Whenever you make calls to GDI+, you should do so by calling the methods and functions provided by the C++ wrappers. Microsoft Product Support Services will not provide support for code that calls the flat API directly. For more information on using these wrapper methods, see [GDI+ Flat API](-gdiplus-flatapi-flat.md).

The following flat API functions are wrapped by the [**AdjustableArrowCap**](/windows/win32/gdipluslinecaps/nl-gdipluslinecaps-adjustablearrowcap?branch=master) C++ class.

## AdjustableArrowCap Functions and Corresponding Wrapper Methods



| Flat function                                                                                                          | Wrapper method                                                                                                                | Description                                                                                                                                                                                                                              |
|------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GpStatus WINGDIPAPI GdipCreateAdjustableArrowCap(REAL height, REAL width, BOOL isFilled, GpAdjustableArrowCap \*\*cap) | [**AdjustableArrowCap::AdjustableArrowCap**](/windows/win32/Gdipluslinecaps/nf-gdipluslinecaps-adjustablearrowcap-adjustablearrowcap(const adjustablearrowcap &)?branch=master) | Creates an adjustable arrow line cap with the specified height and width. The arrow line cap can be filled or nonfilled. The middle inset defaults to zero.                                                                              |
| GpStatus WINGDIPAPI GdipSetAdjustableArrowCapHeight(GpAdjustableArrowCap\* cap, REAL height)                           | [**AdjustableArrowCap::SetHeight**](/windows/win32/Gdipluslinecaps/nf-gdipluslinecaps-adjustablearrowcap-setheight?branch=master)                                  | The [**AdjustableArrowCap::SetHeight**](/windows/win32/Gdipluslinecaps/nf-gdipluslinecaps-adjustablearrowcap-setheight?branch=master) method sets the height of the arrow cap. This is the distance from the base of the arrow to its vertex.                                 |
| GpStatus WINGDIPAPI GdipGetAdjustableArrowCapHeight(GpAdjustableArrowCap\* cap, REAL\* height)                         | [**AdjustableArrowCap::GetHeight**](/windows/win32/Gdipluslinecaps/nf-gdipluslinecaps-adjustablearrowcap-getheight?branch=master)                                         | The [**AdjustableArrowCap::GetHeight**](/windows/win32/Gdipluslinecaps/nf-gdipluslinecaps-adjustablearrowcap-getheight?branch=master) method gets the height of the arrow cap. The height is the distance from the base of the arrow to its vertex.                                  |
| GpStatus WINGDIPAPI GdipSetAdjustableArrowCapWidth(GpAdjustableArrowCap\* cap, REAL width)                             | [**AdjustableArrowCap::SetWidth**](/windows/win32/Gdipluslinecaps/nf-gdipluslinecaps-adjustablearrowcap-setwidth?branch=master)                                     | The [**AdjustableArrowCap::SetWidth**](/windows/win32/Gdipluslinecaps/nf-gdipluslinecaps-adjustablearrowcap-setwidth?branch=master) method sets the width of the arrow cap. The width is the distance between the endpoints of the base of the arrow.                          |
| GpStatus WINGDIPAPI GdipGetAdjustableArrowCapWidth(GpAdjustableArrowCap\* cap, REAL\* width)                           | [**AdjustableArrowCap::GetWidth**](/windows/win32/Gdipluslinecaps/nf-gdipluslinecaps-adjustablearrowcap-getwidth?branch=master)                                           | The [**AdjustableArrowCap::GetWidth**](/windows/win32/Gdipluslinecaps/nf-gdipluslinecaps-adjustablearrowcap-getwidth?branch=master) method gets the width of the arrow cap. The width is the distance between the endpoints of the base of the arrow.                                |
| GpStatus WINGDIPAPI GdipSetAdjustableArrowCapMiddleInset(GpAdjustableArrowCap\* cap, REAL middleInset)                 | [**AdjustableArrowCap::SetMiddleInset**](/windows/win32/Gdipluslinecaps/nf-gdipluslinecaps-adjustablearrowcap-setmiddleinset?branch=master)                   | The [**AdjustableArrowCap::SetMiddleInset**](/windows/win32/Gdipluslinecaps/nf-gdipluslinecaps-adjustablearrowcap-setmiddleinset?branch=master) method sets the number of units that the midpoint of the base shifts towards the vertex.                                 |
| GpStatus WINGDIPAPI GdipGetAdjustableArrowCapMiddleInset(GpAdjustableArrowCap\* cap, REAL\* middleInset)<br/>    | [**AdjustableArrowCap::GetMiddleInset**](/windows/win32/Gdipluslinecaps/nf-gdipluslinecaps-adjustablearrowcap-getmiddleinset?branch=master)                               | The [**AdjustableArrowCap::GetMiddleInset**](/windows/win32/Gdipluslinecaps/nf-gdipluslinecaps-adjustablearrowcap-getmiddleinset?branch=master) method gets the value of the inset. The middle inset is the number of units that the midpoint of the base shifts towards the vertex. |
| GpStatus WINGDIPAPI GdipSetAdjustableArrowCapFillState(GpAdjustableArrowCap\* cap, BOOL fillState)<br/>          | [**AdjustableArrowCap::SetFillState**](/windows/win32/Gdipluslinecaps/nf-gdipluslinecaps-adjustablearrowcap-setfillstate?branch=master)                          | The [**AdjustableArrowCap::SetFillState**](/windows/win32/Gdipluslinecaps/nf-gdipluslinecaps-adjustablearrowcap-setfillstate?branch=master) method sets the fill state of the arrow cap. If the arrow cap is not filled, only the outline is drawn.                         |
| GpStatus WINGDIPAPI GdipGetAdjustableArrowCapFillState(GpAdjustableArrowCap\* cap, BOOL\* fillState)<br/>        | [**AdjustableArrowCap::IsFilled**](/windows/win32/Gdipluslinecaps/nf-gdipluslinecaps-adjustablearrowcap-isfilled?branch=master)                                           | The [**AdjustableArrowCap::IsFilled**](/windows/win32/Gdipluslinecaps/nf-gdipluslinecaps-adjustablearrowcap-isfilled?branch=master) method determines whether the arrow cap is filled.                                                                                               |



 

 

 




