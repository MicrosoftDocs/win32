---
description: Windows GDI+ provides the Image class and the Bitmap class for storing images in memory and manipulating images in memory.
ms.assetid: f9a5b4b1-4e25-42c8-a96b-a3104841e5f3
title: Using Image Encoders and Decoders
ms.topic: article
ms.date: 05/31/2018
---

# Using Image Encoders and Decoders

Windows GDI+ provides the [**Image**](/windows/desktop/api/gdiplusheaders/nl-gdiplusheaders-image) class and the [**Bitmap**](/windows/desktop/api/gdiplusheaders/nl-gdiplusheaders-bitmap) class for storing images in memory and manipulating images in memory. GDI+ writes images to disk files with the help of image encoders and loads images from disk files with the help of image decoders. An encoder translates the data in an **Image** or **Bitmap** object into a designated disk file format. A decoder translates the data in a disk file to the format required by the **Image** and **Bitmap** objects. GDI+ has built-in encoders and decoders that support the following file types:

-   BMP
-   GIF
-   JPEG
-   PNG
-   TIFF

GDI+ also has built-in decoders that support the following file types:

-   WMF
-   EMF
-   ICON

The following topics discuss encoders and decoders in more detail:

-   [Listing Installed Encoders](-gdiplus-listing-installed-encoders-use.md)
-   [Listing Installed Decoders](-gdiplus-listing-installed-decoders-use.md)
-   [Retrieving the Class Identifier for an Encoder](-gdiplus-retrieving-the-class-identifier-for-an-encoder-use.md)
-   [Determining the Parameters Supported by an Encoder](-gdiplus-determining-the-parameters-supported-by-an-encoder-use.md)
-   [Converting a BMP Image to a PNG Image](-gdiplus-converting-a-bmp-image-to-a-png-image-use.md)
-   [Setting JPEG Compression Level](-gdiplus-setting-jpeg-compression-level-use.md)
-   [Transforming a JPEG Image Without Loss of Information](-gdiplus-transforming-a-jpeg-image-without-loss-of-information-use.md)
-   [Creating and Saving a Multiple-Frame Image](-gdiplus-creating-and-saving-a-multiple-frame-image-use.md)
-   [Copying Individual Frames from a Multiple-Frame Image](-gdiplus-copying-individual-frames-from-a-multiple-frame-image-use.md)

 

 



