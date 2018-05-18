---
Description: 'Specifies how a 3D video frame is stored in a media sample.'
ms.assetid: '1B996B22-C76B-47E5-8937-1E5E672E32EC'
title: 'MFSampleExtension\_3DVideo\_SampleFormat attribute'
---

# MFSampleExtension\_3DVideo\_SampleFormat attribute

Specifies how a 3D video frame is stored in a media sample.

## Data type

**UINT32**

## Remarks

The value of this attribute is a member of the [**MFVideo3DSampleFormat**](mfvideo3dsampleformat.md) enumeration.

A component that generates 3D video frames should set this attribute to **TRUE** on every media sample that contains a 3D frame. The attribute is ignored if the [MFSampleExtension\_3DVideo](mfsampleextension-3dvideo.md) attribute is **FALSE** or not set.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[MFSampleExtension\_3DVideo](mfsampleextension-3dvideo.md)
</dt> </dl>

 

 




