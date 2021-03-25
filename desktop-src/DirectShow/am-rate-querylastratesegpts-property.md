---
description: This property queries the decoder for the start time of the rate change that was queued most recently, regardless of its position in the rate-change queue.
ms.assetid: 3c7006e7-48fd-4df8-b446-8ee2b024278b
title: AM_RATE_QueryLastRateSegPTS Property (Dvdmedia.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AM\_RATE\_QueryLastRateSegPTS Property

This property queries the decoder for the start time of the rate change that was queued most recently, regardless of its position in the rate-change queue.

This property is defined for version 1.1 of this property set; see [**AM\_RATE\_UseRateVersion**](am-rate-userateversion-property.md).



|                   |                               |
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

 

 




