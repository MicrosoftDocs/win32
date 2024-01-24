---
description: Windows supports five graphic modes that allow an application to specify how colors are mixed, where output appears, how the output is scaled, and so on. These modes, which are stored in a DC, are described in the following table.
ms.assetid: 061af47e-fd49-4eb4-9b1b-03eb9c841622
title: Graphic Modes
ms.topic: article
ms.date: 05/31/2018
---

# Graphic Modes

Windows supports five graphic modes that allow an application to specify how colors are mixed, where output appears, how the output is scaled, and so on. These modes, which are stored in a DC, are described in the following table.



| Graphics mode | Description                                                                                                                |
|---------------|----------------------------------------------------------------------------------------------------------------------------|
| Background    | Defines how background colors are mixed with existing window or screen colors for bitmap and text operations.              |
| Drawing       | Defines how foreground colors are mixed with existing window or screen colors for pen, brush, bitmap, and text operations. |
| Mapping       | Defines how graphics output is mapped from logical (or world) space onto the window, screen, or printer paper.             |
| Polygon-fill  | Defines how the brush pattern is used to fill the interior of complex regions.                                             |
| Stretching    | Defines how bitmap colors are mixed with existing window or screen colors when the bitmap is compressed (or scaled down).  |



 

As it does with graphic objects, the system initializes a DC with default graphic modes. An application can retrieve and examine these default modes by calling the following functions.



| Graphics mode | Function                                       |
|---------------|------------------------------------------------|
| Background    | [**GetBkMode**](/windows/desktop/api/Wingdi/nf-wingdi-getbkmode)                 |
| Drawing       | [**GetROP2**](/windows/desktop/api/Wingdi/nf-wingdi-getrop2)                     |
| Mapping       | [**GetMapMode**](/windows/desktop/api/Wingdi/nf-wingdi-getmapmode)               |
| Polygon-fill  | [**GetPolyFillMode**](/windows/desktop/api/Wingdi/nf-wingdi-getpolyfillmode)     |
| Stretching    | [**GetStretchBltMode**](/windows/desktop/api/Wingdi/nf-wingdi-getstretchbltmode) |



 

An application can change the default modes by calling one of the following functions.



| Graphics mode | Function                                       |
|---------------|------------------------------------------------|
| Background    | [**SetBkMode**](/windows/desktop/api/Wingdi/nf-wingdi-setbkmode)                 |
| Drawing       | [**SetROP2**](/windows/desktop/api/Wingdi/nf-wingdi-setrop2)                     |
| Mapping       | [**SetMapMode**](/windows/desktop/api/Wingdi/nf-wingdi-setmapmode)               |
| Polygon-fill  | [**SetPolyFillMode**](/windows/desktop/api/Wingdi/nf-wingdi-setpolyfillmode)     |
| Stretching    | [**SetStretchBltMode**](/windows/desktop/api/Wingdi/nf-wingdi-setstretchbltmode) |



 

 

 



