---
description: Queries whether the video output is standard-definition, analog component video.
ms.assetid: bd4fc5bc-c45d-4228-9759-6300fdfff6a0
title: AM_PROPERTY_COPY_ANALOG_COMPONENT Property (Dvdmedia.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AM\_PROPERTY\_COPY\_ANALOG\_COMPONENT Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Queries whether the video output is standard-definition, analog component video.



| Label | Value |
|-------------------|---------------------------------------|
| Property Set GUID | AM\_KSPROPSETID\_CopyProt             |
| Property ID       | AM\_PROPERTY\_COPY\_ANALOG\_COMPONENT |
| Data Type         | **ULONG**                             |



 

## Remarks

This property is read-only.

The value of the property is **TRUE** if the video output is analog component video with a resolution not greater than 480p for NTSC or 540p for PAL. Otherwise, the value is **FALSE**.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dvdmedia.h</dt> </dl> |



## See also

<dl> <dt>

[**DVD Copy Protection Property Set**](dvd-copy-protection-property-set.md)
</dt> </dl>

 

 




