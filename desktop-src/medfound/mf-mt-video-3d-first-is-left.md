---
description: For a 3D video format, specifies which view is the left view.
ms.assetid: 4F33BF2D-EB32-46B6-B071-F9130D404201
title: MF_MT_VIDEO_3D_FIRST_IS_LEFT attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_VIDEO\_3D\_FIRST\_IS\_LEFT attribute

For a 3D video format, specifies which view is the left view.

## Data type

**BOOL** stored as **UINT32**

## Remarks

For 3D video, each video sample contains two views, which are designated *first view* and *second view*. The exact layout of the views in memory is indicated by the [MF\_MT\_VIDEO\_3D\_FORMAT](mf-mt-video-3d-format.md) attribute.



| Format               | First View              | Second View               |
|----------------------|-------------------------|---------------------------|
| Packed side-by-side  | Left half of the buffer | Right half of the buffer  |
| Packed top-to-bottom | Top half of the buffer  | Bottom half of the buffer |
| Multiview            | Buffer index 0          | Buffer index 1            |
| Base view            | Entire frame            | Not present               |



 

By default, the first view is the left view, and the second view is the right view. If the left and right views are swapped, set the MF\_MT\_VIDEO\_3D\_FIRST\_IS\_LEFT attribute to **FALSE** in the media type.

> [!Note]  
> In *base view* format (**MFVideo3DSampleFormat\_BaseView**), only the base view is retained, so this attribute does not apply.

 

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

 

 




