---
title: Image-Data Compression
description: Image-Data Compression
ms.assetid: 689cf403-cbb5-4ccb-a05b-0caa617430ed
keywords:
- video compression manager (VCM),image-data compression
- VCM (video compression manager),image-data compression
- ICCompress function
ms.topic: article
ms.date: 05/31/2018
---

# Image-Data Compression

Your application can use a series of [**ICCompress**](/windows/desktop/api/Vfw/nf-vfw-iccompress) functions and macros to compress data. The functions and macros can help you perform the following tasks:

-   Determine the compression format to use for a specified input format.
-   Prepare the compressor.
-   Compress the data.
-   End compression.

Your application can increase control over the compression process by using the [**ICCompress**](/windows/desktop/api/Vfw/nf-vfw-iccompress) functions and macros. This group of functions and macros handles individual frames, rather than the sequence as a whole. For example, your application can identify the frames to compress as key frames by using the **ICCompress** function.

A compressor receives data in one format, compresses the data, and returns a compressed version of the data using a specified format. The typical input format specifies DIBs using the [**BITMAPINFO**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfo) structure. The typical output format specifies compressed DIBs, also using the **BITMAPINFO** structure.

> [!Note]  
> To minimize image and audio degradation during playback, avoid compressing an AVI file more than once. Combine uncompressed pieces of video in your editing system and then compress the final product.

 

## Compressor and Compression Format Selection

If you want to compress data and your application requires a specific output format, send the [**ICM\_COMPRESS\_QUERY**](icm-compress-query.md) message (or use the [**ICCompressQuery**](/windows/desktop/api/Vfw/nf-vfw-iccompressquery) macro) to query the compressor to determine if it supports the input and output formats.

If the output format is not important to your application, you need only find a compressor that can handle the input format. To determine if a compressor can handle the input format, you can send **ICM\_COMPRESS\_QUERY**, specifying **NULL** for the *lParam* parameter. This message does not return the output format to your application. Your application can determine the buffer size needed for the data specifying the compression format by sending the [**ICM\_COMPRESS\_GET\_FORMAT**](icm-compress-get-format.md) message (or use the [**ICCompressGetFormatSize**](/windows/desktop/api/Vfw/nf-vfw-iccompressgetformatsize) macro). You can also retrieve the format data by sending ICM\_COMPRESS\_GET\_FORMAT (or the [**ICCompressGetFormat**](/windows/desktop/api/Vfw/nf-vfw-iccompressgetformat) macro).

If you want to determine the largest buffer that the compressor could require for compression, send the [**ICM\_COMPRESS\_GET\_SIZE**](icm-compress-get-size.md) message (or use the [**ICCompressGetSize**](/windows/desktop/api/Vfw/nf-vfw-iccompressgetsize) macro). You can use the number of bytes returned by the [**ICSendMessage**](/windows/desktop/api/Vfw/nf-vfw-icsendmessage) function to allocate a buffer for subsequent image compressions.

## Compressor Initialization

After your application selects a compressor that can handle the input and output formats it needs, you can initialize the compressor by using the [**ICM\_COMPRESS\_BEGIN**](icm-compress-begin.md) message (or use the [**ICCompressBegin**](/windows/desktop/api/Vfw/nf-vfw-iccompressbegin) macro). This message requires the compressor handle and the input and output formats.

## Data Compression

You can use the [**ICCompress**](/windows/desktop/api/Vfw/nf-vfw-iccompress) function to compress a frame. Your application must use this function repeatedly until all the frames in a sequence are compressed. Your application must also track and increment the number of each frame compressed with **ICCompress**. The compressor uses this value to check if frames are sent out of order during fast temporal compression (storing differences between successive frames). If your application recompresses a frame, it should use the same frame number as when the frame was first compressed. If your application compresses a still-frame image, it can specify a frame number of zero.

Your application can use the **ICCOMPRESS\_KEYFRAME** flag to make the frame compressed by [**ICCompress**](/windows/desktop/api/Vfw/nf-vfw-iccompress) a key frame.

When VCM returns control to your application after compressing a frame, VCM stores the compressed data in the structures referenced by the *lpbiOutput* and *lpData* parameters. If your application needs to move the compressed data, it can find its size in the *biSizeImage* member of the [**BITMAPINFO**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfo) structure specified in *lpbiOutput*.

> [!Note]  
> Your application must allocate the structures and buffers that store the uncompressed and compressed data. If the compressor supports temporal compression, your application must also allocate a structure and buffer to hold the format and data for the previous frame of information.

 

## Ending Compression

After your application has compressed the data, it can use the [**ICCompressEnd**](/windows/desktop/api/Vfw/nf-vfw-iccompressend) macro to notify the compressor that it has finished. If you want to restart compression after using this function, your application must reinitialize the compressor by sending the [**ICM\_COMPRESS\_BEGIN**](icm-compress-begin.md) message (or use the [**ICCompressBegin**](/windows/desktop/api/Vfw/nf-vfw-iccompressbegin) macro).

 

 