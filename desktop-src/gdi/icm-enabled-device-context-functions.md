---
Description: Microsoft Image Color Management (ICM) ensures that a color image, graphic, or text object is rendered as closely as possible to its original intent on any device, despite differences in imaging technologies and color capabilities between devices.
ms.assetid: eced18cf-be5a-4c61-b0e5-36d607daa6ff
title: ICM-Enabled Device Context Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ICM-Enabled Device Context Functions

Microsoft Image Color Management (ICM) ensures that a color image, graphic, or text object is rendered as closely as possible to its original intent on any device, despite differences in imaging technologies and color capabilities between devices. (For more information, see [Windows Color System](https://msdn.microsoft.com/b354b90f-575d-4392-9aa2-6fb1d2cb3c07).)

There are various functions in the graphics device interface (GDI) that use or operate on color data. The following device context functions are enabled for use with ICM:

-   [**CreateCompatibleDC**](/windows/desktop/api/Wingdi/nf-wingdi-createcompatibledc)
-   [**CreateDC**](/windows/desktop/api/Wingdi/nf-wingdi-createdca)
-   [**GetDCBrushColor**](/windows/desktop/api/WinGdi/nf-wingdi-getdcbrushcolor)
-   [**GetDCPenColor**](/windows/desktop/api/WinGdi/nf-wingdi-getdcpencolor)
-   [**ResetDC**](/windows/desktop/api/Wingdi/nf-wingdi-resetdca)
-   [**SelectObject**](/windows/desktop/api/Wingdi/nf-wingdi-selectobject)
-   [**SetDCBrushColor**](/windows/desktop/api/Wingdi/nf-wingdi-setdcbrushcolor)
-   [**SetDCPenColor**](/windows/desktop/api/Wingdi/nf-wingdi-setdcpencolor)

 

 



