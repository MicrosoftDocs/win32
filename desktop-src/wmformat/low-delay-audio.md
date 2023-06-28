---
title: Low-Delay Audio
description: Low-Delay Audio
ms.assetid: f93819eb-f38a-45a0-aa1b-4e677e33daf8
keywords:
- Windows Media Format SDK,low-delay audio
- Windows Media Format SDK,audio support
- codecs,low-delay audio
- codecs,audio support
- low-delay audio
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Low-Delay Audio

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Low-delay audio is an encoding mode that produces compressed audio with a smaller buffer-window setting than other modes. This is useful for streams that need to be switched quickly during playback. The typical scenario for this feature is a streamed presentation that includes the ability to arbitrarily switch content, like changing the channel of a television.

When you use a low-delay audio format, the latency for switching content is drastically reduced compared to other audio formats. Latency is also reduced for live broadcasts when you use low-delay formats.

This feature is supported by the Windows Media Audio 9.1 and Windows Media Audio 9.1 Professional codecs. Low-delay formats are available only for constant bit rate encoding (both one-pass and two-pass).

## Related topics

<dl> <dt>

[**Codec Features**](codec-features.md)
</dt> </dl>

 

 




