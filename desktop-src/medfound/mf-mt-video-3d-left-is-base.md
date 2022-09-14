---
description: For a 3D video format, specifies which view is the base view.
ms.assetid: 11555BA0-D9BE-4239-A857-C9EEE86A8520
title: MF_MT_VIDEO_3D_LEFT_IS_BASE attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_VIDEO\_3D\_LEFT\_IS\_BASE attribute

For a 3D video format, specifies which view is the base view.

## Data type

**BOOL** stored as **UINT32**

## Remarks

By default, the left view in a 3D video sequence is the base view. If the right view is the base view, set this attribute to **FALSE**.

To convert stereoscopic video to 2D, keep the base view and discard the other view.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




