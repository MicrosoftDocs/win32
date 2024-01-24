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
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Compressing Data

\[The feature associated with this page, [Video Compression Manager](/windows/win32/multimedia/video-compression-manager), is a legacy feature. Microsoft strongly recommends that new code does not use this feature.\]

The following example compresses image data for use in an AVI file. It assumes the compressor does not support the VIDCF\_CRUNCH or VIDCF\_TEMPORAL flags, but it does support VIDCF\_QUALITY. The example uses the [**ICCompressBegin**](/windows/desktop/api/Vfw/nf-vfw-iccompressbegin) macro, the [**ICCompress**](/windows/desktop/api/Vfw/nf-vfw-iccompress) function, and the [**ICCompressEnd**](/windows/desktop/api/Vfw/nf-vfw-iccompressend) macro.


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
            &dwCkID, &dwCompFlags, lFrameNum, 
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



 

 




