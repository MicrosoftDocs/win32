---
description: Specifies whether a media sample contains a 3D video frame.
ms.assetid: 1B0B9DBD-80EB-4876-B2F2-BE419AC84265
title: MFSampleExtension_3DVideo attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFSampleExtension\_3DVideo attribute

Specifies whether a media sample contains a 3D video frame.

## Data type

**BOOL** stored as **UINT32**

## Remarks

If this attribute is **TRUE**, the media sample contains a video frame that has two or more stereoscopic views. The default value is **FALSE**.

A component that generates 3D video frames should set this attribute to **TRUE** on every media sample that contains a 3D frame.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[MFSampleExtension\_3DVideo\_SampleFormat](mfsampleextension-3dvideo-sampleformat.md)
</dt> </dl>

 

 




