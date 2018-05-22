---
Description: 'On certain versions of Microsoft Windows, the StretchDIBits and SetDIBitsToDevice functions allow JPEG and PNG images to be passed as the source image to printer devices.'
ms.assetid: 'a38a807d-44df-40a2-8af7-0ce5e532cba2'
title: JPEG and PNG Extensions for Specific Bitmap Functions and Structures
---

# JPEG and PNG Extensions for Specific Bitmap Functions and Structures

On certain versions of Microsoft Windows, the [**StretchDIBits**](stretchdibits.md) and [**SetDIBitsToDevice**](setdibitstodevice.md) functions allow JPEG and PNG images to be passed as the source image to printer devices. This extension is not intended as a means to supply general JPEG and PNG decompression to applications, but rather to allow applications to send JPEG- and PNG-compressed images directly to printers having hardware support for JPEG and PNG images.

The [**BITMAPINFOHEADER**](bitmapinfoheader.md), [**BITMAPV4HEADER**](bitmapv4header.md) and [**BITMAPV5HEADER**](bitmapv5header.md) structures are extended to allow specification of **biCompression** values indicating that the bitmap data is a JPEG or PNG image. These compression values are only valid for [**SetDIBitsToDevice**](setdibitstodevice.md) and [**StretchDIBits**](stretchdibits.md) when the *hdc* parameter specifies a printer device. To support metafile spooling of the printer, the application should not rely on the return value to determine whether the device supports the JPEG or PNG file. The application must issue QUERYESCSUPPORT with the corresponding escape before calling **SetDIBitsToDevice** and **StretchDIBits**. If the validation escape fails, the application must then fall back on its own JPEG or PNG support to decompress the image into a bitmap.

 

 



