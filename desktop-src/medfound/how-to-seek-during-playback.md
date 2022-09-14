---
description: This topic describes how to seek during playback using MFPlay.
ms.assetid: 8ccca882-5543-4913-8eb9-8adaed2c57aa
title: How to Seek During Playback
ms.topic: article
ms.date: 05/31/2018
---

# How to Seek During Playback

\[MFPlay is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

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

 

 



