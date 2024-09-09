---
title: Configuring Video Streams for Seeking Performance
description: Configuring Video Streams for Seeking Performance
ms.assetid: 2df507f9-60a5-4489-b3db-7fe15604e625
keywords:
- streams,configuring video streams
- codecs,configuring video streams
- video streams,configuring
- video streams,performance
- performance,video streams
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Configuring Video Streams for Seeking Performance

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Some playback applications perform a lot of seeking on individual streams. Seeking is an area where performance can vary greatly depending upon the settings of the stream. If you know your content needs to be optimized for quick seeking, you can tailor your stream configuration to improve performance.

The biggest factor affecting the speed of seeking operations in video is the spacing of the key frames. Because every frame between key frames needs to be reconstructed based on the frames that come before it, widely spaced key frames result longer seek times. For example, if a video stream with 30 frames per second has a maximum key-frame spacing of 10 seconds, there are potentially 300 frames between key frames. If you seek to the last [*delta frame*](wmformat-glossary.md), 299 frames have to be reconstructed for the frame to be decompressed. If each frame reconstruction took .01 second, the seek would take almost 3 seconds. If you want to increase the efficiency of seeking, lowering the key-frame spacing can help. However, if you set the key frames too close together, you can lose quality.

You can set the maximum key-frame spacing by calling [**IWMVideoMediaProps::SetMaxKeyFrameSpacing**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmvideomediaprops-setmaxkeyframespacing). The recommended values, based on the bit rate of the stream, are listed in the following table. These values provide a good balance of seeking performance and quality. The SDK does not enforce any limit on the time between key frames. In general, times longer than 30 seconds can adversely affect seek times both when the content is streamed over a network, and when it is played back locally.



| Bit rate             | Suggested maximum key-frame spacing |
|----------------------|-------------------------------------|
| 22 Kbps to 300 Kbps  | 8 seconds                           |
| 300 Kbps to 600 Kbps | 6 seconds                           |
| 600 Kbps to 2 Mbps   | 4 seconds                           |
| 2 Mbps and higher    | 3 seconds                           |



 

For more information about getting the best performance when seeking video files, see [Getting the Best Video Seeking Performance](getting-the-best-video-seeking-performance.md).

## Related topics

<dl> <dt>

[**Configuring Streams**](configuring-streams.md)
</dt> </dl>

 

 




