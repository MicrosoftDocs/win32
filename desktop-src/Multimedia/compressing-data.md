---
title: Compressing Data
description: Compressing Data
ms.assetid: b231316b-0c81-410a-b2fe-b58ab7aca02b
keywords:
- video compression manager (VCM),compressing data
- VCM (video compression manager),compressing data
- ICCompressBegin macro
- ICCompress function
- ICCompressEnd macro
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Compressing Data

The following example compresses image data for use in an AVI file. It assumes the compressor does not support the VIDCF\_CRUNCH or VIDCF\_TEMPORAL flags, but it does support VIDCF\_QUALITY. The example uses the [**ICCompressBegin**](/windows/win32/Vfw/nf-vfw-iccompressbegin?branch=master) macro, the [**ICCompress**](/windows/win32/Vfw/nf-vfw-iccompress?branch=master) function, and the [**ICCompressEnd**](/windows/win32/Vfw/nf-vfw-iccompressend?branch=master) macro.


```C++
DWORD dwCkID; 
DWORD dwCompFlags; 
DWORD dwQuality; 
LONG  lNumFrames, lFrameNum; 
// Assume dwNumFrames is initialized to the total number of frames. 
// Assume dwQuality holds the proper quality value (0-10000). 
// Assume lpbiOut, lpOut, lpbiIn, and lpIn are initialized properly. 
 
// If OK to start, compress each frame. 
if (ICCompressBegin(hIC, lpbiIn, lpbiOut) == ICERR_OK)
{ 
    for ( lFrameNum = 0; lFrameNum < lNumFrames; lFrameNum++)
    { 
        if (ICCompress(hIC, 0, lpbiOut, lpOut, lpbiIn, lpIn, 
            &amp;dwCkID, &amp;dwCompFlags, lFrameNum, 
            0, dwQuality, NULL, NULL) == ICERR_OK)
        { 
            // Write compressed data to the AVI file. 
             
            // Set lpIn to the next frame in the sequence. 
             
        } 
        else 
        { 
            // Handle compressor error. 
        } 
    } 
    ICCompressEnd(hIC);    // terminate compression 
} 
else 
{ 
    // Handle the error identifying the unsupported format. 
} 
 
```



 

 




