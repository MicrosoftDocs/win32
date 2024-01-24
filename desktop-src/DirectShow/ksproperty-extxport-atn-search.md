---
description: This property sends a command to the device to search for an absolute track number (ATN). The UVC device driver supports this property.
ms.assetid: 209e0aa3-d7a3-4b5c-ae5a-5063a3804a9d
title: KSPROPERTY_EXTXPORT_ATN_SEARCH
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# KSPROPERTY\_EXTXPORT\_ATN\_SEARCH

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This property sends a command to the device to search for an absolute track number (ATN). The UVC device driver supports this property.



| Label | Value |
|-------------------|---------------------------------------|
| Property Set GUID | PROPSETID\_EXT\_TRANSPORT             |
| Property ID       | KSPROPERTY\_EXTXPORT\_ATN\_SEARCH     |
| Data Type         | **KSPROPERTY\_EXTXPORT\_S** structure |



 

## Remarks

Set the **dwAbsTrackNumber** member of the **KSPROPERTY\_EXTXPORT\_S** structure to the following value:


```
(absolute track number << 1) + continuity bit
```



The UVC specification does not define how the device uses the continuity bit. The **KSPROPERTY\_EXTXPORT\_S** structure is described in the Windows DDK.

## See also

<dl> <dt>

[External Device Transport Property Set](external-device-transport-property-set.md)
</dt> </dl>

 

 



