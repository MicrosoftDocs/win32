---
title: DWM Messages
description: This section contains information about the Desktop Window Manager (DWM) messages.
ms.assetid: 'FF251CDA-7D68-4dd0-A54B-50B07E11C7C1'
keywords: ["Desktop Window Manager (DWM),reference", "DWM (Desktop Window Manager),reference", "Desktop Window Manager (DWM),messages", "DWM (Desktop Window Manager),messages"]
---

# DWM Messages

This section contains information about the Desktop Window Manager (DWM) messages.

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
<td>[<strong>WM_DWMCOLORIZATIONCOLORCHANGED</strong>](wm-dwmcolorizationcolorchanged.md)<br/></td>
<td>Informs all top-level windows that the colorization color has changed.<br/></td>
</tr>
<tr class="even">
<td>[<strong>WM_DWMCOMPOSITIONCHANGED</strong>](wm-dwmcompositionchanged.md)<br/></td>
<td>Informs all top-level windows that DWM composition has been enabled or disabled. <br/>
<blockquote>
[!Note]<br />
As of Windows 8, DWM composition is always enabled, so this message is not sent regardless of video mode changes.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>WM_DWMNCRENDERINGCHANGED</strong>](wm-dwmncrenderingchanged.md)<br/></td>
<td>Sent when the non-client area rendering policy has changed.<br/></td>
</tr>
<tr class="even">
<td>[<strong>WM_DWMSENDICONICLIVEPREVIEWBITMAP</strong>](wm-dwmsendiconiclivepreviewbitmap.md)<br/></td>
<td>Instructs a window to provide a static bitmap to use as a <em>live preview</em> (also known as a <em>Peek preview</em>) of that window.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>WM_DWMSENDICONICTHUMBNAIL</strong>](wm-dwmsendiconicthumbnail.md)<br/></td>
<td>Instructs a window to provide a static bitmap to use as a thumbnail representation of that window.<br/></td>
</tr>
<tr class="even">
<td>[<strong>WM_DWMWINDOWMAXIMIZEDCHANGE</strong>](wm-dwmwindowmaximizedchange.md)<br/></td>
<td>Sent when a DWM composed window is maximized.<br/></td>
</tr>
</tbody>
</table>



 

 

 





