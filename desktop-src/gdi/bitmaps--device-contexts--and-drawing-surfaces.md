---
description: A device context (DC) is a data structure defining the graphics objects, their associated attributes, and the graphics modes affecting output on a device. To create a DC, call the CreateDC function; to retrieve a DC, call the GetDC function.
ms.assetid: 4feafb23-bf5a-493a-9d1d-96170711b907
title: Bitmaps, Device Contexts, and Drawing Surfaces
ms.topic: article
ms.date: 05/31/2018
---

# Bitmaps, Device Contexts, and Drawing Surfaces

A *device context* (DC) is a data structure defining the graphics objects, their associated attributes, and the graphics modes affecting output on a device. To create a DC, call the [**CreateDC**](/windows/desktop/api/Wingdi/nf-wingdi-createdca) function; to retrieve a DC, call the [**GetDC**](/windows/desktop/api/Winuser/nf-winuser-getdc) function.

Before returning a handle that identifies that DC, the system selects a drawing surface into the DC. If the application called the [**CreateDC**](/windows/desktop/api/Wingdi/nf-wingdi-createdca) function to create a device context for a VGA display, the dimensions of this drawing surface are 640-by-480 pixels. If the application called the [**GetDC**](/windows/desktop/api/Winuser/nf-winuser-getdc) function, the dimensions reflect the size of the client area.

Before an application can begin drawing, it must select a bitmap with the appropriate width and height into the DC by calling the [**SelectObject**](/windows/desktop/api/Wingdi/nf-wingdi-selectobject) function. When an application passes the handle to the DC to one of the graphics device interface (GDI) drawing functions, the requested output appears on the drawing surface selected into the DC.

For more information, see [Memory Device Contexts](memory-device-contexts.md).

 

 



