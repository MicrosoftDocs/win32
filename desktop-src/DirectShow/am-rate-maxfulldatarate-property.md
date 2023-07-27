---
description: Returns the maximum rate at which a decoder can process data. The value of this property is the decoder's maximum playback speed x 10000. For example, if the maximum forward speed is 2.0, the value of this property is 20000.
ms.assetid: 66e6885b-7ad7-4912-85e4-ea36855bfde6
title: AM_RATE_MaxFullDataRate Property (Dvdmedia.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AM\_RATE\_MaxFullDataRate Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Returns the maximum rate at which a decoder can process data. The value of this property is the decoder's maximum playback speed x 10000. For example, if the maximum forward speed is 2.0, the value of this property is 20000.

The data type for this property is **AM\_MaxFullDataRate**, which is a `typedef` for **LONG**.

This property is read-only.



| Label | Value |
|-------------------|------------------------------------|
| Property Set GUID | AM\_KSPROPSETID\_TSRateChange      |
| Property ID       | AM\_RATE\_MaxFullDataRate          |
| Data Type         | **AM\_MaxFullDataRate** (**LONG**) |



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dvdmedia.h</dt> </dl> |



## See also

<dl> <dt>

[**Rate Change Property Set**](rate-change-property-set.md)
</dt> </dl>

 

 




