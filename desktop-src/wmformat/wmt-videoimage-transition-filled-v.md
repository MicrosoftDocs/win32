---
title: WMT_VIDEOIMAGE_TRANSITION_FILLED_V (Wmsdkidl.h)
description: The filled V transition reveals the new image in a triangle originating from one side of the frame.
ms.assetid: d256178f-cb1d-4d36-9d30-e6dd6b3b23ec
keywords:
- WMT_VIDEOIMAGE_TRANSITION_FILLED_V windows Media Format
topic_type:
- apiref
api_name:
- WMT_VIDEOIMAGE_TRANSITION_FILLED_V
api_location:
- wmsdkidl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WMT\_VIDEOIMAGE\_TRANSITION\_FILLED\_V

The filled V transition reveals the new image in a triangle originating from one side of the frame.

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
<td>Width</td>
<td><strong>fEffectPara0</strong></td>
<td>Width of the filled V in pixels.</td>
</tr>
<tr class="even">
<td>Height</td>
<td><strong>fEffectPara1</strong></td>
<td>Height of the filled V in pixels.</td>
</tr>
<tr class="odd">
<td>Direction</td>
<td><strong>fEffectPara2</strong></td>
<td>Direction from which the filled V originates.Set to one of the following values:<br/>
<ul>
<li>0 - Enters from the left side of the frame.</li>
<li>1 - Enters from the right side of the frame.</li>
<li>2 - Enters from the bottom of the frame.</li>
<li>3 - Enters from the top of the frame.</li>
</ul></td>
</tr>
<tr class="even">
<td>Composition</td>
<td><strong>fEffectPara3</strong></td>
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

 

 





