---
description: Specifies whether Windows Camera Effects are enabled for a capture device.
title: MF_DEVSOURCE_ATTRIBUTE_ENABLE_MS_CAMERA_EFFECTS attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/09/2022
---

# MF\_DEVSOURCE\_ATTRIBUTE\_ENABLE\_MS\_CAMERA\_EFFECTS attribute

Specifies whether Windows Camera Effects are enabled for a capture device.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Remarks

This attribute should be set during camera creation. If the value is non-zero, Windows Camera Effects are enabled.

The following requirements must be met before this feature can be enabled:
- An NPU based Video Effects Accelerator is available on the system.
- A camera producing streams consumable by the NPU is available on the system.
- The camera for which effects are being enabled is front-facing.

If any of these requirements are not met, then the specified attribute value is ignored and Windows Camera Effects are not enabled for the camera.



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11<br/>                                         |
| Minimum supported server<br/> | Windows Server<br/>                            |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Audio/Video Capture](audio-video-capture.md)
</dt> <dt>

[Capture Device Attributes](capture-device-attributes.md)
</dt> </dl>

 

 




