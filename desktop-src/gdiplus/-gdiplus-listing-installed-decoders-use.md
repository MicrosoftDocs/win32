---
Description: 'Windows GDI+ provides the GetImageDecoders function so that you can determine which image decoders are available on your computer.'
ms.assetid: '793e23de-d959-4feb-8bf6-647a455c85ae'
title: Listing Installed Decoders
---

# Listing Installed Decoders

Windows GDI+ provides the [**GetImageDecoders**](-gdiplus-func-getimagedecoders-numdecoders-size-decoders-.md) function so that you can determine which image decoders are available on your computer. **GetImageDecoders** returns an array of [**ImageCodecInfo**](-gdiplus-class-imagecodecinfo-class.md) objects. Before you call **GetImageDecoders**, you must allocate a buffer large enough to receive that array. You can call [**GetImageDecodersSize**](-gdiplus-func-getimagedecoderssize-numdecoders-size-.md) to determine the size of the required buffer.

The following console application lists the available image decoders:


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
   GdiplusStartup(&amp;gdiplusToken, &amp;gdiplusStartupInput, NULL);

   UINT  num;        // number of image decoders
   UINT  size;       // size, in bytes, of the image decoder array

   ImageCodecInfo* pImageCodecInfo;

   // How many decoders are there?
   // How big (in bytes) is the array of all ImageCodecInfo objects?
   GetImageDecodersSize(&amp;num, &amp;size);

   // Create a buffer large enough to hold the array of ImageCodecInfo
   // objects that will be returned by GetImageDecoders.
   pImageCodecInfo = (ImageCodecInfo*)(malloc(size));

   // GetImageDecoders creates an array of ImageCodecInfo objects
   // and copies that array into a previously allocated buffer. 
   // The third argument, imageCodecInfo, is a pointer to that buffer. 
   GetImageDecoders(num, size, pImageCodecInfo);

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
image/x-emf
image/x-wmf
image/tiff
image/png
image/x-icon
```



 

 



