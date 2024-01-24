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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WMT\_VIDEOIMAGE\_TRANSITION\_SPLIT

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





