---
title: Image-Data Decompression
description: Image-Data Decompression
ms.assetid: 4bff02be-dac8-41f4-a3af-2da6a2693ffe
keywords:
- video compression manager (VCM),image-data decompression
- VCM (video compression manager),image-data decompression
- ICDecompressEx functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Image-Data Decompression

Your application uses a series of [**ICDecompressEx**](/windows/win32/Vfw/nf-vfw-icdecompressex?branch=master) functions to control the decompressor. The functions can help you perform the following tasks:

-   Select a decompressor.
-   Prepare the decompressor.
-   Decompress the data.
-   End decompression.

Your application handles decompression similarly to the way it handles compression, except that the input format is a compressed format and the output format is a displayable format. The input format for decompression is usually obtained from the stream header. After determining the input format, your application can use the [**ICLocate**](/windows/win32/Vfw/nf-vfw-iclocate?branch=master) or [**ICOpen**](/windows/win32/Vfw/nf-vfw-icopen?branch=master) functions to find a decompressor that can handle it.

The [**ICDecompressEx**](/windows/win32/Vfw/nf-vfw-icdecompressex?branch=master) functions and macros are a superset of the [**ICDecompress**](/windows/win32/Vfw/nf-vfw-icdecompress?branch=master) function group and provide more capabilities. The functionality of **ICDecompressEx**, [**ICDecompressExBegin**](/windows/win32/Vfw/nf-vfw-icdecompressexbegin?branch=master), [**ICDecompressExEnd**](/windows/win32/Vfw/nf-vfw-icdecompressexend?branch=master), and [**ICDecompressExQuery**](/windows/win32/Vfw/nf-vfw-icdecompressexquery?branch=master) replaces that of the **ICDecompress**, [**ICDecompressBegin**](/windows/win32/Vfw/nf-vfw-icdecompressbegin?branch=master), [**ICDecompressEnd**](/windows/win32/Vfw/nf-vfw-icdecompressend?branch=master), and [**ICDecompressQuery**](/windows/win32/Vfw/nf-vfw-icdecompressquery?branch=master) functions. Use the **ICDecompressEx** functions and macros in place of the **ICDecompress** equivalents.

## Decompressor and Decompression Format Selection

If you want to decompress data and your application requires a specific output format, you can use the [**ICDecompressExQuery**](/windows/win32/Vfw/nf-vfw-icdecompressexquery?branch=master) function to query the decompressor to determine if it supports the input and output formats.

If the output format is not important in your application, you need only find a decompressor that can handle the input format. To determine if a decompressor can handle the input format, use [**ICDecompressExQuery**](/windows/win32/Vfw/nf-vfw-icdecompressexquery?branch=master) and specify **NULL** for the *lpbiDst* parameter. Your application can determine the buffer size needed for the data specifying the decompression format by sending the [**ICM\_DECOMPRESS\_GET\_FORMAT**](icm-decompress-get-format.md) message (or use the [**ICDecompressGetFormatSize**](/windows/win32/Vfw/nf-vfw-icdecompressgetformatsize?branch=master) macro). You can also send **ICM\_DECOMPRESS\_GET\_FORMAT** (or the [**ICDecompressGetFormat**](/windows/win32/Vfw/nf-vfw-icdecompressgetformat?branch=master) macro) to retrieve the format data. The decompressor returns its suggested format in a [**BITMAPINFO**](https://msdn.microsoft.com/library/windows/desktop/dd183375) structure. This format typically preserves the most information during decompression. Your application should ensure that the decompressor returns successfully before it decompresses the information.

Because your application allocates the memory required for decompression, it needs to determine the maximum memory the decompressor can require for the output format. The **ICM\_DECOMPRESS\_GET\_FORMAT** message obtains the number of bytes the decompressor uses for the default format.

If your application defines its own format by using [**ICDecompressExQuery**](/windows/win32/Vfw/nf-vfw-icdecompressexquery?branch=master), it must also obtain a palette for the bitmap; **ICDecompressExQuery** does not provide palette definitions. (Most applications use standard formats and do not need to obtain a palette.) Your application can obtain the palette by sending the [**ICM\_DECOMPRESS\_GET\_PALETTE**](icm-decompress-get-palette.md) message (or use the [**ICDecompressGetPalette**](/windows/win32/Vfw/nf-vfw-icdecompressgetpalette?branch=master) macro).

## Decompressor Initialization

After your application selects a decompressor that can handle the input and output formats it needs, you can initialize the decompressor by using the [**ICDecompressExBegin**](/windows/win32/Vfw/nf-vfw-icdecompressexbegin?branch=master) function. This function requires the decompressor handle and the input and output formats.

## Data Decompression

You can use the [**ICDecompressEx**](/windows/win32/Vfw/nf-vfw-icdecompressex?branch=master) function to decompress a frame. Your application must use this function repeatedly until all the frames in a sequence are decompressed.

If your video stream lags behind other components (such as audio) during playback, your application can specify the **ICDECOMPRESS\_HURRYUP** flag to speed decompression. To do this, a decompressor might extract only the information it needs to decompress the next frame and not fully decompress the current frame. Therefore, your application should not try to draw the decompressed data when it uses this flag.

After your application has decompressed the data, it can send the [**ICM\_DECOMPRESSEX\_END**](icm-decompressex-end.md) message (or use the [**ICDecompressExEnd**](/windows/win32/Vfw/nf-vfw-icdecompressexend?branch=master) macro) to notify the decompressor that it has finished. If you want to restart decompression after using this function, your application must reinitialize the decompressor by using [**ICDecompressExBegin**](/windows/win32/Vfw/nf-vfw-icdecompressexbegin?branch=master).

## Related topics

<dl> <dt>

[VCM Services](vcm-services.md)
</dt> </dl>

 

 




