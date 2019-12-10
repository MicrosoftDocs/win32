---
Description: The Image::Save Methods and Image::SaveAdd Methods methods of the Image class receive an EncoderParameters object that contains an array of EncoderParameter objects.
ms.assetid: babc89f0-aea5-4341-8cf9-40d11e73fb10
title: Image Encoder Constants
ms.topic: article
ms.date: 05/31/2018
---

# Image Encoder Constants

The [Image::Save Methods](https://msdn.microsoft.com/library/ms535399(v=VS.85).aspx) and [Image::SaveAdd Methods](https://msdn.microsoft.com/library/ms535398(v=VS.85).aspx) methods of the [**Image**](/windows/desktop/api/gdiplusheaders/nl-gdiplusheaders-image) class receive an [**EncoderParameters**](https://msdn.microsoft.com/library/ms534435(v=VS.85).aspx) object that contains an array of [**EncoderParameter**](https://msdn.microsoft.com/library/ms534434(v=VS.85).aspx) objects. Each **EncoderParameter** object has a GUID data member that specifies the parameter category. The following constants, defined in Gdiplusimaging.h, represent GUIDs that specify the various parameter categories.

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

 

 



