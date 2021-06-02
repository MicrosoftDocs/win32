---
description: Exposing Capture and Compression Formats
ms.assetid: f7466cfe-b13e-4ee9-82f9-0528ed97bf99
title: Exposing Capture and Compression Formats
ms.topic: article
ms.date: 05/31/2018
---

# Exposing Capture and Compression Formats

This article describes how to return capture and compression formats by using the [**IAMStreamConfig::GetStreamCaps**](/windows/desktop/api/Strmif/nf-strmif-iamstreamconfig-getstreamcaps) method. This method can get more information about accepted media types than the traditional way of enumerating a pin's media types, so it should typically be used instead. **GetStreamCaps** can return information about the kinds of formats allowed for audio or video. Additionally, this article provides some sample code that demonstrates how to reconnect the input pin of a transform filter to ensure your filter can produce a particular output.

The **GetStreamCaps** method returns an array of pairs of media type and capabilities structures. The media type is an [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure and the capabilities are represented either by an [**AUDIO\_STREAM\_CONFIG\_CAPS**](/windows/win32/api/strmif/ns-strmif-audio_stream_config_caps) structure or a [**VIDEO\_STREAM\_CONFIG\_CAPS**](/windows/win32/api/strmif/ns-strmif-video_stream_config_caps) structure. The first section in this article presents a video example and the second presents an audio example.

This article contains the following topics:

-   [Video Capabilities](video-capabilities.md)
-   [Audio Capabilities](audio-capabilities.md)
-   [Reconnecting Your Input to Ensure Specific Output Types](reconnecting-your-input-to-ensure-specific-output-types.md)

## Related topics

<dl> <dt>

[Writing DirectShow Filters](writing-directshow-filters.md)
</dt> </dl>

 

 



