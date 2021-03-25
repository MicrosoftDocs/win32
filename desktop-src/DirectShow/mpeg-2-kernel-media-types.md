---
description: For several MPEG-2 media type GUIDs, the Windows DDK defines names that differ from the names used in DirectShow. The following table shows the DirectShow names (defined in Ksuuids.h) and the corresponding kernel-mode names (defined in Ksmedia.h).
ms.assetid: ecf94552-5a0f-464c-9f9b-4861faa38d05
title: MPEG-2 Kernel Media Types (Dshow.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MPEG-2 Kernel Media Types

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

 

 




