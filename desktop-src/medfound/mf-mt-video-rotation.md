---
description: Specifies the rotation of a video frame in the counter-clockwise direction.
ms.assetid: 7C0911A6-6D7C-4510-891F-A6F56CE1EC2B
title: MF_MT_VIDEO_ROTATION attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_VIDEO\_ROTATION attribute

Specifies the rotation of a video frame in the counter-clockwise direction.

## Data type

**MFVideoRotationFormat** stored as **UINT32**

## Remarks

Video from a handheld device, such as a mobile phone, is often rotated by 90, 180, or 270 degrees. If the camera stores the orientation as metadata in the video file, the image can be adjusted at the time of playback.

If this attribute set to **MFVideoRotationFormat\_90**, it means that the content has been rotated 90 degrees in the counter-clockwise direction. If the content was rotated 90 degrees in the clockwise direction, the attribute value would be **MFVideoRotationFormat\_270**.

The supported values for this attribute are enumerated in [**MFVideoRotationFormat**](/windows/desktop/api/mfapi/ne-mfapi-mfvideorotationformat).

The GUID constant for this attribute is exported from mfuuid.lib.

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

[Media Types](media-types.md)
</dt> </dl>

 

 




