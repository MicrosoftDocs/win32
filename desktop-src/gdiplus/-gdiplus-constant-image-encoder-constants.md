---
Description: The ImageSave Methods and ImageSaveAdd Methods methods of the Image class receive an EncoderParameters object that contains an array of EncoderParameter objects.
ms.assetid: babc89f0-aea5-4341-8cf9-40d11e73fb10
title: Image Encoder Constants
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Image Encoder Constants

The [Image::Save Methods](/windows/win32/gdiplusheaders/nf-gdiplusheaders-image-save(in istream,in const clsid,in const encoderparameters)?branch=master) and [Image::SaveAdd Methods](/windows/win32/Gdiplusheaders/nf-gdiplusheaders-image-saveadd(in image,in const encoderparameters)?branch=master) methods of the [**Image**](/windows/win32/gdiplusheaders/nl-gdiplusheaders-image?branch=master) class receive an [**EncoderParameters**](/windows/win32/Gdiplusimaging/?branch=master) object that contains an array of [**EncoderParameter**](/windows/win32/Gdiplusimaging/?branch=master) objects. Each **EncoderParameter** object has a GUID data member that specifies the parameter category. The following constants, defined in Gdiplusimaging.h, represent GUIDs that specify the various parameter categories.

-   EncoderChrominanceTable
-   EncoderColorDepth
-   EncoderColorSpace
-   EncoderCompression
-   EncoderLuminanceTable
-   EncoderQuality
-   EncoderRenderMethod
-   EncoderSaveFlag
-   EncoderScanMethod
-   EncoderTransformation
-   EncoderVersion
-   EncoderImageItems
-   EncoderSaveAsCMYK

 

 



