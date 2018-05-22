---
Description: 'A device context (DC) is a data structure defining the graphics objects, their associated attributes, and the graphics modes affecting output on a device. To create a DC, call the CreateDC function; to retrieve a DC, call the GetDC function.'
ms.assetid: '4feafb23-bf5a-493a-9d1d-96170711b907'
title: 'Bitmaps, Device Contexts, and Drawing Surfaces'
---

# Bitmaps, Device Contexts, and Drawing Surfaces

A *device context* (DC) is a data structure defining the graphics objects, their associated attributes, and the graphics modes affecting output on a device. To create a DC, call the [**CreateDC**](createdc.md) function; to retrieve a DC, call the [**GetDC**](getdc.md) function.

Before returning a handle that identifies that DC, the system selects a drawing surface into the DC. If the application called the [**CreateDC**](createdc.md) function to create a device context for a VGA display, the dimensions of this drawing surface are 640-by-480 pixels. If the application called the [**GetDC**](getdc.md) function, the dimensions reflect the size of the client area.

Before an application can begin drawing, it must select a bitmap with the appropriate width and height into the DC by calling the [**SelectObject**](selectobject.md) function. When an application passes the handle to the DC to one of the graphics device interface (GDI) drawing functions, the requested output appears on the drawing surface selected into the DC.

For more information, see [Memory Device Contexts](memory-device-contexts.md).

 

 



