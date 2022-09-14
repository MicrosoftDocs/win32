---
title: WMT_VIDEOIMAGE_TRANSITION_SPLIT (Wmsdkidl.h)
description: The split transition reveals the new image by splitting the old image. The split appears along a straight horizontal or vertical line starting inside the frame.
ms.assetid: ad777bfb-29a7-441f-8399-e462639450eb
keywords:
- WMT_VIDEOIMAGE_TRANSITION_SPLIT windows Media Format
topic_type:
- apiref
api_name:
- WMT_VIDEOIMAGE_TRANSITION_SPLIT
api_location:
- wmsdkidl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMT\_VIDEOIMAGE\_TRANSITION\_SPLIT

The split transition reveals the new image by splitting the old image. The split appears along a straight horizontal or vertical line starting inside the frame.

## Parameters

The following table describes the parameters used by this transition and lists the members of the [**WMT\_VIDEOIMAGE\_SAMPLE2**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_videoimage_sample2) structure to which they are assigned.




| Parameter | Structure member | Description | 
|-----------|------------------|-------------|
| Center X | <strong>fEffectPara0</strong> | X-coordinate, relative to the video frame, of the origin line of the split. | 
| Center Y | <strong>fEffectPara1</strong> | Y-coordinate, relative to the video frame, of the origin line of the split. | 
| Distance | <strong>fEffectPara2</strong> | Width of the split in pixels. | 
| Direction | <strong>fEffectPara3</strong> | Orientation of the split.Set to one of the following values:<br /><ul><li>0 - Splits along a horizontal line.</li><li>1 - Splits along a vertical line.</li></ul> | 
| Composition | <strong>fEffectPara4</strong> | Set to one of the following values:<ul><li>0 - Specifies normal composition, in which the previous image is the background, and the current image is the foreground.</li><li>1 - Specifies reversed composition, in which the current image is the background image, and the previous image is the foreground</li></ul> | 




 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmsdkidl.h</dt> </dl> |



## See also

<dl> <dt>

[**Video Image Transitions**](video-image-transitions.md)
</dt> </dl>

 

 





