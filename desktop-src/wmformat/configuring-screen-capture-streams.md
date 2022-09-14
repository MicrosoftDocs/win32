---
title: Configuring Screen Capture Streams
description: Configuring Screen Capture Streams
ms.assetid: 974e679f-0bf6-412b-9e80-43370de7605a
keywords:
- streams,configuring screen capture streams
- codecs,configuring screen capture streams
- screen capture streams
ms.topic: article
ms.date: 05/31/2018
---

# Configuring Screen Capture Streams

Streams that use the Windows Media® Video 9 Screen codec are configured by applications in the same way as normal video streams. However, if you set the video complexity level to 0, the writer will ignore any video quality value set with [**IWMVideoMediaProps::SetQuality**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmvideomediaprops-setquality). For more information, see [Getting Good Results with the Windows Media Video 9 Screen Codec](getting-good-results-with-the-windows-media-video-9-screen-codec.md).

## Related topics

<dl> <dt>

[**Configuring Streams**](configuring-streams.md)
</dt> <dt>

[**Configuration Common to All Streams**](configuration-common-to-all-streams.md)
</dt> <dt>

[**Configuring Video Streams**](configuring-video-streams.md)
</dt> </dl>

 

 




