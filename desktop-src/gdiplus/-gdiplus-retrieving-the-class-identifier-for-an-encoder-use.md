---
description: The function GetEncoderClsid in the following example receives the MIME type of an encoder and returns the class identifier (CLSID) of that encoder.
ms.assetid: f78dac7c-4bc1-4614-8a26-d99d5619399a
title: Retrieving the Class Identifier for an Encoder
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving the Class Identifier for an Encoder

The function GetEncoderClsid in the following example receives the MIME type of an encoder and returns the class identifier (**CLSID**) of that encoder. The MIME types of the encoders built into Windows GDI+ are as follows:

-   image/bmp
-   image/jpeg
-   image/gif
-   image/tiff
-   image/png

The function calls [**GetImageEncoders**](/windows/desktop/api/Gdiplusimagecodec/nf-gdiplusimagecodec-getimageencoders) to get an array of [**ImageCodecInfo**](/windows/win32/api/gdiplusimaging/nl-gdiplusimaging-imagecodecinfo) objects. If one of the **ImageCodecInfo** objects in that array represents the requested encoder, the function returns the index of the **ImageCodecInfo** object and copies the **CLSID** into the variable pointed to by **pClsid**. If the function fails, it returns –1.


```
int GetEncoderClsid(const WCHAR* format, CLSID* pClsid)
{
   UINT  num = 0;          // number of image encoders
   UINT  size = 0;         // size of the image encoder array in bytes

   ImageCodecInfo* pImageCodecInfo = NULL;

   GetImageEncodersSize(&num, &size);
   if(size == 0)
      return -1;  // Failure

   pImageCodecInfo = (ImageCodecInfo*)(malloc(size));
   if(pImageCodecInfo == NULL)
      return -1;  // Failure

   GetImageEncoders(num, size, pImageCodecInfo);

   for(UINT j = 0; j < num; ++j)
   {
      if( wcscmp(pImageCodecInfo[j].MimeType, format) == 0 )
      {
         *pClsid = pImageCodecInfo[j].Clsid;
         free(pImageCodecInfo);
         return j;  // Success
      }    
   }

   free(pImageCodecInfo);
   return -1;  // Failure
}
```



The following console application calls the GetEncoderClsid function to determine the **CLSID** of the PNG encoder:


```
#include <windows.h>
#include <gdiplus.h>
#include <stdio.h>
using namespace Gdiplus;

#include "GdiplusHelperFunctions.h"

INT main()
{
   // Initialize GDI+.
   GdiplusStartupInput gdiplusStartupInput;
   ULONG_PTR gdiplusToken;
   GdiplusStartup(&gdiplusToken, &gdiplusStartupInput, NULL);

   CLSID  encoderClsid;
   INT    result;
   WCHAR  strGuid[39];

   result = GetEncoderClsid(L"image/png", &encoderClsid);

   if(result < 0)
   {
      printf("The PNG encoder is not installed.\n");
   }
   else
   {
      StringFromGUID2(encoderClsid, strGuid, 39);
      printf("An ImageCodecInfo object representing the PNG encoder\n");
      printf("was found at position %d in the array.\n", result);
      wprintf(L"The CLSID of the PNG encoder is %s.\n", strGuid);
   }

   GdiplusShutdown(gdiplusToken);
   return 0;
}
```



When you run the preceding console application, you get an output similar to the following:


```
An ImageCodecInfo object representing the PNG encoder
was found at position 4 in the array.
The CLSID of the PNG encoder is {557CF406-1A04-11D3-9A73-0000F81EF32E}.
```



 

 
