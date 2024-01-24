---
title: Reading from a Stream
description: Reading from a Stream
ms.assetid: be961f06-cf5f-4093-9b31-7d1d69e62fec
keywords:
- AVIStreamInfo function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Reading from a Stream

\[The feature associated with this page, [AVIFile Functions and Macros](/windows/win32/multimedia/avifile-functions-and-macros), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader). **Source Reader** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** instead of **AVIFile Functions and Macros**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can retrieve information about an open stream by using the [**AVIStreamInfo**](/windows/desktop/api/Vfw/nf-vfw-avistreaminfoa) function. This function fills the [**AVISTREAMINFO**](/windows/desktop/api/Vfw/ns-vfw-avistreaminfoa) structure with information such as the type of data in the stream, the compression method used when writing stream data, the suggested buffer size, the playback rate, and a text description of the stream.

Some members of the [**AVISTREAMINFO**](/windows/desktop/api/Vfw/ns-vfw-avistreaminfoa) structure are also present in the [**AVIFILEINFO**](/windows/desktop/api/Vfw/ns-vfw-avifileinfoa) structure. The information in the **AVIFILEINFO** structure applies to the entire file. The information in the **AVISTREAMINFO** structure is specific to the accessed stream and has precedence over the information in the **AVIFILEINFO** structure.

If a stream has supplementary information associated with it, you can retrieve this information by using the [**AVIStreamReadData**](/windows/desktop/api/Vfw/nf-vfw-avistreamreaddata) function. This function returns the information in an application-supplied buffer. Supplementary stream information might include configuration settings for the compression and decompression methods used on a stream. You can obtain the required buffer size by using the [**AVIStreamDataSize**](/windows/desktop/api/Vfw/nf-vfw-avistreamdatasize) macro.

You can retrieve formatting information about a stream by using the [**AVIStreamReadFormat**](/windows/desktop/api/Vfw/nf-vfw-avistreamreadformat) function. This function returns a stream-specific structure in an application-supplied buffer. For a video stream, the buffer contains formatting information in a [**BITMAPINFO**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfo) structure. For an audio stream, the buffer contains formatting information in a [**WAVEFORMATEX**](/windows/win32/api/mmeapi/ns-mmeapi-waveformatex) or [**PCMWAVEFORMAT**](/windows/win32/api/mmreg/ns-mmreg-pcmwaveformat) structure. For other stream types, the stream handler returns information specific to the stream. You can determine the required buffer size by using **AVIStreamReadFormat** and specifying a **NULL** buffer address or by using the [**AVIStreamFormatSize**](/windows/desktop/api/Vfw/nf-vfw-avistreamformatsize) macro.

You can retrieve the multimedia content in a stream by using the [**AVIStreamRead**](/windows/desktop/api/Vfw/nf-vfw-avistreamread) function. This function copies raw data from the stream into an application-supplied buffer. For video streams, this function retrieves the bitmapped images that make up the frame content. For audio streams, this function retrieves waveform-audio samples that make up the sound content. You can determine the required buffer size by using **AVIStreamRead** and specifying a **NULL** buffer address or by using the [**AVIStreamSampleSize**](/windows/desktop/api/Vfw/nf-vfw-avistreamsamplesize) macro.

Some AVI stream handlers introduce delays associated with software and hardware initialization or coordination. You can inform these handlers to prepare for data streaming by using the [**AVIStreamBeginStreaming**](/windows/desktop/api/Vfw/nf-vfw-avistreambeginstreaming) function. This function lets the stream handler allocate and initialize the resources it needs. To inform these handlers when streaming has ended, use the [**AVIStreamEndStreaming**](/windows/desktop/api/Vfw/nf-vfw-avistreamendstreaming) function. This function lets the stream handler deallocate the resources it allocated for **AVIStreamBeginStreaming**.

The [**AVIStreamRead**](/windows/desktop/api/Vfw/nf-vfw-avistreamread) function does not provide decompression services. For information about compressing and decompressing audio streams, see [Audio Compression Manager](audio-compression-manager.md). For information about compressing and decompressing video streams, see [Video Compression Manager](video-compression-manager.md). For information about compressing and decompressing individual frames in a video stream, see [Working with Compressed Video Data in a Stream](working-with-compressed-video-data-in-a-stream.md).

## Related topics

<dl> <dt>

[Stream Operations](stream-operations.md)
</dt> </dl>

 

 