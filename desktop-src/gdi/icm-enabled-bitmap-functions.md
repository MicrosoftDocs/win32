---
Description: Microsoft Image Color Management (ICM) ensures that a color image, graphic object, or text object is rendered as closely as possible to its original intent on any device, despite differences in imaging technologies and color capabilities between devices.
ms.assetid: 7b3cb9a4-ffd2-4867-85bd-0e663fdde6e3
title: ICM-Enabled Bitmap Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ICM-Enabled Bitmap Functions

Microsoft Image Color Management (ICM) ensures that a color image, graphic object, or text object is rendered as closely as possible to its original intent on any device, despite differences in imaging technologies and color capabilities between devices. Whether you are scanning an image or other graphic on a color scanner, downloading it over the Internet, viewing or editing it onscreen, or printing it on paper, film, or other media, ICM 2.0 helps you keep colors consistent and accurate. For more information about ICM, see [Windows Color System](wcs.windows_color_system).

There are various functions in the graphics device interface (GDI) that use or operate on color data. The following bitmap functions are enabled for use with ICM:

-   [**BitBlt**](/windows/win32/Wingdi/nf-wingdi-bitblt?branch=master)
-   [**CreateDIBitmap**](/windows/win32/Wingdi/nf-wingdi-createdibitmap?branch=master)
-   [**CreateDIBSection**](/windows/win32/Wingdi/nf-wingdi-createdibsection?branch=master)
-   [**MaskBlt**](/windows/win32/Wingdi/nf-wingdi-maskblt?branch=master)
-   [**SetDIBColorTable**](/windows/win32/Wingdi/nf-wingdi-setdibcolortable?branch=master)
-   [**StretchBlt**](/windows/win32/Wingdi/nf-wingdi-stretchblt?branch=master)
-   [**SetDIBits**](/windows/win32/Wingdi/nf-wingdi-setdibits?branch=master)
-   [**SetDIBitsToDevice**](/windows/win32/Wingdi/nf-wingdi-setdibitstodevice?branch=master)
-   [**StretchDIBits**](/windows/win32/Wingdi/nf-wingdi-stretchdibits?branch=master)

 

 



