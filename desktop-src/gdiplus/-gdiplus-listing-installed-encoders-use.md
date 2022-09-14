---
description: GDI+ provides the GetImageEncoders function so that you can determine which image encoders are available on your computer.
ms.assetid: a261cf61-b853-4208-984b-0d5040eb1667
title: Listing Installed Encoders
ms.topic: article
ms.date: 05/31/2018
---

# Listing Installed Encoders

GDI+ provides the [**GetImageEncoders**](/windows/desktop/api/Gdiplusimagecodec/nf-gdiplusimagecodec-getimageencoders) function so that you can determine which image encoders are available on your computer. **GetImageEncoders** returns an array of [**ImageCodecInfo**](/windows/win32/api/gdiplusimaging/nl-gdiplusimaging-imagecodecinfo) objects. Before you call **GetImageEncoders**, you must allocate a buffer large enough to receive that array. You can call [**GetImageEncodersSize**](/windows/desktop/api/Gdiplusimagecodec/nf-gdiplusimagecodec-getimageencoderssize) to determine the size of the required buffer.

The following console application lists the available image encoders:


```
#include <windows.h>
#include <gdiplus.h>
#include <stdio.h>
using namespace Gdiplus;

INT main()
{
   // Initialize GDI+.
   GdiplusStartupInput gdiplusStartupInput;
   ULONG_PTR gdiplusToken;
   GdiplusStartup(&gdiplusToken, &gdiplusStartupInput, NULL);

   UINT  num;        // number of image encoders
   UINT  size;       // size, in bytes, of the image encoder array

   ImageCodecInfo* pImageCodecInfo;

   // How many encoders are there?
   // How big (in bytes) is the array of all ImageCodecInfo objects?
   GetImageEncodersSize(&num, &size);

   // Create a buffer large enough to hold the array of ImageCodecInfo
   // objects that will be returned by GetImageEncoders.
   pImageCodecInfo = (ImageCodecInfo*)(malloc(size));

   // GetImageEncoders creates an array of ImageCodecInfo objects
   // and copies that array into a previously allocated buffer. 
   // The third argument, imageCodecInfo, is a pointer to that buffer. 
   GetImageEncoders(num, size, pImageCodecInfo);

   // Display the graphics file format (MimeType)
   // for each ImageCodecInfo object.
   for(UINT j = 0; j < num; ++j)
   { 
      wprintf(L"%s\n", pImageCodecInfo[j].MimeType);   
   }

   free(pImageCodecInfo);
   GdiplusShutdown(gdiplusToken);
   return 0;
}
```



When you run the preceding console application, the output will be similar to the following:


```
image/bmp
image/jpeg
image/gif
image/tiff
image/png
```



 

 
