---
Description: Microsoft Image Color Management (ICM) ensures that a color image, graphic, or text object is rendered as closely as possible to its original intent on any device, despite differences in imaging technologies and color capabilities between devices.
ms.assetid: eced18cf-be5a-4c61-b0e5-36d607daa6ff
title: ICM-Enabled Device Context Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ICM-Enabled Device Context Functions

Microsoft Image Color Management (ICM) ensures that a color image, graphic, or text object is rendered as closely as possible to its original intent on any device, despite differences in imaging technologies and color capabilities between devices. (For more information, see [Windows Color System](wcs.windows_color_system).)

There are various functions in the graphics device interface (GDI) that use or operate on color data. The following device context functions are enabled for use with ICM:

-   [**CreateCompatibleDC**](/windows/win32/Wingdi/nf-wingdi-createcompatibledc?branch=master)
-   [**CreateDC**](/windows/win32/Wingdi/nf-wingdi-createdca?branch=master)
-   [**GetDCBrushColor**](/windows/win32/WinGdi/nf-wingdi-getdcbrushcolor?branch=master)
-   [**GetDCPenColor**](/windows/win32/WinGdi/nf-wingdi-getdcpencolor?branch=master)
-   [**ResetDC**](/windows/win32/Wingdi/nf-wingdi-resetdca?branch=master)
-   [**SelectObject**](/windows/win32/Wingdi/nf-wingdi-selectobject?branch=master)
-   [**SetDCBrushColor**](/windows/win32/Wingdi/nf-wingdi-setdcbrushcolor?branch=master)
-   [**SetDCPenColor**](/windows/win32/Wingdi/nf-wingdi-setdcpencolor?branch=master)

 

 



