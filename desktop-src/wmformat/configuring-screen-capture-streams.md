---
title: Configuring Screen Capture Streams
description: Configuring Screen Capture Streams
ms.assetid: 974e679f-0bf6-412b-9e80-43370de7605a
keywords:
- streams,configuring screen capture streams
- codecs,configuring screen capture streams
- screen capture streams
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Configuring Screen Capture Streams

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Streams that use the Windows Media® Video 9 Screen codec are configured by applications in the same way as normal video streams. However, if you set the video complexity level to 0, the writer will ignore any video quality value set with [**IWMVideoMediaProps::SetQuality**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmvideomediaprops-setquality). For more information, see [Getting Good Results with the Windows Media Video 9 Screen Codec](getting-good-results-with-the-windows-media-video-9-screen-codec.md).

## Related topics

<dl> <dt>

[**Configuring Streams**](configuring-streams.md)
</dt> <dt>

[**Configuration Common to All Streams**](configuration-common-to-all-streams.md)
</dt> <dt>

[**Configuring Video Streams**](configuring-video-streams.md)
</dt> </dl>

 

 




