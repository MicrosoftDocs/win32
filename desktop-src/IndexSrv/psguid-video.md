---
title: PSGUID\_VIDEO
description: PSGUID\_VIDEO
ms.assetid: cb12df54-10c5-488a-880d-a53b4ac0588f
keywords:
- PSGUID_VIDEO
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PSGUID\_VIDEO

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The PSGUID\_VIDEO property set defines properties for video files.

``` syntax
#define PSGUID_VIDEO {0x64440491, 0x4c8b, 0x11d1, 0x8b, 0x70, 0x8, \
    0x0, 0x36, 0xb1, 0x1a, 0x3}
```

### Remarks

The PSGUID\_VIDEO property set contains the following property constants:

<dl> <dt>

<span id="PIDVSI_STREAM_NAME"></span><span id="pidvsi_stream_name"></span>PIDVSI\_STREAM\_NAME
</dt> <dd>

Property ID 0x00000002. Indicates the name for the video stream.

</dd> <dt>

<span id="PIDVSI_FRAME_WIDTH"></span><span id="pidvsi_frame_width"></span>PIDVSI\_FRAME\_WIDTH
</dt> <dd>

Property ID 0x00000003. Indicates the frame width for the video stream.

</dd> <dt>

<span id="PIDVSI_FRAME_HEIGHT"></span><span id="pidvsi_frame_height"></span>PIDVSI\_FRAME\_HEIGHT
</dt> <dd>

Property ID 0x00000004. Indicates the frame height for the video stream.

</dd> <dt>

<span id="PIDVSI_TIMELENGTH"></span><span id="pidvsi_timelength"></span>PIDVSI\_TIMELENGTH
</dt> <dd>

Property ID 0x00000007. Indicates the length, in milliseconds, of the video stream.

</dd> <dt>

<span id="PIDVSI_FRAME_COUNT"></span><span id="pidvsi_frame_count"></span>PIDVSI\_FRAME\_COUNT
</dt> <dd>

Property ID 0x00000005. Indicates the number of frames in the video stream.

</dd> <dt>

<span id="PIDVSI_FRAME_RATE"></span><span id="pidvsi_frame_rate"></span>PIDVSI\_FRAME\_RATE
</dt> <dd>

Property ID 0x00000006. Indicates the frame rate, in frames per millisecond, for the video stream.

</dd> <dt>

<span id="PIDVSI_DATA_RATE"></span><span id="pidvsi_data_rate"></span>PIDVSI\_DATA\_RATE
</dt> <dd>

Property ID 0x00000008. Indicates the date rate, in bytes per second, for the video stream.

</dd> <dt>

<span id="PIDVSI_SAMPLE_SIZE"></span><span id="pidvsi_sample_size"></span>PIDVSI\_SAMPLE\_SIZE
</dt> <dd>

Property ID 0x00000009. Indicates the sample size for the video stream.

</dd> <dt>

<span id="PIDVSI_COMPRESSION"></span><span id="pidvsi_compression"></span>PIDVSI\_COMPRESSION
</dt> <dd>

Property ID 0x0000000A. Indicates the level of compression for the video stream.

</dd> </dl>

## Related topics

<dl> <dt>

[PSGUID\_AUDIO](psguid-audio.md)
</dt> <dt>

[PSGUID\_DRM](psguid-drm.md)
</dt> <dt>

[PSGUID\_IMAGESUMMARYINFORMATION](psguid-imagesummaryinformation.md)
</dt> <dt>

[PSGUID\_MUSIC](psguid-music.md)
</dt> </dl>

 

 




