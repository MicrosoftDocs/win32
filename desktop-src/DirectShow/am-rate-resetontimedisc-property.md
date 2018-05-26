---
Description: Applies to Windows Vista and later.
ms.assetid: 3e342219-341e-49a2-9f8f-4188dd7bf719
title: AM\_RATE\_ResetOnTimeDisc Property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AM\_RATE\_ResetOnTimeDisc Property

Applies to Windows Vista and later.

This property queries whether the decoder resynchronizes the output time stamps to the input time stamps when the decoder receives a sample with the discontinuity flag.

This property is read/write.



|                   |                               |
|-------------------|-------------------------------|
| Property Set GUID | AM\_KSPROPSETID\_TSRateChange |
| Property ID       | AM\_RATE\_ResetOnTimeDisc     |
| Data Type         | **DWORD**                     |



 

## Remarks

This property supports smooth rate changes. If the value of this property is **TRUE** and the decoder receives an input sample with the AM\_SAMPLE\_TIMEDISCONTINUITY flag, the decoded frame should have the same time stamp as the input frame.

To retrieve the AM\_SAMPLE\_TIMEDISCONTINUITY flag, call [**IMediaSample2::GetProperties**](/windows/win32/Strmif/nf-strmif-imediasample2-getproperties?branch=master) on the sample. The flag is set in the **dwSampleFlags** member of the [**AM\_SAMPLE2\_PROPERTIES**](/windows/win32/strmif/ns-strmif-tagam_sample2_properties?branch=master) structure.

For more information, see [DVD Playback Enhancements in Windows Vista](dvd-playback-enhancements-in-windows-vista.md).

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dvdmedia.h</dt> </dl> |



## See also

<dl> <dt>

[**Rate Change Property Set**](rate-change-property-set.md)
</dt> </dl>

 

 




