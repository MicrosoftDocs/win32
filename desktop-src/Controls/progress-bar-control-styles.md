---
title: Progress Bar Control Styles (CommCtrl.h)
description: The following control styles are supported by Progress Bar controls
ms.assetid: bd89aa74-c15e-4745-8b2b-7cbd8b28c1c8
topic_type:
- apiref
api_name:
- PBS_MARQUEE
- PBS_SMOOTH
- PBS_SMOOTHREVERSE
- PBS_VERTICAL
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Progress Bar Control Styles

The following control styles are supported by [Progress Bar](progress-bar-control.md) controls:



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Constant</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><span id="PBS_MARQUEE"></span><span id="pbs_marquee"></span><dl> <dt><strong>PBS_MARQUEE</strong></dt> </dl></td>
<td style="text-align: left;"><a href="common-control-versions.md">Version 6.0</a> or later. The progress indicator does not grow in size but instead moves repeatedly along the length of the bar, indicating activity without specifying what proportion of the progress is complete. <br/>
<blockquote>
[!Note]<br />
Comctl32.dll version 6 is not redistributable but it is included in Windows or later. To use Comctl32.dll version 6, specify it in a manifest. For more information on manifests, see <a href="cookbook-overview.md">Enabling Visual Styles</a>.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="PBS_SMOOTH"></span><span id="pbs_smooth"></span><dl> <dt><strong>PBS_SMOOTH</strong></dt> </dl></td>
<td style="text-align: left;"><a href="common-control-versions.md">Version 4.70</a> or later. The progress bar displays progress status in a smooth scrolling bar instead of the default segmented bar. <br/>
<blockquote>
[!Note]<br />
This style is supported only in the Windows Classic theme. All other themes override this style.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="PBS_SMOOTHREVERSE"></span><span id="pbs_smoothreverse"></span><dl> <dt><strong>PBS_SMOOTHREVERSE</strong></dt> </dl></td>
<td style="text-align: left;"><a href="common-control-versions.md">Version 6.0</a> or later and <strong>Windows Vista.</strong> Determines the animation behavior that the progress bar should use when moving backward (from a higher value to a lower value). If this is set, then a &quot;smooth&quot; transition will occur, otherwise the control will &quot;jump&quot; to the lower value.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="PBS_VERTICAL"></span><span id="pbs_vertical"></span><dl> <dt><strong>PBS_VERTICAL</strong></dt> </dl></td>
<td style="text-align: left;"><a href="common-control-versions.md">Version 4.70</a> or later. The progress bar displays progress status vertically, from bottom to top.<br/></td>
</tr>
</tbody>
</table>



## Remarks

You can set progress bar styles, in the same way as other common controls, with [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa), [**GetWindowLong**](/windows/desktop/api/winuser/nf-winuser-getwindowlonga), or [**SetWindowLong**](/windows/desktop/api/winuser/nf-winuser-setwindowlonga).

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



 

