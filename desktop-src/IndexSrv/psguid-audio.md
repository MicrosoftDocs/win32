---
Description: PSGUID\_AUDIO
ms.assetid: dca5f205-956e-4ec7-b79c-ce007a6c9384
title: PSGUID\_AUDIO
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PSGUID\_AUDIO

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The PSGUID\_AUDIO property set defines properties for audio files.

``` syntax
#define PSGUID_AUDIO {0x64440490, 0x4c8b, 0x11d1, 0x8b, 0x70, 0x8, \
    0x0, 0x36, 0xb1, 0x1a, 0x3}
```

### Remarks

The PSGUID\_AUDIO property set contains the following property constants:

<dl> <dt>

<span id="PIDASI_FORMAT"></span><span id="pidasi_format"></span>PIDASI\_FORMAT
</dt> <dd>

Property ID 0x00000002. Indicates the format of the audio file.

</dd> <dt>

<span id="PIDASI_TIMELENGTH"></span><span id="pidasi_timelength"></span>PIDASI\_TIMELENGTH
</dt> <dd>

Property ID 0x00000003. Indicates the length, in milliseconds, of the audio file.

</dd> <dt>

<span id="PIDASI_AVG_DATA_RATE"></span><span id="pidasi_avg_data_rate"></span>PIDASI\_AVG\_DATA\_RATE
</dt> <dd>

Property ID 0x00000004. Indicates the average data rate, in Hz, for the audio file.

</dd> <dt>

<span id="PIDASI_SAMPLE_RATE"></span><span id="pidasi_sample_rate"></span>PIDASI\_SAMPLE\_RATE
</dt> <dd>

Property ID 0x00000005. Indicates the audio sample rate, in bits, for the audio file.

</dd> <dt>

<span id="PIDASI_SAMPLE_SIZE"></span><span id="pidasi_sample_size"></span>PIDASI\_SAMPLE\_SIZE
</dt> <dd>

Property ID 0x00000006. Indicates the audio sample size, in bits, for the audio file.

</dd> <dt>

<span id="PIDASI_CHANNEL_COUNT"></span><span id="pidasi_channel_count"></span>PIDASI\_CHANNEL\_COUNT
</dt> <dd>

Property ID 0x00000007. Indicates the channel count for the audio file.

</dd> </dl>

## Related topics

<dl> <dt>

[PSGUID\_DRM](psguid-drm.md)
</dt> <dt>

[PSGUID\_IMAGESUMMARYINFORMATION](psguid-imagesummaryinformation.md)
</dt> <dt>

[PSGUID\_MUSIC](psguid-music.md)
</dt> <dt>

[PSGUID\_VIDEO](psguid-video.md)
</dt> </dl>

 

 



