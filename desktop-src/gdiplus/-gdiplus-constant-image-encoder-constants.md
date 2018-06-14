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

The [Image::Save Methods](/windows/desktop/api/gdiplusheaders/nf-gdiplusheaders-image-save(in istream,in const clsid,in const encoderparameters)) and [Image::SaveAdd Methods](/windows/desktop/api/Gdiplusheaders/nf-gdiplusheaders-image-saveadd(in image,in const encoderparameters)) methods of the [**Image**](/windows/desktop/api/gdiplusheaders/nl-gdiplusheaders-image) class receive an [**EncoderParameters**](https://msdn.microsoft.com/en-us/library/ms534435(v=VS.85).aspx) object that contains an array of [**EncoderParameter**](https://msdn.microsoft.com/en-us/library/ms534434(v=VS.85).aspx) objects. Each **EncoderParameter** object has a GUID data member that specifies the parameter category. The following constants, defined in Gdiplusimaging.h, represent GUIDs that specify the various parameter categories.

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

 

 



