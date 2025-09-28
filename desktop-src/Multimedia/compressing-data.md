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
ms.topic: concept-article
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

A detailed compress-image-data example, which explains how to write compressed data to the AVI file, can be found in 
[**the SO post**](https://stackoverflow.com/questions/22765194/is-it-possible-to-encode-using-the-mrle-codec-on-video-for-windows-under-windows/79762695#79762695)
. A crucial point of this post states that, when writing the compressed data, we do still need to create the compressed stream, but we no longer write to it, 
as we did it before Windows 8. Instead we write RLE8 encoded data to the raw stream. Also, we do not put the compress loop inside ICCompressBegin/ICCompressEnd 
brackets, because AVIStreamSetFormat sends the ICM_COMPRESS_BEGIN message with lpInput and lpOutput parameters (as the ICCompressBegin macro does) and AVIStreamRelease sends the ICM_COMPRESS_END message (as the ICCompressEnd macro does in the code above):

```C
    DWORD dwCkID;
    DWORD dwCompFlags = AVIIF_KEYFRAME;
    LONG  lNumFrames, lFrameNum = 0;
    LONG lSamplesWritten = 0;
    LONG lBytesWritten = 0;
    // Assume dwNumFrames is initialized to the total number of frames. 
    // Assume dwQuality holds the proper quality value (0-10000). 
    // Assume lpbiOut, lpOut, lpbiIn, and lpIn are initialized properly. 

    if (AVIStreamSetFormat(pCompressedStream, 0, lpbiIn, biSize) != 0)
    {
        std::cout << "AVIStreamSetFormat failed" << std::endl;
        return 1;
    }

    for (int frame = 0; frame < nframes; frame++)
    {
        ICCompress(hIC, 0, lpbiOut, lpOutput, lpbiIn, lpInput,
            &dwCkID, &dwCompFlags, frame, lpbiIn->biSizeImage, dwQuality, NULL, NULL);
        hr = AVIStreamWrite(pStream, frame, 1, lpOutput, lpbiOut->biSizeImage,
            AVIIF_KEYFRAME, &lSamplesWritten, &lBytesWritten);
        if (hr != S_OK)
        {
            std::cout << "AVIStreamWrite failed" << std::endl;
            return 1;
        }
    }

    //GlobalUnlock(...),GlobalFree(...);

    if (AVIStreamRelease(pCompressedStream) != 0 || AVIStreamRelease(pStream) != 0)
    {
        std::cout << "AVIStreamRelease failed" << std::endl;
        return 1;
    }
```

 

 




