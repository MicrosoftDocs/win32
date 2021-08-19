---
title: WMT_VIDEOIMAGE_TRANSITION_PAGE_ROLL (Wmsdkidl.h)
description: The page roll transition transforms the old image with a page-flipping effect, revealing the new image underneath.
ms.assetid: 50efa4e9-0d3a-4b85-96b0-6d5cd637ca98
keywords:
- WMT_VIDEOIMAGE_TRANSITION_PAGE_ROLL windows Media Format
topic_type:
- apiref
api_name:
- WMT_VIDEOIMAGE_TRANSITION_PAGE_ROLL
api_location:
- wmsdkidl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMT\_VIDEOIMAGE\_TRANSITION\_PAGE\_ROLL

The page roll transition transforms the old image with a page-flipping effect, revealing the new image underneath.

## Parameters

The following table describes the parameters used by this transition and lists the members of the [**WMT\_VIDEOIMAGE\_SAMPLE2**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_videoimage_sample2) structure to which they are assigned.




| Parameter | Structure member | Description | 
|-----------|------------------|-------------|
| Radius | <strong>fEffectPara0</strong> | Radius of the roll in the page roll effect. | 
| Distance | <strong>fEffectPara1</strong> | Amount of the new image that is revealed by the page roll effect, in pixels. | 
| Direction | <strong>fEffectPara2</strong> | Corner or side of the video frame, from which the page roll originates.Set to one of the following values:<br /><ul><li>0 - Left side</li><li>1 - Right side</li><li>2 - Bottom</li><li>3 - Top</li><li>4 - Bottom left corner</li><li>5 - Bottom right corner</li><li>6 - Upper left corner</li><li>7 - Upper right corner</li></ul> | 
| Composition | <strong>fEffectPara3</strong> | Set to one of the following values:<ul><li>0 - Specifies normal composition, in which the previous image is the background, and the current image is the foreground.</li><li>1 - Specifies reversed composition, in which the current image is the background image, and the previous image is the foreground</li></ul> | 




 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmsdkidl.h</dt> </dl> |



## See also

<dl> <dt>

[**Video Image Transitions**](video-image-transitions.md)
</dt> </dl>

 

 





