---
title: WMT_VIDEOIMAGE_TRANSITION_FLIP (Wmsdkidl.h)
description: The flip transition rotates the old image on a y-axis through the center of the frame. The new image is revealed as the back of the old image.
ms.assetid: ff9990ef-962c-4dbb-b2bc-3bee070d2044
keywords:
- WMT_VIDEOIMAGE_TRANSITION_FLIP windows Media Format
topic_type:
- apiref
api_name:
- WMT_VIDEOIMAGE_TRANSITION_FLIP
api_location:
- wmsdkidl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMT\_VIDEOIMAGE\_TRANSITION\_FLIP

The flip transition rotates the old image on a y-axis through the center of the frame. The new image is revealed as the back of the old image.

## Parameters

The following table describes the parameters used by this transition and lists the members of the [**WMT\_VIDEOIMAGE\_SAMPLE2**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_videoimage_sample2) structure to which they are assigned.




| Parameter | Structure member | Description | 
|-----------|------------------|-------------|
| Angle | <strong>fEffectPara0</strong> | Angle of the rotation, from 0.0 to 180.0 degrees. | 
| Composition | <strong>fEffectPara1</strong> | Set to one of the following values:<ul><li>0 - Specifies normal composition, in which the previous image is the background, and the current image is the foreground.</li><li>1 - Specifies reversed composition, in which the current image is the background image, and the previous image is the foreground</li></ul> | 




 

## Remarks

You can visualize the effect of this transition as if both images were physical photographs glued together back-to-back. The transition has the same effect as holding two such photographs at the center of the bottom edge and rotating them 180 degrees.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmsdkidl.h</dt> </dl> |



## See also

<dl> <dt>

[**Video Image Transitions**](video-image-transitions.md)
</dt> </dl>

 

 





