---
title: WMT_VIDEOIMAGE_TRANSITION_INSET (Wmsdkidl.h)
description: The inset transition reveals the new image in a rectangle originating from one corner of the frame.
ms.assetid: fd8bc4b7-0546-4897-ab7b-a320bbd126ef
keywords:
- WMT_VIDEOIMAGE_TRANSITION_INSET windows Media Format
topic_type:
- apiref
api_name:
- WMT_VIDEOIMAGE_TRANSITION_INSET
api_location:
- wmsdkidl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMT\_VIDEOIMAGE\_TRANSITION\_INSET

The inset transition reveals the new image in a rectangle originating from one corner of the frame.

## Parameters

The following table describes the parameters used by this transition and lists the members of the [**WMT\_VIDEOIMAGE\_SAMPLE2**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_videoimage_sample2) structure to which they are assigned.




| Parameter | Structure member | Description | 
|-----------|------------------|-------------|
| Width | <strong>fEffectPara0</strong> | Width of the inset in pixels. | 
| Height | <strong>fEffectPara1</strong> | Height of the inset in pixels. | 
| Direction | <strong>fEffectPara2</strong> | Corner from which the inset originates.Set to one of the following values:<br /><ul><li>0 - Lower left</li><li>1 - Lower right</li><li>2 - Upper left</li><li>3 - Upper right</li></ul> | 
| Composition | <strong>fEffectPara3</strong> | Set to one of the following values:<ul><li>0 - Specifies normal composition, in which the previous image is the background, and the current image is the foreground.</li><li>1 - Specifies reversed composition, in which the current image is the background image, and the previous image is the foreground</li></ul> | 




 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmsdkidl.h</dt> </dl> |



## See also

<dl> <dt>

[**Video Image Transitions**](video-image-transitions.md)
</dt> </dl>

 

 





