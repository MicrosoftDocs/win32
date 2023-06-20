---
title: Implementing a Video DSP Plug-in
description: Implementing a Video DSP Plug-in
ms.assetid: 36c06c57-7623-430b-8280-9dba7b0a2e9b
keywords:
- Windows Media Player plug-ins,video DSP
- plug-ins,video DSP
- digital signal processing plug-ins,implementing code
- DSP plug-ins,implementing code
- digital signal processing plug-ins,modifying sample code
- DSP plug-ins,modifying sample code
- digital signal processing plug-ins,video implementation
- DSP plug-ins,video implementation
- video DSP plug-ins,implementing code
- video DSP plug-ins,modifying sample code
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Implementing a Video DSP Plug-in

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Computer video display adapters support a set of video formats. Digital video codecs also support a set of video formats. When attempting to play a particular video file, Windows Media Player must choose a format to use for rendering. The Player attempts to find the best match between the formats supported by the video codec and the formats supported by the video display adapter—that is, the one that yields the highest quality.

To create a Windows Media Player DSP plug-in that processes video, you'll first need to decide which video formats you'd like your plug-in to process. The sample video DSP plug-in works with the following video formats:

-   NV12
-   YV12
-   YUY2
-   UYVY
-   RGB32
-   RGB24
-   RGB555
-   RGB565

Which formats you choose to process is up to you. You can remove formats from the sample plug-in so that they aren't supported any longer and you can add code to process additional formats.

The following sections provide additional information you should know before creating your own video DSP plug-in for Windows Media Player:

-   [Video Format Negotiation in the Sample Video DSP Plug-in](video-format-negotiation-in-the-sample-video-dsp-plug-in.md)
-   [DoProcessOutput in the Sample Video DSP Plug-in](doprocessoutput-in-the-sample-video-dsp-plug-in.md)
-   [Processing the Video](processing-the-video.md)

## Related topics

<dl> <dt>

[**Implementing Your DSP Code**](implementing-your-dsp-code.md)
</dt> </dl>

 

 




