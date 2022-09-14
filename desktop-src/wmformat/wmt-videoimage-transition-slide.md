---
title: WMT_VIDEOIMAGE_TRANSITION_SLIDE (Wmsdkidl.h)
description: The slide transition reveals the new image by sliding the old image out of the frame.
ms.assetid: 925bcf92-5608-48ca-9bdc-dd08bcd8b8d5
keywords:
- WMT_VIDEOIMAGE_TRANSITION_SLIDE windows Media Format
topic_type:
- apiref
api_name:
- WMT_VIDEOIMAGE_TRANSITION_SLIDE
api_location:
- wmsdkidl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMT\_VIDEOIMAGE\_TRANSITION\_SLIDE

The slide transition reveals the new image by sliding the old image out of the frame.

## Parameters

The following table describes the parameters used by this transition and lists the members of the [**WMT\_VIDEOIMAGE\_SAMPLE2**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_videoimage_sample2) structure to which they are assigned.




| Parameter | Structure member | Description | 
|-----------|------------------|-------------|
| Distance | <strong>fEffectPara0</strong> | Distance, in pixels, that the old image slides out of the frame. | 
| Direction | <strong>fEffectPara1</strong> | Direction in which the old image slides.Set to one of the following values:<br /><ul><li>0 - Slide to the right.</li><li>1 - Slide to the left.</li><li>2 - Slide upward.</li><li>3 - Slide downward.</li></ul> | 
| Composition | <strong>fEffectPara2</strong> | Set to one of the following values:<ul><li>0 - Specifies normal composition, in which the previous image is the background, and the current image is the foreground.</li><li>1 - Specifies reversed composition, in which the current image is the background image, and the previous image is the foreground</li></ul> | 




 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmsdkidl.h</dt> </dl> |



## See also

<dl> <dt>

[**Video Image Transitions**](video-image-transitions.md)
</dt> </dl>

 

 





