---
description: The following subtypes are defined for MEDIATYPE\_VBI.
ms.assetid: 31ea89c5-fb09-48ae-878f-724a2cbd4772
title: VBI Media Types (Uuids.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VBI Media Types

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following subtypes are defined for **MEDIATYPE\_VBI**.



| GUID                                                                                                                                                                                               | Description                                     |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------|
| <span id="KSDATAFORMAT_SUBTYPE_RAW8"></span><span id="ksdataformat_subtype_raw8"></span><dl> <dt>**KSDATAFORMAT\_SUBTYPE\_RAW8**</dt> </dl> | Raw VBI data.<br/>                        |
| <span id="MEDIASUBTYPE_TELETEXT"></span><span id="mediasubtype_teletext"></span><dl> <dt>**MEDIASUBTYPE\_TELETEXT**</dt> </dl>              | Teletext data.<br/>                       |
| <span id="MEDIASUBTYPE_VPS"></span><span id="mediasubtype_vps"></span><dl> <dt>**MEDIASUBTYPE\_VPS**</dt> </dl>                             | Video Programming System (VPS) data.<br/> |
| <span id="MEDIASUBTYPE_WSS"></span><span id="mediasubtype_wss"></span><dl> <dt>**MEDIASUBTYPE\_WSS**</dt> </dl>                             | Wide Screen Signaling (WSS) data.<br/>    |



## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Uuids.h</dt> </dl> |



## See also

<dl> <dt>

[**Line 21 Media Types**](line-21-media-types.md)
</dt> <dt>

[Media Types](media-types.md)
</dt> </dl>

 

 




