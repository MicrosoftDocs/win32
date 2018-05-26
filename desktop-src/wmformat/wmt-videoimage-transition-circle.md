---
title: WMT\_VIDEOIMAGE\_TRANSITION\_CIRCLE
description: The circle transition reveals the new image in a circle.
ms.assetid: ba3bcf46-1254-4aad-a958-0f9ddb2f40dc
keywords:
- WMT_VIDEOIMAGE_TRANSITION_CIRCLE windows Media Format
topic_type:
- apiref
api_name:
- WMT_VIDEOIMAGE_TRANSITION_CIRCLE
api_location:
- wmsdkidl.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WMT\_VIDEOIMAGE\_TRANSITION\_CIRCLE

The circle transition reveals the new image in a circle.

## Parameters

The following table describes the parameters used by this transition and lists the members of the [**WMT\_VIDEOIMAGE\_SAMPLE2**](/windows/win32/Wmsdkidl/ns-wmsdkidl-__wmt_videoimage_sample2?branch=master) structure to which they are assigned.



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
<td>X-coordinate, relative to the video frame, of the center of the circle.</td>
</tr>
<tr class="even">
<td>Center Y</td>
<td><strong>fEffectPara1</strong></td>
<td>Y-coordinate, relative to the video frame, of center of the circle.</td>
</tr>
<tr class="odd">
<td>Radius</td>
<td><strong>fEffectPara2</strong></td>
<td>Radius, in pixels, of the circle.</td>
</tr>
<tr class="even">
<td>Composition</td>
<td><strong>fEffectPara3</strong></td>
<td>Set to one of the following values:
<ul>
<li>0 - Specifies normal composition, in which the previous image is the background, and the current image is the foreground.</li>
<li>1 - Specifies reversed composition, in which the current image is the background image, and the previous image is the foreground.</li>
</ul></td>
</tr>
</tbody>
</table>



 

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmsdkidl.h</dt> </dl> |



## See also

<dl> <dt>

[**Video Image Transitions**](video-image-transitions.md)
</dt> </dl>

 

 





