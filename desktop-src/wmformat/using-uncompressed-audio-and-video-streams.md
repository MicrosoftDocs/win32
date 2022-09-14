---
title: Using Uncompressed Audio and Video Streams
description: Using Uncompressed Audio and Video Streams
ms.assetid: 1a8fe604-bd99-4ba1-878f-8e1fd89483b3
keywords:
- streams,configuring uncompressed audio and video streams
- codecs,configuring uncompressed audio and video streams
- video streams,uncompressed
- audio streams,uncompressed
- uncompressed audio and video streams
ms.topic: article
ms.date: 05/31/2018
---

# Using Uncompressed Audio and Video Streams

Under most circumstances, uncompressed media has prohibitively large storage and delivery requirements, but for some local playback scenarios, the quality level is important enough to warrant not using compression..

The settings for an uncompressed media stream should reflect the settings of the source media. When configuring an uncompressed stream, you must calculate the bit rate of the media and set the stream appropriately by calling [**IWMStreamConfig::SetBitrate**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstreamconfig-setbitrate). Because uncompressed streams are not viable for streaming, you should always set the buffer window for uncompressed media streams to zero by calling [**IWMStreamConfig::SetBufferWindow**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstreamconfig-setbufferwindow).

The following pixel formats are supported for uncompressed video streams:

-   WMMEDIASUBTYPE\_RGB555
-   WMMEDIASUBTYPE\_RGB24
-   WMMEDIASUBTYPE\_RGB32
-   WMMEDIASUBTYPE\_I420
-   WMMEDIASUBTYPE\_IYUV
-   WMMEDIASUBTYPE\_YV12
-   WMMEDIASUBTYPE\_YUY2
-   WMMEDIASUBTYPE\_UYVY
-   WMMEDIASUBTYPE\_YVYU

## Related topics

<dl> <dt>

[**Configuration Common to All Streams**](configuration-common-to-all-streams.md)
</dt> <dt>

[**Configuring Audio Streams**](configuring-audio-streams.md)
</dt> <dt>

[**Configuring Streams**](configuring-streams.md)
</dt> <dt>

[**Configuring Video Streams**](configuring-video-streams.md)
</dt> </dl>

 

 




