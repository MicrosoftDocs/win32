---
title: WMT_VIDEOIMAGE_TRANSITION_BOW_TIE (Wmsdkidl.h)
description: The bow tie transition reveals the new image in a set of triangles on opposite sides of the frame.
ms.assetid: d98da767-eea7-460c-ae5f-6bef9d93ad9d
keywords:
- WMT_VIDEOIMAGE_TRANSITION_BOW_TIE windows Media Format
topic_type:
- apiref
api_name:
- WMT_VIDEOIMAGE_TRANSITION_BOW_TIE
api_location:
- wmsdkidl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WMT\_VIDEOIMAGE\_TRANSITION\_BOW\_TIE

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The bow tie transition reveals the new image in a set of triangles on opposite sides of the frame.

## Parameters

The following table describes the parameters used by this transition and lists the members of the [**WMT\_VIDEOIMAGE\_SAMPLE2**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_videoimage_sample2) structure to which they are assigned.




| Parameter | Structure member | Description | 
|-----------|------------------|-------------|
| Width | <strong>fEffectPara0</strong> | Width of each triangular side of the bow tie. | 
| Height | <strong>fEffectPara1</strong> | Height of each triangular side of the bow tie. | 
| Direction | <strong>fEffectPara2</strong> | Set to one of the following values:<ul><li>0 - Specifies horizontal bow tie effect, in which the triangles enter from the right and left sides of the frame.</li><li>1 - Specifies vertical bow tie effect, in which the triangles enter from the top and bottom of the frame.</li></ul> | 
| Composition | <strong>fEffectPara3</strong> | Set to one of the following values:<ul><li>0 - Specifies normal composition, in which the previous image is the background, and the current image is the foreground.</li><li>1 - Specifies reversed composition, in which the current image is the background image, and the previous image is the foreground.</li></ul> | 




 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmsdkidl.h</dt> </dl> |



## See also

<dl> <dt>

[**Video Image Transitions**](video-image-transitions.md)
</dt> </dl>

 

 





