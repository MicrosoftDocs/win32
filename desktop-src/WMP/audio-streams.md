---
title: Audio Streams
description: Audio Streams
ms.assetid: 7bb39c48-5d0b-483d-83ee-946adfc9724f
keywords:
- Windows Media Player online stores,audio streams
- online stores,audio streams
- type 1 online stores,audio streams
- Windows Media Player online stores,streams from music servers
- online stores,streams from music servers
- type 1 online stores,streams from music servers
- Windows Media Player online stores,music server streams
- online stores,music server streams
- type 1 online stores,music server streams
- audio streams
- music server streams
- streams from music servers
ms.topic: article
ms.date: 05/31/2018
---

# Audio Streams

Online stores can provide music as a stream from a music server. This is useful for providing samples, special promotional items, or to enable subscription users to enjoy music without having to download the content. It is common not to store the URL of the stream as part of the music catalog, but instead to resolve the URL just before playback based upon the track ID. To enable this, Windows Media Player calls [IWMPContentPartner::GetStreamingURL](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-getstreamingurl) and provides the streaming type (as a [WMPStreamingType](/previous-versions/windows/desktop/api/contentpartner/ne-contentpartner-wmpstreamingtype) enumeration value) and the ID for the stream. The plug-in returns the URL for the stream through the *pbstrURL* parameter.

## Related topics

<dl> <dt>

[**About Type 1 Online Stores**](about-type-1-online-stores.md)
</dt> </dl>

 

 




