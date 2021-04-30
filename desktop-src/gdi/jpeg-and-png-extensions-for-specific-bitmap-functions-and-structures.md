---
description: On certain versions of Microsoft Windows, the StretchDIBits and SetDIBitsToDevice functions allow JPEG and PNG images to be passed as the source image to printer devices.
ms.assetid: a38a807d-44df-40a2-8af7-0ce5e532cba2
title: JPEG and PNG Extensions for Specific Bitmap Functions and Structures
ms.topic: article
ms.date: 05/31/2018
---

# JPEG and PNG Extensions for Specific Bitmap Functions and Structures

On certain versions of Microsoft Windows, the [**StretchDIBits**](/windows/desktop/api/Wingdi/nf-wingdi-stretchdibits) and [**SetDIBitsToDevice**](/windows/desktop/api/Wingdi/nf-wingdi-setdibitstodevice) functions allow JPEG and PNG images to be passed as the source image to printer devices. This extension is not intended as a means to supply general JPEG and PNG decompression to applications, but rather to allow applications to send JPEG- and PNG-compressed images directly to printers having hardware support for JPEG and PNG images.

The [**BITMAPINFOHEADER**](/previous-versions//dd183376(v=vs.85)), [**BITMAPV4HEADER**](/windows/desktop/api/Wingdi/ns-wingdi-bitmapv4header) and [**BITMAPV5HEADER**](/windows/desktop/api/Wingdi/ns-wingdi-bitmapv5header) structures are extended to allow specification of **biCompression** values indicating that the bitmap data is a JPEG or PNG image. These compression values are only valid for [**SetDIBitsToDevice**](/windows/desktop/api/Wingdi/nf-wingdi-setdibitstodevice) and [**StretchDIBits**](/windows/desktop/api/Wingdi/nf-wingdi-stretchdibits) when the *hdc* parameter specifies a printer device. To support metafile spooling of the printer, the application should not rely on the return value to determine whether the device supports the JPEG or PNG file. The application must issue QUERYESCSUPPORT with the corresponding escape before calling **SetDIBitsToDevice** and **StretchDIBits**. If the validation escape fails, the application must then fall back on its own JPEG or PNG support to decompress the image into a bitmap.

 

 
