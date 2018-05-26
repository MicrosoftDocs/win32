---
title: Functions
description: This section contains reference information about the Magnification API functions.
ms.assetid: 82b7d82b-b8cd-4f80-ad30-f7db20c57742
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
<td>[<strong>MagGetColorEffect</strong>](/windows/previous-versions/Magnification/nf-magnification-maggetcoloreffect?branch=master)<br/></td>
<td>Gets the color transformation matrix for a magnifier control.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MagGetFullscreenColorEffect</strong>](/windows/previous-versions/Magnification/nf-magnification-maggetfullscreencoloreffect?branch=master)<br/></td>
<td>Retrieves the color transformation matrix associated with the full-screen magnifier.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MagGetFullscreenTransform</strong>](/windows/previous-versions/Magnification/nf-magnification-maggetfullscreentransform?branch=master)<br/></td>
<td>Retrieves the magnification settings for the full-screen magnifier.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MagGetImageScalingCallback</strong>](/windows/previous-versions/Magnification/nf-magnification-maggetimagescalingcallback?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
The [<strong>MagGetImageScalingCallback</strong>](/windows/previous-versions/Magnification/nf-magnification-maggetimagescalingcallback?branch=master) function is deprecated in Windows 7 and later, and should not be used in new applications. There is no alternate functionality.
</blockquote>
<br/> <br/> Retrieves the registered callback function that implements a custom transform for image scaling. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>MagGetInputTransform</strong>](/windows/previous-versions/Magnification/nf-magnification-maggetinputtransform?branch=master)<br/></td>
<td>Retrieves the current input transformation for pen and touch input, represented as a source rectangle and a destination rectangle.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MagGetWindowFilterList</strong>](/windows/previous-versions/Magnification/nf-magnification-maggetwindowfilterlist?branch=master)<br/></td>
<td>Retrieves the list of windows that are magnified or excluded from magnification.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MagGetWindowSource</strong>](/windows/previous-versions/Magnification/nf-magnification-maggetwindowsource?branch=master)<br/></td>
<td>Gets the rectangle of the area that is being magnified.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MagGetWindowTransform</strong>](/windows/previous-versions/Magnification/nf-magnification-maggetwindowtransform?branch=master)<br/></td>
<td>Retrieves the transformation matrix associated with a magnifier control. <br/></td>
</tr>
<tr class="odd">
<td>[<em>MagImageScalingCallback</em>](/windows/previous-versions/Magnification/nc-magnification-magimagescalingcallback?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
The [<em>MagImageScalingCallback</em>](/windows/previous-versions/Magnification/nc-magnification-magimagescalingcallback?branch=master) function is deprecated in Windows 7 and later, and should not be used in new applications. There is no alternate functionality.
</blockquote>
<br/> Prototype for a callback function that implements a custom transform for image scaling.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MagInitialize</strong>](/windows/previous-versions/Magnification/nf-magnification-maginitialize?branch=master)<br/></td>
<td>Creates and initializes the magnifier run-time objects. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>MagSetColorEffect</strong>](/windows/previous-versions/Magnification/nf-magnification-magsetcoloreffect?branch=master)<br/></td>
<td>Sets the color transformation matrix for a magnifier control.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MagSetFullscreenColorEffect</strong>](/windows/previous-versions/Magnification/nf-magnification-magsetfullscreencoloreffect?branch=master)<br/></td>
<td>Changes the color transformation matrix associated with the full-screen magnifier.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MagSetFullscreenTransform</strong>](/windows/previous-versions/Magnification/nf-magnification-magsetfullscreentransform?branch=master)<br/></td>
<td>Changes the magnification settings for the full-screen magnifier.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MagSetImageScalingCallback</strong>](/windows/previous-versions/Magnification/nf-magnification-magsetimagescalingcallback?branch=master)<br/></td>
<td><blockquote>
[!Note]<br />
The [<strong>MagSetImageScalingCallback</strong>](/windows/previous-versions/Magnification/nf-magnification-magsetimagescalingcallback?branch=master) function is deprecated in Windows 7 and later, and should not be used in new applications. There is no alternate functionality.
</blockquote>
<br/> <br/> Sets the callback function for external image filtering and scaling.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MagSetInputTransform</strong>](/windows/previous-versions/Magnification/nf-magnification-magsetinputtransform?branch=master)<br/></td>
<td>Sets the current active input transformation for pen and touch input, represented as a source rectangle and a destination rectangle.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MagSetWindowFilterList</strong>](/windows/previous-versions/Magnification/nf-magnification-magsetwindowfilterlist?branch=master)<br/></td>
<td>Sets the list of windows to be magnified or the list of windows to be excluded from magnification.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MagSetWindowSource</strong>](/windows/previous-versions/Magnification/nf-magnification-magsetwindowsource?branch=master)<br/></td>
<td>Sets the source rectangle for the magnification window.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MagSetWindowTransform</strong>](/windows/previous-versions/Magnification/nf-magnification-magsetwindowtransform?branch=master)<br/></td>
<td>Sets the transformation matrix for a magnifier control. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>MagShowSystemCursor</strong>](/windows/previous-versions/Magnification/nf-magnification-magshowsystemcursor?branch=master)<br/></td>
<td>Shows or hides the system cursor.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MagUninitialize</strong>](/windows/previous-versions/Magnification/nf-magnification-maguninitialize?branch=master)<br/></td>
<td>Destroys the magnifier run-time objects.<br/></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Reference](entry-magapi-ref.md)
</dt> </dl>

 

 





