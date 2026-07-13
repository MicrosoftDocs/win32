---
description: This property is used to send rate changes to the decoder. The data type for this property is an AM\_SimpleRateChange structure, which gives the new playback rate and the presentation time when the new rate takes effect.
ms.assetid: d6ade463-82c7-46be-8d9a-e372ddbd7a4b
title: AM_RATE_SimpleRateChange Property (Dvdmedia.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AM\_RATE\_SimpleRateChange Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This property is used to send rate changes to the decoder. The data type for this property is an **AM\_SimpleRateChange** structure, which gives the new playback rate and the presentation time when the new rate takes effect.



| Label | Value |
|-------------------|-----------------------------------------------------|
| Property Set GUID | AM\_KSPROPSETID\_TSRateChange                       |
| Property ID       | AM\_RATE\_SimpleRateChange                          |
| Data Type         | [**AM\_SimpleRateChange**](/previous-versions/windows/desktop/api/Dvdmedia/ns-dvdmedia-am_simpleratechange) |



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dvdmedia.h</dt> </dl> |



## See also

<dl> <dt>

[**Rate Change Property Set**](rate-change-property-set.md)
</dt> </dl>

 

 




