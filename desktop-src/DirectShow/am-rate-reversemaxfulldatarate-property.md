---
description: AM_RATE_ReverseMaxFullDataRate Property - Applies to Windows Vista and later.
ms.assetid: 4f170736-516d-4420-a215-e0e414f036cd
title: AM_RATE_ReverseMaxFullDataRate Property (Dvdmedia.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AM\_RATE\_ReverseMaxFullDataRate Property

Applies to Windows Vista and later.

Returns the decoder's maximum reverse playback rate. The value of the property is the absolute value of the maximum reverse speed x 10000. For example, if the maximum reverse speed is -2.0, the value of this property is 20000.

The data type for this property is **AM\_MaxFullDataRate**, which is a `typedef` for **LONG**.

This property is read-only.



| Label | Value |
|-------------------|----------------------------------|
| Property Set GUID | AM\_KSPROPSETID\_TSRateChange    |
| Property ID       | AM\_RATE\_ReverseMaxFullDataRate |
| Data Type         | **AM\_MaxFullDataRate**          |



 

## Remarks

Decoders that support smooth reverse playback should expose this property. For more information, see [DVD Playback Enhancements in Windows Vista](dvd-playback-enhancements-in-windows-vista.md).

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dvdmedia.h</dt> </dl> |



## See also

<dl> <dt>

[**Rate Change Property Set**](rate-change-property-set.md)
</dt> </dl>

 

 




