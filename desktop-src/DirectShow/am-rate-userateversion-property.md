---
description: This property is used to signal which version of the Rate Change property set the decoder should use.
ms.assetid: 49d1bfda-749b-4614-9a75-1f76fa8b320d
title: AM_RATE_UseRateVersion Property (Dvdmedia.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AM\_RATE\_UseRateVersion Property

This property is used to signal which version of the Rate Change property set the decoder should use. The value is a **WORD** type. The high-order byte contains the minor version number, and the low-order byte contains the low-order byte. Thus, version 1.1 is signaled with the value 0x0101.

If the decoder does not support the specified version, it should fail the call to [**IKsPropertySet::Set**](ikspropertyset-set.md) and return E\_NOINTERFACE. If the source filter does not set the version, the decoder should default to version 1.0.



| Label | Value |
|-------------------|-------------------------------|
| Property Set GUID | AM\_KSPROPSETID\_TSRateChange |
| Property ID       | AM\_RATE\_UseRateVersion      |
| Data Type         | **WORD**                      |



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dvdmedia.h</dt> </dl> |



## See also

<dl> <dt>

[**Rate Change Property Set**](rate-change-property-set.md)
</dt> </dl>

 

 




