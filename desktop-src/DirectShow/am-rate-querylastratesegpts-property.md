---
description: This property queries the decoder for the start time of the rate change that was queued most recently, regardless of its position in the rate-change queue.
ms.assetid: 3c7006e7-48fd-4df8-b446-8ee2b024278b
title: AM_RATE_QueryLastRateSegPTS Property (Dvdmedia.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AM\_RATE\_QueryLastRateSegPTS Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This property queries the decoder for the start time of the rate change that was queued most recently, regardless of its position in the rate-change queue.

This property is defined for version 1.1 of this property set; see [**AM\_RATE\_UseRateVersion**](am-rate-userateversion-property.md).



| Label | Value |
|-------------------|-------------------------------|
| Property Set GUID | AM\_KSPROPSETID\_TSRateChange |
| Property ID       | AM\_RATE\_QueryLastRateSegPTS |
| Data Type         | **REFERENCE\_TIME**           |



 

## Remarks

The source filter can use this property to synchronize rate changes across several audio and video streams.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dvdmedia.h</dt> </dl> |



## See also

<dl> <dt>

[**Rate Change Property Set**](rate-change-property-set.md)
</dt> </dl>

 

 




