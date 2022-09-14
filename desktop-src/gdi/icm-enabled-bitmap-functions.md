---
description: Microsoft Image Color Management (ICM) ensures that a color image, graphic object, or text object is rendered as closely as possible to its original intent on any device, despite differences in imaging technologies and color capabilities between devices.
ms.assetid: 7b3cb9a4-ffd2-4867-85bd-0e663fdde6e3
title: ICM-Enabled Bitmap Functions
ms.topic: article
ms.date: 05/31/2018
---

# ICM-Enabled Bitmap Functions

Microsoft Image Color Management (ICM) ensures that a color image, graphic object, or text object is rendered as closely as possible to its original intent on any device, despite differences in imaging technologies and color capabilities between devices. Whether you are scanning an image or other graphic on a color scanner, downloading it over the Internet, viewing or editing it onscreen, or printing it on paper, film, or other media, ICM 2.0 helps you keep colors consistent and accurate. For more information about ICM, see [Windows Color System](/previous-versions//dd372446(v=vs.85)).

There are various functions in the graphics device interface (GDI) that use or operate on color data. The following bitmap functions are enabled for use with ICM:

-   [**BitBlt**](/windows/desktop/api/Wingdi/nf-wingdi-bitblt)
-   [**CreateDIBitmap**](/windows/desktop/api/Wingdi/nf-wingdi-createdibitmap)
-   [**CreateDIBSection**](/windows/desktop/api/Wingdi/nf-wingdi-createdibsection)
-   [**MaskBlt**](/windows/desktop/api/Wingdi/nf-wingdi-maskblt)
-   [**SetDIBColorTable**](/windows/desktop/api/Wingdi/nf-wingdi-setdibcolortable)
-   [**StretchBlt**](/windows/desktop/api/Wingdi/nf-wingdi-stretchblt)
-   [**SetDIBits**](/windows/desktop/api/Wingdi/nf-wingdi-setdibits)
-   [**SetDIBitsToDevice**](/windows/desktop/api/Wingdi/nf-wingdi-setdibitstodevice)
-   [**StretchDIBits**](/windows/desktop/api/Wingdi/nf-wingdi-stretchdibits)

 

 
