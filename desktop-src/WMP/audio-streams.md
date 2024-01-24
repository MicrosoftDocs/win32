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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Audio Streams

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Online stores can provide music as a stream from a music server. This is useful for providing samples, special promotional items, or to enable subscription users to enjoy music without having to download the content. It is common not to store the URL of the stream as part of the music catalog, but instead to resolve the URL just before playback based upon the track ID. To enable this, Windows Media Player calls [IWMPContentPartner::GetStreamingURL](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-getstreamingurl) and provides the streaming type (as a [WMPStreamingType](/previous-versions/windows/desktop/api/contentpartner/ne-contentpartner-wmpstreamingtype) enumeration value) and the ID for the stream. The plug-in returns the URL for the stream through the *pbstrURL* parameter.

## Related topics

<dl> <dt>

[**About Type 1 Online Stores**](about-type-1-online-stores.md)
</dt> </dl>

 

 




