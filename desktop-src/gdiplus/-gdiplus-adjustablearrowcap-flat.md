---
Description: 'Windows GDI+ exposes a flat API that consists of about 600 functions, which are implemented in Gdiplus.dll and declared in Gdiplusflat.h.'
ms.assetid: '809d8b1e-ccdd-4156-b650-1bb7443a59fa'
title: AdjustableArrowCap Functions
---

# AdjustableArrowCap Functions

Windows GDI+ exposes a flat API that consists of about 600 functions, which are implemented in Gdiplus.dll and declared in Gdiplusflat.h. The functions in the GDI+ flat API are wrapped by a collection of about 40 C++ classes. It is recommended that you do not directly call the functions in the flat API. Whenever you make calls to GDI+, you should do so by calling the methods and functions provided by the C++ wrappers. Microsoft Product Support Services will not provide support for code that calls the flat API directly. For more information on using these wrapper methods, see [GDI+ Flat API](-gdiplus-flatapi-flat.md).

The following flat API functions are wrapped by the [**AdjustableArrowCap**](-gdiplus-class-adjustablearrowcap-class.md) C++ class.

## AdjustableArrowCap Functions and Corresponding Wrapper Methods



| Flat function                                                                                                          | Wrapper method                                                                                                                | Description                                                                                                                                                                                                                              |
|------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GpStatus WINGDIPAPI GdipCreateAdjustableArrowCap(REAL height, REAL width, BOOL isFilled, GpAdjustableArrowCap \*\*cap) | [**AdjustableArrowCap::AdjustableArrowCap**](-gdiplus-class-adjustablearrowcap-adjustablearrowcap-height-width-isfilled-.md) | Creates an adjustable arrow line cap with the specified height and width. The arrow line cap can be filled or nonfilled. The middle inset defaults to zero.                                                                              |
| GpStatus WINGDIPAPI GdipSetAdjustableArrowCapHeight(GpAdjustableArrowCap\* cap, REAL height)                           | [**AdjustableArrowCap::SetHeight**](-gdiplus-class-adjustablearrowcap-setheight-height-.md)                                  | The [**AdjustableArrowCap::SetHeight**](-gdiplus-class-adjustablearrowcap-setheight-height-.md) method sets the height of the arrow cap. This is the distance from the base of the arrow to its vertex.                                 |
| GpStatus WINGDIPAPI GdipGetAdjustableArrowCapHeight(GpAdjustableArrowCap\* cap, REAL\* height)                         | [**AdjustableArrowCap::GetHeight**](-gdiplus-class-adjustablearrowcap-getheight-.md)                                         | The [**AdjustableArrowCap::GetHeight**](-gdiplus-class-adjustablearrowcap-getheight-.md) method gets the height of the arrow cap. The height is the distance from the base of the arrow to its vertex.                                  |
| GpStatus WINGDIPAPI GdipSetAdjustableArrowCapWidth(GpAdjustableArrowCap\* cap, REAL width)                             | [**AdjustableArrowCap::SetWidth**](-gdiplus-class-adjustablearrowcap-setwidth-width-.md)                                     | The [**AdjustableArrowCap::SetWidth**](-gdiplus-class-adjustablearrowcap-setwidth-width-.md) method sets the width of the arrow cap. The width is the distance between the endpoints of the base of the arrow.                          |
| GpStatus WINGDIPAPI GdipGetAdjustableArrowCapWidth(GpAdjustableArrowCap\* cap, REAL\* width)                           | [**AdjustableArrowCap::GetWidth**](-gdiplus-class-adjustablearrowcap-getwidth-.md)                                           | The [**AdjustableArrowCap::GetWidth**](-gdiplus-class-adjustablearrowcap-getwidth-.md) method gets the width of the arrow cap. The width is the distance between the endpoints of the base of the arrow.                                |
| GpStatus WINGDIPAPI GdipSetAdjustableArrowCapMiddleInset(GpAdjustableArrowCap\* cap, REAL middleInset)                 | [**AdjustableArrowCap::SetMiddleInset**](-gdiplus-class-adjustablearrowcap-setmiddleinset-middleinset-.md)                   | The [**AdjustableArrowCap::SetMiddleInset**](-gdiplus-class-adjustablearrowcap-setmiddleinset-middleinset-.md) method sets the number of units that the midpoint of the base shifts towards the vertex.                                 |
| GpStatus WINGDIPAPI GdipGetAdjustableArrowCapMiddleInset(GpAdjustableArrowCap\* cap, REAL\* middleInset)<br/>    | [**AdjustableArrowCap::GetMiddleInset**](-gdiplus-class-adjustablearrowcap-getmiddleinset-.md)                               | The [**AdjustableArrowCap::GetMiddleInset**](-gdiplus-class-adjustablearrowcap-getmiddleinset-.md) method gets the value of the inset. The middle inset is the number of units that the midpoint of the base shifts towards the vertex. |
| GpStatus WINGDIPAPI GdipSetAdjustableArrowCapFillState(GpAdjustableArrowCap\* cap, BOOL fillState)<br/>          | [**AdjustableArrowCap::SetFillState**](-gdiplus-class-adjustablearrowcap-setfillstate-isfilled-.md)                          | The [**AdjustableArrowCap::SetFillState**](-gdiplus-class-adjustablearrowcap-setfillstate-isfilled-.md) method sets the fill state of the arrow cap. If the arrow cap is not filled, only the outline is drawn.                         |
| GpStatus WINGDIPAPI GdipGetAdjustableArrowCapFillState(GpAdjustableArrowCap\* cap, BOOL\* fillState)<br/>        | [**AdjustableArrowCap::IsFilled**](-gdiplus-class-adjustablearrowcap-isfilled-.md)                                           | The [**AdjustableArrowCap::IsFilled**](-gdiplus-class-adjustablearrowcap-isfilled-.md) method determines whether the arrow cap is filled.                                                                                               |



 

 

 




