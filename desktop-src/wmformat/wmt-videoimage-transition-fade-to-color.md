---
title: WMT_VIDEOIMAGE_TRANSITION_FADE_TO_COLOR (Wmsdkidl.h)
description: The fade-to-color transition dissolves from the image to a frame of solid color.
ms.assetid: 4ec52682-1ca2-436d-b7ce-2a9d407ff50e
keywords:
- WMT_VIDEOIMAGE_TRANSITION_FADE_TO_COLOR windows Media Format
topic_type:
- apiref
api_name:
- WMT_VIDEOIMAGE_TRANSITION_FADE_TO_COLOR
api_location:
- wmsdkidl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMT\_VIDEOIMAGE\_TRANSITION\_FADE\_TO\_COLOR

The fade-to-color transition dissolves from the image to a frame of solid color.

## Parameters

The following table describes the parameters used by this transition and lists the members of the [**WMT\_VIDEOIMAGE\_SAMPLE2**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_videoimage_sample2) structure to which they are assigned.



| Parameter         | Structure member | Description                                                                                                                                                                                                               |
|-------------------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Red               | **fEffectPara0** | Red value of the background color. Set to a number between 0 and 255.                                                                                                                                                     |
| Green             | **fEffectPara1** | Green value of the background color. Set to a number between 0 and 255.                                                                                                                                                   |
| Blue              | **fEffectPara2** | Blue value of the background color. Set to a number between 0 and 255.                                                                                                                                                    |
| Background weight | **fEffectPara3** | Weight of the background color. This parameter expresses the percentage of the background color in the mix as a decimal. For example, to blend the background color at 30%, making the image 70% of the mix, set to 0.30. |



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmsdkidl.h</dt> </dl> |



## See also

<dl> <dt>

[**Video Image Transitions**](video-image-transitions.md)
</dt> </dl>

 

 





