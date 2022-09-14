---
title: WMT_VIDEOIMAGE_TRANSITION_WHEEL (Wmsdkidl.h)
description: The wheel transition reveals the new image by rotating four lines around a common pivot point, like the spokes of a wheel.
ms.assetid: 426217be-789b-4b78-b0ea-de9629ecd46c
keywords:
- WMT_VIDEOIMAGE_TRANSITION_WHEEL windows Media Format
topic_type:
- apiref
api_name:
- WMT_VIDEOIMAGE_TRANSITION_WHEEL
api_location:
- wmsdkidl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMT\_VIDEOIMAGE\_TRANSITION\_WHEEL

The wheel transition reveals the new image by rotating four lines around a common pivot point, like the spokes of a wheel.

## Parameters

The following table describes the parameters used by this transition and lists the members of the [**WMT\_VIDEOIMAGE\_SAMPLE2**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_videoimage_sample2) structure to which they are assigned.




| Parameter | Structure member | Description | 
|-----------|------------------|-------------|
| Center X | <strong>fEffectPara0</strong> | X-coordinate, relative to the video frame, of the center of the wheel effect. | 
| Center Y | <strong>fEffectPara1</strong> | Y-coordinate, relative to the video frame, of the center of the wheel effect. | 
| Angle | <strong>fEffectPara2</strong> | Angle of rotation, in degrees, of the spokes of the wheel effect. A value of 0.0 indicates the old image without any of the new image revealed. A value of 90.0 indicates the new image fully revealed.Movement from 0.0 to 90.0 appears as clockwise rotation of the spokes.<br /> | 
| Composition | <strong>fEffectPara3</strong> | Set to one of the following values:<ul><li>0 - Specifies normal composition, in which the previous image is the background, and the current image is the foreground.</li><li>1 - Specifies reversed composition, in which the current image is the background image, and the previous image is the foreground</li></ul> | 




 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmsdkidl.h</dt> </dl> |



## See also

<dl> <dt>

[**Video Image Transitions**](video-image-transitions.md)
</dt> </dl>

 

 





