---
title: WMT_VIDEOIMAGE_TRANSITION_IRIS (Wmsdkidl.h)
description: The iris transition reveals the new image along an x-axis and a y-axis. The visual effect of this transition is that the new image appears in a widening cross reaching to all sides of the frame.
ms.assetid: 7390d959-a566-43e7-937d-1e617bc98a6e
keywords:
- WMT_VIDEOIMAGE_TRANSITION_IRIS windows Media Format
topic_type:
- apiref
api_name:
- WMT_VIDEOIMAGE_TRANSITION_IRIS
api_location:
- wmsdkidl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMT\_VIDEOIMAGE\_TRANSITION\_IRIS

The iris transition reveals the new image along an x-axis and a y-axis. The visual effect of this transition is that the new image appears in a widening cross reaching to all sides of the frame.

## Parameters

The following table describes the parameters used by this transition and lists the members of the [**WMT\_VIDEOIMAGE\_SAMPLE2**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_videoimage_sample2) structure to which they are assigned.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Structure member</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Center X</td>
<td><strong>fEffectPara0</strong></td>
<td>X-coordinate, relative to the video frame, of the center of the iris effect.</td>
</tr>
<tr class="even">
<td>Center Y</td>
<td><strong>fEffectPara1</strong></td>
<td>Y-coordinate, relative to the video frame, of the center of the iris effect.</td>
</tr>
<tr class="odd">
<td>Width</td>
<td><strong>fEffectPara2</strong></td>
<td>Width of the vertical line revealing the new image, in pixels.</td>
</tr>
<tr class="even">
<td>Height</td>
<td><strong>fEffectPara3</strong></td>
<td>Height of the horizontal line revealing the new image, in pixels.</td>
</tr>
<tr class="odd">
<td>Composition</td>
<td><strong>fEffectPara4</strong></td>
<td>Set to one of the following values:
<ul>
<li>0 - Specifies normal composition, in which the previous image is the background, and the current image is the foreground.</li>
<li>1 - Specifies reversed composition, in which the current image is the background image, and the previous image is the foreground</li>
</ul></td>
</tr>
</tbody>
</table>



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmsdkidl.h</dt> </dl> |



## See also

<dl> <dt>

[**Video Image Transitions**](video-image-transitions.md)
</dt> </dl>

 

 





