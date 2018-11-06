---
title: WMT_VIDEOIMAGE_TRANSITION_CROSS_FADE
description: The cross-fade transition has no special effect; the characteristics of the fade (dissolve) are determined by the fPrevBlendCoef and fCurrBlendCoef members of the WMT\_VIDEOIMAGE\_SAMPLE2 structure.
ms.assetid: 254c4552-ce49-4f44-86e3-ee7d30c83000
keywords:
- WMT_VIDEOIMAGE_TRANSITION_CROSS_FADE windows Media Format
topic_type:
- apiref
api_name:
- WMT_VIDEOIMAGE_TRANSITION_CROSS_FADE
api_location:
- wmsdkidl.h
api_type:
- HeaderDef
ms.topic: article
ms.date: 05/31/2018
---

# WMT\_VIDEOIMAGE\_TRANSITION\_CROSS\_FADE

The cross-fade transition has no special effect; the characteristics of the fade (dissolve) are determined by the **fPrevBlendCoef** and **fCurrBlendCoef** members of the [**WMT\_VIDEOIMAGE\_SAMPLE2**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-__wmt_videoimage_sample2) structure.

## Parameters

This transition takes no parameters.

## Remarks

Setting this transition is the same as setting the **dwEffectType** member of the **WMT\_VIDEOIMAGE\_SAMPLE2** structure to 0.

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmsdkidl.h</dt> </dl> |



## See also

<dl> <dt>

[**Video Image Transitions**](video-image-transitions.md)
</dt> </dl>

 

 





