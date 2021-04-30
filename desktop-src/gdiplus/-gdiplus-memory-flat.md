---
description: Windows GDI+ exposes a flat API that consists of about 600 functions, which are implemented in Gdiplus.dll and declared in Gdiplusflat.h.
ms.assetid: b4fcc02c-1b0f-4731-8312-29894b1f722f
title: Memory Functions
ms.topic: article
ms.date: 05/31/2018
---

# Memory Functions

Windows GDI+ exposes a flat API that consists of about 600 functions, which are implemented in Gdiplus.dll and declared in Gdiplusflat.h. The functions in the GDI+ flat API are wrapped by a collection of about 40 C++ classes. It is recommended that you do not directly call the functions in the flat API. Whenever you make calls to GDI+, you should do so by calling the methods and functions provided by the C++ wrappers. Microsoft Product Support Services will not provide support for code that calls the flat API directly. For more information on using these wrapper methods, see [GDI+ Flat API](-gdiplus-flatapi-flat.md).

The following flat API functions are wrapped by the [**GdiplusBase**](/windows/desktop/api/gdiplusbase/nl-gdiplusbase-gdiplusbase) C++ class.

## Memory Functions and Corresponding Wrapper Methods



| Flat function                                          | Wrapper method                                                                                                                                      | Remarks                                                                                                      |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| GpStatus WINGDIPAPI GdipAlloc(size\_t size)<br/> | [**GpStatus WINGDIPAPI GdiplusBase void\* (operator new)(size\_t in\_size)**](/windows/win32/api/gdiplusbase/nf-gdiplusbase-gdiplusbase-operatornew)<br/>      | Allocates memory for one Windows GDI+ object. <br/> GdipAlloc is declared in GdiplusMem.h.<br/>  |
| GpStatus WINGDIPAPI GdipFree(void\* ptr);<br/>   | [**GpStatus WINGDIPAPI GdiplusBase void (operator delete)(void\* in\_pVoid)**](/windows/win32/api/gdiplusbase/nf-gdiplusbase-gdiplusbase-operatordelete)<br/> | Deallocates memory for one Windows GDI+ object. <br/> GdipFree is declared in GdiplusMem.h.<br/> |



 

 

 
