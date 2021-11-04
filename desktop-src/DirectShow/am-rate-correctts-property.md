---
description: The DVD Navigator uses this property to inform the decoder that the Navigator is setting the correct time stamps on the samples it delivers to the decoder.
ms.assetid: f04e8291-734f-483e-b756-5362beb68d9c
title: AM_RATE_CorrectTS Property (Dvdmedia.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AM\_RATE\_CorrectTS Property

The DVD Navigator uses this property to inform the decoder that the Navigator is setting the correct time stamps on the samples it delivers to the decoder.



| Label | Value |
|-------------------|-------------------------------|
| Property Set GUID | AM\_KSPROPSETID\_TSRateChange |
| Property ID       | AM\_RATE\_CorrectTS           |
| Data Type         | **LONG**                      |



 

## Remarks

Earlier versions of the DVD Navigator did not set the correct time stamps when the playback rate was something other than 1.0. Many decoders work around this problem by ignoring the time stamps during rewind or fast forward, and estimating the correct presentation times.

These problems have been corrected in the current version of the DVD Navigator. For backward compatibility with existing decoders, the DVD Navigator indicates that the time stamps are correct by setting the AM\_RATE\_CorrectTS property on the decoder with the value **TRUE**. When this property is set, the decoder should use the actual time stamps, instead of estimating the presentation times.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dvdmedia.h</dt> </dl> |



## See also

<dl> <dt>

[**Rate Change Property Set**](rate-change-property-set.md)
</dt> </dl>

 

 




