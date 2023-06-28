---
title: Video Complexity Settings
description: Video Complexity Settings
ms.assetid: 60191c07-4467-459c-909a-f0752d2be4a9
keywords:
- Windows Media Format SDK,video complexity settings
- Windows Media Format SDK,complexity settings for video
- codecs,video complexity settings
- codecs,complexity settings for video
- video complexity settings
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Video Complexity Settings

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Some video codecs support multiple *complexity levels*. The complexity level used to encode a stream does not directly affect the bit rate of that stream, but can affect the quality. Where bit rate is a measure of the size of the compressed samples in the ASF file, complexity level is a measure of the processing power needed to reconstruct the compressed data. Complexity level is therefore dictated more by the processing power of the playing platform than by the available bandwidth.

For information about working with complexity levels, see [Configuring Video Streams](configuring-video-streams.md).

## Related topics

<dl> <dt>

[**Codec Features**](codec-features.md)
</dt> </dl>

 

 




