---
description: AM_RATE_ReverseMaxFullDataRate Property - Applies to Windows Vista and later.
ms.assetid: 4f170736-516d-4420-a215-e0e414f036cd
title: AM_RATE_ReverseMaxFullDataRate Property (Dvdmedia.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AM\_RATE\_ReverseMaxFullDataRate Property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




