---
title: Reading from a Stream
description: Reading from a Stream
ms.assetid: be961f06-cf5f-4093-9b31-7d1d69e62fec
keywords:
- AVIStreamInfo function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Reading from a Stream

You can retrieve information about an open stream by using the [**AVIStreamInfo**](/windows/win32/Vfw/nf-vfw-avistreaminfoa?branch=master) function. This function fills the [**AVISTREAMINFO**](/windows/win32/Vfw/ns-vfw-_avistreaminfoa?branch=master) structure with information such as the type of data in the stream, the compression method used when writing stream data, the suggested buffer size, the playback rate, and a text description of the stream.

Some members of the [**AVISTREAMINFO**](/windows/win32/Vfw/ns-vfw-_avistreaminfoa?branch=master) structure are also present in the [**AVIFILEINFO**](/windows/win32/Vfw/ns-vfw-_avifileinfoa?branch=master) structure. The information in the **AVIFILEINFO** structure applies to the entire file. The information in the **AVISTREAMINFO** structure is specific to the accessed stream and has precedence over the information in the **AVIFILEINFO** structure.

If a stream has supplementary information associated with it, you can retrieve this information by using the [**AVIStreamReadData**](/windows/win32/Vfw/nf-vfw-avistreamreaddata?branch=master) function. This function returns the information in an application-supplied buffer. Supplementary stream information might include configuration settings for the compression and decompression methods used on a stream. You can obtain the required buffer size by using the [**AVIStreamDataSize**](/windows/win32/Vfw/nf-vfw-avistreamdatasize?branch=master) macro.

You can retrieve formatting information about a stream by using the [**AVIStreamReadFormat**](/windows/win32/Vfw/nf-vfw-avistreamreadformat?branch=master) function. This function returns a stream-specific structure in an application-supplied buffer. For a video stream, the buffer contains formatting information in a [**BITMAPINFO**](https://msdn.microsoft.com/library/windows/desktop/dd183375) structure. For an audio stream, the buffer contains formatting information in a [**WAVEFORMATEX**](/windows/win32/Mmreg/?branch=master) or [**PCMWAVEFORMAT**](pcmwaveformat.md) structure. For other stream types, the stream handler returns information specific to the stream. You can determine the required buffer size by using **AVIStreamReadFormat** and specifying a **NULL** buffer address or by using the [**AVIStreamFormatSize**](/windows/win32/Vfw/nf-vfw-avistreamformatsize?branch=master) macro.

You can retrieve the multimedia content in a stream by using the [**AVIStreamRead**](/windows/win32/Vfw/nf-vfw-avistreamread?branch=master) function. This function copies raw data from the stream into an application-supplied buffer. For video streams, this function retrieves the bitmapped images that make up the frame content. For audio streams, this function retrieves waveform-audio samples that make up the sound content. You can determine the required buffer size by using **AVIStreamRead** and specifying a **NULL** buffer address or by using the [**AVIStreamSampleSize**](/windows/win32/Vfw/nf-vfw-avistreamsamplesize?branch=master) macro.

Some AVI stream handlers introduce delays associated with software and hardware initialization or coordination. You can inform these handlers to prepare for data streaming by using the [**AVIStreamBeginStreaming**](/windows/win32/Vfw/nf-vfw-avistreambeginstreaming?branch=master) function. This function lets the stream handler allocate and initialize the resources it needs. To inform these handlers when streaming has ended, use the [**AVIStreamEndStreaming**](/windows/win32/Vfw/nf-vfw-avistreamendstreaming?branch=master) function. This function lets the stream handler deallocate the resources it allocated for **AVIStreamBeginStreaming**.

The [**AVIStreamRead**](/windows/win32/Vfw/nf-vfw-avistreamread?branch=master) function does not provide decompression services. For information about compressing and decompressing audio streams, see [Audio Compression Manager](audio-compression-manager.md). For information about compressing and decompressing video streams, see [Video Compression Manager](video-compression-manager.md). For information about compressing and decompressing individual frames in a video stream, see [Working with Compressed Video Data in a Stream](working-with-compressed-video-data-in-a-stream.md).

## Related topics

<dl> <dt>

[Stream Operations](stream-operations.md)
</dt> </dl>

 

 




