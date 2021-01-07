---
description: The Image::Save Methods and Image::SaveAdd Methods methods of the Image class receive an EncoderParameters object that contains an array of EncoderParameter objects.
ms.assetid: babc89f0-aea5-4341-8cf9-40d11e73fb10
title: Image Encoder Constants
ms.topic: article
ms.date: 05/31/2018
---

# Image Encoder Constants

The [Image::Save Methods](/windows/win32/api/gdiplusheaders/nf-gdiplusheaders-image-save(inistream_inconstclsid_inconstencoderparameters)) and [Image::SaveAdd Methods](/windows/win32/api/gdiplusheaders/nf-gdiplusheaders-image-saveadd(inimage_inconstencoderparameters)) methods of the [**Image**](/windows/win32/api/gdiplusheaders/nl-gdiplusheaders-image) class receive an [**EncoderParameters**](/windows/win32/api/gdiplusimaging/nl-gdiplusimaging-encoderparameters) object that contains an array of [**EncoderParameter**](/windows/win32/api/gdiplusimaging/nl-gdiplusimaging-encoderparameter) objects. Each **EncoderParameter** object has a GUID data member that specifies the parameter category. The following constants, defined in Gdiplusimaging.h, represent GUIDs that specify the various parameter categories.

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

 

 
