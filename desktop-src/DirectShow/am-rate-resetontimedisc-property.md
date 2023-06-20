---
description: AM_RATE_ResetOnTimeDisc Property - Applies to Windows Vista and later.
ms.assetid: 3e342219-341e-49a2-9f8f-4188dd7bf719
title: AM_RATE_ResetOnTimeDisc Property (Dvdmedia.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AM\_RATE\_ResetOnTimeDisc Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Applies to Windows Vista and later.

This property queries whether the decoder resynchronizes the output time stamps to the input time stamps when the decoder receives a sample with the discontinuity flag.

This property is read/write.



| Label | Value |
|-------------------|-------------------------------|
| Property Set GUID | AM\_KSPROPSETID\_TSRateChange |
| Property ID       | AM\_RATE\_ResetOnTimeDisc     |
| Data Type         | **DWORD**                     |



 

## Remarks

This property supports smooth rate changes. If the value of this property is **TRUE** and the decoder receives an input sample with the AM\_SAMPLE\_TIMEDISCONTINUITY flag, the decoded frame should have the same time stamp as the input frame.

To retrieve the AM\_SAMPLE\_TIMEDISCONTINUITY flag, call [**IMediaSample2::GetProperties**](/windows/desktop/api/Strmif/nf-strmif-imediasample2-getproperties) on the sample. The flag is set in the **dwSampleFlags** member of the [**AM\_SAMPLE2\_PROPERTIES**](/windows/win32/api/strmif/ns-strmif-am_sample2_properties) structure.

For more information, see [DVD Playback Enhancements in Windows Vista](dvd-playback-enhancements-in-windows-vista.md).

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dvdmedia.h</dt> </dl> |



## See also

<dl> <dt>

[**Rate Change Property Set**](rate-change-property-set.md)
</dt> </dl>

 

 




