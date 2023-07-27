---
description: The following globally unique identifiers (GUIDs) define different time formats.
ms.assetid: '510c7146-ff3c-4812-a7ad-b4051aa82ef3'
title: Time Format GUIDs (Uuids.h)
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Time Format GUIDs

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following globally unique identifiers (GUIDs) define different time formats.



| GUID                                                                                                                                                                                       | Description                                       |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------|
| <span id="TIME_FORMAT_NONE"></span><span id="time_format_none"></span><dl> <dt>**TIME\_FORMAT\_NONE**</dt> </dl>                    | No format.<br/>                             |
| <span id="TIME_FORMAT_FRAME"></span><span id="time_format_frame"></span><dl> <dt>**TIME\_FORMAT\_FRAME**</dt> </dl>                 | Video frames.<br/>                          |
| <span id="TIME_FORMAT_SAMPLE"></span><span id="time_format_sample"></span><dl> <dt>**TIME\_FORMAT\_SAMPLE**</dt> </dl>              | Samples in the stream.<br/>                 |
| <span id="TIME_FORMAT_FIELD"></span><span id="time_format_field"></span><dl> <dt>**TIME\_FORMAT\_FIELD**</dt> </dl>                 | Interlaced video fields.<br/>               |
| <span id="TIME_FORMAT_BYTE"></span><span id="time_format_byte"></span><dl> <dt>**TIME\_FORMAT\_BYTE**</dt> </dl>                    | Byte offset within the stream.<br/>         |
| <span id="TIME_FORMAT_MEDIA_TIME"></span><span id="time_format_media_time"></span><dl> <dt>**TIME\_FORMAT\_MEDIA\_TIME**</dt> </dl> | Reference time (100-nanosecond units).<br/> |



## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Uuids.h (include Dshow.h)</dt> </dl> |



## See also

<dl> <dt>

[Constants and GUIDs](constants-and-guids.md)
</dt> <dt>

[**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking)
</dt> </dl>

 

 




