---
description: This property queries the decoder for the maximum full-frame rate that the decoder supports. The data type for this property is an AM\_QueryRate structure.
ms.assetid: 98808ed4-6d34-437b-9729-9cc805bc81f0
title: AM_RATE_QueryFullFrameRate Property (Dvdmedia.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AM\_RATE\_QueryFullFrameRate Property

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

 

 




