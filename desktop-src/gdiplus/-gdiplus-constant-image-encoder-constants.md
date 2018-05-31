---
Description: The Image::Save Methods and Image::SaveAdd Methods methods of the Image class receive an EncoderParameters object that contains an array of EncoderParameter objects.
ms.assetid: babc89f0-aea5-4341-8cf9-40d11e73fb10
title: Image Encoder Constants
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Image Encoder Constants

The [Image::Save Methods](/windows/desktop/api/gdiplusheaders/nf-gdiplusheaders-image-save(in istream,in const clsid,in const encoderparameters)) and [Image::SaveAdd Methods](/windows/desktop/api/Gdiplusheaders/nf-gdiplusheaders-image-saveadd(in image,in const encoderparameters)) methods of the [**Image**](/windows/desktop/api/gdiplusheaders/nl-gdiplusheaders-image) class receive an [**EncoderParameters**](/windows/desktop/api/Gdiplusimaging/) object that contains an array of [**EncoderParameter**](/windows/desktop/api/Gdiplusimaging/) objects. Each **EncoderParameter** object has a GUID data member that specifies the parameter category. The following constants, defined in Gdiplusimaging.h, represent GUIDs that specify the various parameter categories.

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

 

 



