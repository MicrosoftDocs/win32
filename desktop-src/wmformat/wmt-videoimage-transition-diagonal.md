---
title: WMT_VIDEOIMAGE_TRANSITION_DIAGONAL (Wmsdkidl.h)
description: The diagonal transition reveals the new image along a diagonal line originating in one corner of the frame.
ms.assetid: 1aaaf9e8-bbb8-4289-948e-5d352798e831
keywords:
- WMT_VIDEOIMAGE_TRANSITION_DIAGONAL windows Media Format
topic_type:
- apiref
api_name:
- WMT_VIDEOIMAGE_TRANSITION_DIAGONAL
api_location:
- wmsdkidl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMT\_VIDEOIMAGE\_TRANSITION\_DIAGONAL

The diagonal transition reveals the new image along a diagonal line originating in one corner of the frame.

## Parameters

The following table describes the parameters used by this transition and lists the members of the [**WMT\_VIDEOIMAGE\_SAMPLE2**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_videoimage_sample2) structure to which they are assigned.




| Parameter | Structure member | Description | 
|-----------|------------------|-------------|
| Width | <strong>fEffectPara0</strong> | Width of the diagonal section in pixels. | 
| Height | <strong>fEffectPara1</strong> | Height of the diagonal section in pixels. | 
| Direction | <strong>fEffectPara2</strong> | Determines the corner from which the transition originates.Set to one of the following:<br /><ul><li>0 - Upper right</li><li>1 - Upper left</li><li>2 - Lower right</li><li>3 - Lower left</li></ul> | 
| Composition | <strong>fEffectPara3</strong> | Set to one of the following values:<ul><li>0 - Specifies normal composition, in which the previous image is the background, and the current image is the foreground.</li><li>1 - Specifies reversed composition, in which the current image is the background image, and the previous image is the foreground.</li></ul> | 




 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmsdkidl.h</dt> </dl> |



## See also

<dl> <dt>

[**Video Image Transitions**](video-image-transitions.md)
</dt> </dl>

 

 





