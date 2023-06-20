---
description: This property sends a command to the device to search for a specified time code. The UVC device driver supports this property.
ms.assetid: 0502d59a-0a9e-4192-af9f-1553cd13a69c
title: KSPROPERTY_EXTXPORT_TIMECODE_SEARCH
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# KSPROPERTY\_EXTXPORT\_TIMECODE\_SEARCH

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This property sends a command to the device to search for a specified time code. The UVC device driver supports this property.



| Label | Value |
|-------------------|----------------------------------------|
| Property Set GUID | PROPSETID\_EXT\_TRANSPORT              |
| Property ID       | KSPROPERTY\_EXTXPORT\_TIMECODE\_SEARCH |
| Data Type         | **KSPROPERTY\_EXTXPORT\_S** structure  |



 

## Remarks

Fill in the **Timecode** member of the **KSPROPERTY\_EXTXPORT\_S** structure with the desired frame, second, minute, and hour. The **KSPROPERTY\_EXTXPORT\_S** structure is described in the Windows DDK.

## See also

<dl> <dt>

[External Device Transport Property Set](external-device-transport-property-set.md)
</dt> </dl>

 

 



