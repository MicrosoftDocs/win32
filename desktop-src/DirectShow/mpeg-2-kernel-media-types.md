---
description: For several MPEG-2 media type GUIDs, the Windows DDK defines names that differ from the names used in DirectShow. The following table shows the DirectShow names (defined in Ksuuids.h) and the corresponding kernel-mode names (defined in Ksmedia.h).
ms.assetid: ecf94552-5a0f-464c-9f9b-4861faa38d05
title: MPEG-2 Kernel Media Types (Dshow.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# MPEG-2 Kernel Media Types

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

For several MPEG-2 media type GUIDs, the Windows DDK defines names that differ from the names used in DirectShow. The following table shows the DirectShow names (defined in Ksuuids.h) and the corresponding kernel-mode names (defined in Ksmedia.h).



| Name in Ksuuids.h              | Name in Ksmedia.h                          |
|--------------------------------|--------------------------------------------|
| FORMAT\_WaveFormatEx           | KSDATAFORMAT\_SPECIFIER\_WAVEFORMATEX      |
| FORMAT\_MPEG2Video             | KSDATAFORMAT\_SPECIFIER\_MPEG2\_VIDEO      |
| MEDIASUBTYPE\_ATSC\_SI         | KSDATAFORMAT\_SUBTYPE\_ATSC\_SI            |
| MEDIASUBTYPE\_DOLBY\_AC3       | KSDATAFORMAT\_SUBTYPE\_AC3\_AUDIO          |
| MEDIASUBTYPE\_DVB\_SI          | KSDATAFORMAT\_SUBTYPE\_DVB\_SI             |
| MEDIASUBTYPE\_DVD\_LPCM\_AUDIO | KSDATAFORMAT\_SUBTYPE\_LPCM\_AUDIO         |
| MEDIASUBTYPE\_MPEG2\_AUDIO     | KSDATAFORMAT\_SUBTYPE\_MPEG2\_AUDIO        |
| MEDIASUBTYPE\_MPEG2\_PROGRAM   | STATIC\_KSDATAFORMAT\_TYPE\_MPEG2\_PROGRAM |
| MEDIASUBTYPE\_MPEG2\_TRANSPORT | KSDATAFORMAT\_TYPE\_MPEG2\_TRANSPORT       |
| MEDIASUBTYPE\_MPEG2\_VIDEO     | KSDATAFORMAT\_SUBTYPE\_MPEG2\_VIDEO        |
| MEDIATYPE\_MPEG2\_SECTIONS     | KSDATAFORMAT\_TYPE\_MPEG2\_SECTIONS        |
| MEDIATYPE\_Audio               | KSDATAFORMAT\_TYPE\_AUDIO                  |
| MEDIATYPE\_MPEG2\_PES          | KSDATAFORMAT\_TYPE\_MPEG2\_PES             |
| MEDIATYPE\_Video               | KSDATAFORMAT\_TYPE\_VIDEO                  |



 

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dshow.h</dt> </dl> |



## See also

<dl> <dt>

[MPEG-2 Media Types](mpeg-2-media-types.md)
</dt> </dl>

 

 




