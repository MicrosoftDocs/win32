---
title: Functions
description: This section contains reference information about the Magnification API functions.
ms.assetid: 82b7d82b-b8cd-4f80-ad30-f7db20c57742
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Functions

This section contains reference information about the Magnification API functions.

## In this section



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>MagGetColorEffect</strong>](/previous-versions/windows/desktop/api/Magnification/nf-magnification-maggetcoloreffect)<br/></td>
<td>Gets the color transformation matrix for a magnifier control.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MagGetFullscreenColorEffect</strong>](/previous-versions/windows/desktop/api/Magnification/nf-magnification-maggetfullscreencoloreffect)<br/></td>
<td>Retrieves the color transformation matrix associated with the full-screen magnifier.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MagGetFullscreenTransform</strong>](/previous-versions/windows/desktop/api/Magnification/nf-magnification-maggetfullscreentransform)<br/></td>
<td>Retrieves the magnification settings for the full-screen magnifier.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MagGetImageScalingCallback</strong>](/previous-versions/windows/desktop/api/Magnification/nf-magnification-maggetimagescalingcallback)<br/></td>
<td><blockquote>
[!Note]<br />
The [<strong>MagGetImageScalingCallback</strong>](/previous-versions/windows/desktop/api/Magnification/nf-magnification-maggetimagescalingcallback) function is deprecated in Windows 7 and later, and should not be used in new applications. There is no alternate functionality.
</blockquote>
<br/> <br/> Retrieves the registered callback function that implements a custom transform for image scaling. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>MagGetInputTransform</strong>](/previous-versions/windows/desktop/api/Magnification/nf-magnification-maggetinputtransform)<br/></td>
<td>Retrieves the current input transformation for pen and touch input, represented as a source rectangle and a destination rectangle.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MagGetWindowFilterList</strong>](/previous-versions/windows/desktop/api/Magnification/nf-magnification-maggetwindowfilterlist)<br/></td>
<td>Retrieves the list of windows that are magnified or excluded from magnification.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MagGetWindowSource</strong>](/previous-versions/windows/desktop/api/Magnification/nf-magnification-maggetwindowsource)<br/></td>
<td>Gets the rectangle of the area that is being magnified.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MagGetWindowTransform</strong>](/previous-versions/windows/desktop/api/Magnification/nf-magnification-maggetwindowtransform)<br/></td>
<td>Retrieves the transformation matrix associated with a magnifier control. <br/></td>
</tr>
<tr class="odd">
<td>[<em>MagImageScalingCallback</em>](/previous-versions/windows/desktop/api/Magnification/nc-magnification-magimagescalingcallback)<br/></td>
<td><blockquote>
[!Note]<br />
The [<em>MagImageScalingCallback</em>](/previous-versions/windows/desktop/api/Magnification/nc-magnification-magimagescalingcallback) function is deprecated in Windows 7 and later, and should not be used in new applications. There is no alternate functionality.
</blockquote>
<br/> Prototype for a callback function that implements a custom transform for image scaling.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MagInitialize</strong>](/previous-versions/windows/desktop/api/Magnification/nf-magnification-maginitialize)<br/></td>
<td>Creates and initializes the magnifier run-time objects. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>MagSetColorEffect</strong>](/previous-versions/windows/desktop/api/Magnification/nf-magnification-magsetcoloreffect)<br/></td>
<td>Sets the color transformation matrix for a magnifier control.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MagSetFullscreenColorEffect</strong>](/previous-versions/windows/desktop/api/Magnification/nf-magnification-magsetfullscreencoloreffect)<br/></td>
<td>Changes the color transformation matrix associated with the full-screen magnifier.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MagSetFullscreenTransform</strong>](/previous-versions/windows/desktop/api/Magnification/nf-magnification-magsetfullscreentransform)<br/></td>
<td>Changes the magnification settings for the full-screen magnifier.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MagSetImageScalingCallback</strong>](/previous-versions/windows/desktop/api/Magnification/nf-magnification-magsetimagescalingcallback)<br/></td>
<td><blockquote>
[!Note]<br />
The [<strong>MagSetImageScalingCallback</strong>](/previous-versions/windows/desktop/api/Magnification/nf-magnification-magsetimagescalingcallback) function is deprecated in Windows 7 and later, and should not be used in new applications. There is no alternate functionality.
</blockquote>
<br/> <br/> Sets the callback function for external image filtering and scaling.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MagSetInputTransform</strong>](/previous-versions/windows/desktop/api/Magnification/nf-magnification-magsetinputtransform)<br/></td>
<td>Sets the current active input transformation for pen and touch input, represented as a source rectangle and a destination rectangle.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MagSetWindowFilterList</strong>](/previous-versions/windows/desktop/api/Magnification/nf-magnification-magsetwindowfilterlist)<br/></td>
<td>Sets the list of windows to be magnified or the list of windows to be excluded from magnification.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MagSetWindowSource</strong>](/previous-versions/windows/desktop/api/Magnification/nf-magnification-magsetwindowsource)<br/></td>
<td>Sets the source rectangle for the magnification window.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MagSetWindowTransform</strong>](/previous-versions/windows/desktop/api/Magnification/nf-magnification-magsetwindowtransform)<br/></td>
<td>Sets the transformation matrix for a magnifier control. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>MagShowSystemCursor</strong>](/previous-versions/windows/desktop/api/Magnification/nf-magnification-magshowsystemcursor)<br/></td>
<td>Shows or hides the system cursor.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MagUninitialize</strong>](/previous-versions/windows/desktop/api/Magnification/nf-magnification-maguninitialize)<br/></td>
<td>Destroys the magnifier run-time objects.<br/></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Reference](entry-magapi-ref.md)
</dt> </dl>

 

 





