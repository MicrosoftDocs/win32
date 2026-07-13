---
description: This topic describes how to seek during playback using MFPlay.
ms.assetid: 8ccca882-5543-4913-8eb9-8adaed2c57aa
title: How to Seek During Playback
ms.topic: how-to
ms.date: 05/31/2018
---

# How to Seek During Playback

\[The feature associated with this page, MFPlay, is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and  [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This topic describes how to seek during playback using MFPlay.

**To Seek During Playback**

1.  Initialize a **PROPVARIANT** to hold the seek time in 100-nanosecond units, as a **LARGE\_INTEGER** (**VT\_I8**) type.
2.  Call [**IMFPMediaPlayer::SetPosition**](/windows/desktop/api/mfplay/nf-mfplay-imfpmediaplayer-setposition). Specify **MFP\_POSITIONTYPE\_100NS** for the first parameter, and pass in the **PROPVARIANT** for the second parameter.

## Requirements

MFPlay requires Windows 7.

## Related topics

<dl> <dt>

[Using MFPlay for Audio/Video Playback](using-mfplay-for-audio-video-playback.md)
</dt> </dl>

 

 



