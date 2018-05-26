---
Description: The SetDIBitsToDevice function uses color data from a DIB to set the pixels in the specified rectangle on the device that is associated with the destination device context.
ms.assetid: 7cbb2b7a-2d95-4352-9e75-aa814e8f01bd
title: Testing a Printer for JPEG or PNG Support
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Testing a Printer for JPEG or PNG Support

The [**SetDIBitsToDevice**](/windows/win32/Wingdi/nf-wingdi-setdibitstodevice?branch=master) function uses color data from a DIB to set the pixels in the specified rectangle on the device that is associated with the destination device context.

[**SetDIBitsToDevice**](/windows/win32/Wingdi/nf-wingdi-setdibitstodevice?branch=master) is extended to allow a JPEG or PNG image to be passed as the source image.

For example:


```C++
// 
// pvJpgImage points to a buffer containing the JPEG image 
// nJpgImageSize is the size of the buffer 
// ulJpgWidth is the width of the JPEG image 
// ulJpgHeight is the height of the JPEG image 
// 

// 
// Check if CHECKJPEGFORMAT is supported (device has JPEG support) 
// and use it to verify that device can handle the JPEG image. 
// 

ul = CHECKJPEGFORMAT;

if (
    // Check if CHECKJPEGFORMAT exists: 

    (ExtEscape(hdc, QUERYESCSUPPORT,
               sizeof(ul), &amp;ul, 0, 0) > 0) &amp;&amp;

    // Check if CHECKJPEGFORMAT executed without error: 

    (ExtEscape(hdc, CHECKJPEGFORMAT,
               pvJpgImage, nJpgImageSize, sizeof(ul), &amp;ul) > 0) &amp;&amp;

    // Check status code returned by CHECKJPEGFORMAT: 

    (ul == 1)
   )
{
    // 
    // Initialize the BITMAPINFO. 
    // 

    memset(&amp;bmi, 0, sizeof(bmi));
    bmi.bmiHeader.biSize        = sizeof(BITMAPINFOHEADER);
    bmi.bmiHeader.biWidth       = ulJpgWidth;
    bmi.bmiHeader.biHeight      = -ulJpgHeight; // top-down image 
    bmi.bmiHeader.biPlanes      = 1;
    bmi.bmiHeader.biBitCount    = 0;
    bmi.bmiHeader.biCompression = BI_JPEG;
    bmi.bmiHeader.biSizeImage   = nJpgImageSize;

    // 
    // Do the SetDIBitsToDevice. 
    // 

    iRet = SetDIBitsToDevice(hdc,
                             ulDstX, ulDstY,
                             ulDstWidth, ulDstHeight,
                             0, 0,
                             0, ulJpgHeight,
                             pvJpgImage,
                             &amp;bmi,
                             DIB_RGB_COLORS);

    if (iRet == GDI_ERROR)
        return FALSE;
}
else
{
    // 
    // Decompress image into a DIB and call SetDIBitsToDevice  
    // with the DIB instead. 
    // 
}
```



 

 



