---
Description: On certain versions of Microsoft Windows, the StretchDIBits and SetDIBitsToDevice functions allow JPEG and PNG images to be passed as the source image to printer devices.
ms.assetid: a38a807d-44df-40a2-8af7-0ce5e532cba2
title: JPEG and PNG Extensions for Specific Bitmap Functions and Structures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# JPEG and PNG Extensions for Specific Bitmap Functions and Structures

On certain versions of Microsoft Windows, the [**StretchDIBits**](/windows/win32/Wingdi/nf-wingdi-stretchdibits?branch=master) and [**SetDIBitsToDevice**](/windows/win32/Wingdi/nf-wingdi-setdibitstodevice?branch=master) functions allow JPEG and PNG images to be passed as the source image to printer devices. This extension is not intended as a means to supply general JPEG and PNG decompression to applications, but rather to allow applications to send JPEG- and PNG-compressed images directly to printers having hardware support for JPEG and PNG images.

The [**BITMAPINFOHEADER**](/windows/win32/Wingdi/?branch=master), [**BITMAPV4HEADER**](/windows/win32/Wingdi/ns-wingdi-bitmapv4header?branch=master) and [**BITMAPV5HEADER**](/windows/win32/Wingdi/ns-wingdi-bitmapv5header?branch=master) structures are extended to allow specification of **biCompression** values indicating that the bitmap data is a JPEG or PNG image. These compression values are only valid for [**SetDIBitsToDevice**](/windows/win32/Wingdi/nf-wingdi-setdibitstodevice?branch=master) and [**StretchDIBits**](/windows/win32/Wingdi/nf-wingdi-stretchdibits?branch=master) when the *hdc* parameter specifies a printer device. To support metafile spooling of the printer, the application should not rely on the return value to determine whether the device supports the JPEG or PNG file. The application must issue QUERYESCSUPPORT with the corresponding escape before calling **SetDIBitsToDevice** and **StretchDIBits**. If the validation escape fails, the application must then fall back on its own JPEG or PNG support to decompress the image into a bitmap.

 

 



