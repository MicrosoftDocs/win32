---
title: WMT_VIDEOIMAGE_TRANSITION_CROSS_FADE (Wmsdkidl.h)
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
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WMT\_VIDEOIMAGE\_TRANSITION\_CROSS\_FADE

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The cross-fade transition has no special effect; the characteristics of the fade (dissolve) are determined by the **fPrevBlendCoef** and **fCurrBlendCoef** members of the [**WMT\_VIDEOIMAGE\_SAMPLE2**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_videoimage_sample2) structure.

## Parameters

This transition takes no parameters.

## Remarks

Setting this transition is the same as setting the **dwEffectType** member of the **WMT\_VIDEOIMAGE\_SAMPLE2** structure to 0.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmsdkidl.h</dt> </dl> |



## See also

<dl> <dt>

[**Video Image Transitions**](video-image-transitions.md)
</dt> </dl>

 

 





