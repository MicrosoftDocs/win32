---
description: A number of subtypes are defined for DV video. Each has a FOURCC code and a corresponding GUID value. Not all of these formats are supported; see the Remarks section for more information.
ms.assetid: d8390bd4-0339-4955-992c-92b8c9f6bf88
title: DV Video Subtypes (Dshow.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DV Video Subtypes

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A number of subtypes are defined for DV video. Each has a FOURCC code and a corresponding GUID value. Not all of these formats are supported; see the Remarks section for more information.

## Consumer Formats



| FOURCC | GUID               | Data Rate | Description                  |
|--------|--------------------|-----------|------------------------------|
| 'dvsl' | MEDIASUBTYPE\_dvsl | 12.5 Mbps | SD-DVCR (525-60 or 625-50)   |
| 'dvsd' | MEDIASUBTYPE\_dvsd | 25 Mbps   | SDL-DVCR (525-60 or 625-50)  |
| 'dvhd' | MEDIASUBTYPE\_dvhd | 50 Mbps   | HD-DVCR (1125-60 or 1250-50) |



 

Refer to IEC-61834 for more information about these formats.

## Professional Formats



| FOURCC | GUID               | Data Rate | Description                                 |
|--------|--------------------|-----------|---------------------------------------------|
| 'dv25' | MEDIASUBTYPE\_dv25 | 25 Mbps   | DVCPRO 25 (525-60 or 625-50).               |
| 'dv50' | MEDIASUBTYPE\_dv50 | 50 Mbps   | DVCPRO 50 (525-60 or 625-50)                |
| 'dvh1' | MEDIASUBTYPE\_dvh1 | 100 Mbps  | DVCPRO 100 (1080/60i, 1080/50i, or 720/60P) |



 

Refer to SMPTE 314M for more information about dv25 and dv50, and SMPTE 370M for more information about dvh1.

## Miscellaneous

Two additional DV subtypes are defined in the header file Uuids.h. These correspond to FOURCC codes that are produced by certain DV codecs; they do not correspond to any defined DV standards. These subtypes are obsolete and should not be used.



| FOURCC | GUID               |
|--------|--------------------|
| 'DVCS' | MEDIASUBTYPE\_DVCS |
| 'DVSD' | MEDIASUBTYPE\_DVSD |



 

## Remarks

The following table shows the supported data rates, in megabits per second (Mbps), for the MSDV and UVC drivers.



| Operating System                                                                 | MSDV (IEEE 1394) Driver | UVC Driver    |
|----------------------------------------------------------------------------------|-------------------------|---------------|
| Windows XP Service Pack 1 or earlier                                             | 12.5, 25                | Not available |
| Windows XP Service Pack 2 or later, Windows Server 2003 Service Pack 1 or later. | 12.5, 25, 50, 100       | 12.5, 25      |



 

For 25-Mbps streams, the behavior of the MSDV driver has changed in Windows Vista Prior to Windows Vista, the MSDV driver always set the media type to MEDIASUBTYPE\_dvsd for 25-Mbps streams, regardless of whether the source was SDL-DVCR or DVCPRO 25. The 'dv25' media type was not used. Starting with Windows Vista, the MSDV driver now distinguishes between these two formats. For SDL-DVCR, it continues to use the 'dvsd' subtype. For DVCPRO 25, it now uses the 'dv25' subtype.

The DirectShow [DV Splitter](dv-splitter-filter.md) and [DV Video Decoder](dv-video-decoder-filter.md) filters support SDL-DVCR formats only. The data can be PAL or NTSC. Third-party filters or codecs may be available that can parse other DV formats, as long as the data rate is supported by the MSDV or UVC driver.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dshow.h</dt> </dl> |



## See also

<dl> <dt>

[Digital Video in DirectShow](digital-video-in-directshow.md)
</dt> <dt>

[MSDV Driver](msdv-driver.md)
</dt> <dt>

[Video Subtypes](video-subtypes.md)
</dt> </dl>

 

 




