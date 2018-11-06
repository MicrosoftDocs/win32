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
ms.date: 05/31/2018
---

# Low-Delay Audio

Low-delay audio is an encoding mode that produces compressed audio with a smaller buffer-window setting than other modes. This is useful for streams that need to be switched quickly during playback. The typical scenario for this feature is a streamed presentation that includes the ability to arbitrarily switch content, like changing the channel of a television.

When you use a low-delay audio format, the latency for switching content is drastically reduced compared to other audio formats. Latency is also reduced for live broadcasts when you use low-delay formats.

This feature is supported by the Windows Media Audio 9.1 and Windows Media Audio 9.1 Professional codecs. Low-delay formats are available only for constant bit rate encoding (both one-pass and two-pass).

## Related topics

<dl> <dt>

[**Codec Features**](codec-features.md)
</dt> </dl>

 

 




