---
description: This property queries the decoder for the maximum full-frame rate that the decoder supports. The data type for this property is an AM\_QueryRate structure.
ms.assetid: 98808ed4-6d34-437b-9729-9cc805bc81f0
title: AM_RATE_QueryFullFrameRate Property (Dvdmedia.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AM\_RATE\_QueryFullFrameRate Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This property queries the decoder for the maximum full-frame rate that the decoder supports. The data type for this property is an **AM\_QueryRate** structure.

This property is defined for version 1.1 of this property set; see [**AM\_RATE\_UseRateVersion**](am-rate-userateversion-property.md).



| Label | Value |
|-------------------|---------------------------------------|
| Property Set GUID | AM\_KSPROPSETID\_TSRateChange         |
| Property ID       | AM\_RATE\_QueryFullFrameRate Property |
| Data Type         | [**AM\_QueryRate**](/previous-versions/windows/desktop/api/Dvdmedia/ns-dvdmedia-am_queryrate) |



 

## Remarks

If the playback rate exceeds the decoder's maximum rate, the source filter sends groups of continuous samples separated by discontinuities. The time stamps jump across the discontinuities. The source filter might do this even if the playback rate is within the decoder's maximum rate, because there may be other factors, such as disk IO, that limit the full playback rate.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dvdmedia.h</dt> </dl> |



## See also

<dl> <dt>

[**Rate Change Property Set**](rate-change-property-set.md)
</dt> </dl>

 

 




