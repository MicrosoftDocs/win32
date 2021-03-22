---
title: Header Control Styles (CommCtrl.h)
description: Header controls have a number of styles, described in this section, that determine the control's appearance and behavior. You set the initial styles when you create the header control.
ms.assetid: e47dc6c3-a1af-456c-9235-29ce63f1e13b
topic_type:
- apiref
api_name:
- HDS_BUTTONS
- HDS_DRAGDROP
- HDS_FILTERBAR
- HDS_FLAT
- HDS_FULLDRAG
- HDS_HIDDEN
- HDS_HORZ
- HDS_HOTTRACK
- HDS_CHECKBOXES
- HDS_NOSIZING
- HDS_OVERFLOW
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Header Control Styles

Header controls have a number of styles, described in this section, that determine the control's appearance and behavior. You set the initial styles when you create the header control.



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
<td style="text-align: left;"><span id="HDS_BUTTONS"></span><span id="hds_buttons"></span><dl> <dt><strong>HDS_BUTTONS</strong></dt> </dl></td>
<td style="text-align: left;">Each item in the control looks and behaves like a push button. This style is useful if an application carries out a task when the user clicks an item in the header control. For example, an application could sort information in the columns differently depending on which item the user clicks. <br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="HDS_DRAGDROP"></span><span id="hds_dragdrop"></span><dl> <dt><strong>HDS_DRAGDROP</strong></dt> </dl></td>
<td style="text-align: left;">Allows drag-and-drop reordering of header items. <br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="HDS_FILTERBAR"></span><span id="hds_filterbar"></span><dl> <dt><strong>HDS_FILTERBAR</strong></dt> </dl></td>
<td style="text-align: left;">Include a filter bar as part of the standard header control. This bar allows users to conveniently apply a filter to the display. Calls to <a href="hdm-layout.md"><strong>HDM_LAYOUT</strong></a> will yield a new size for the control and cause the list view to update. <br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="HDS_FLAT"></span><span id="hds_flat"></span><dl> <dt><strong>HDS_FLAT</strong></dt> </dl></td>
<td style="text-align: left;"><a href="common-control-versions.md">Version 6.0 and later</a>. Causes the header control to be drawn flat when the operating system is running in classic mode. <br/>
<blockquote>
[!Note]<br />
Comctl32.dll version 6 is not redistributable but it is included in Windows. To use Comctl32.dll version 6, specify it in a manifest. For more information on manifests, see <a href="cookbook-overview.md">Enabling Visual Styles</a>.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="HDS_FULLDRAG"></span><span id="hds_fulldrag"></span><dl> <dt><strong>HDS_FULLDRAG</strong></dt> </dl></td>
<td style="text-align: left;">Causes the header control to display column contents even while the user resizes a column. <br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="HDS_HIDDEN"></span><span id="hds_hidden"></span><dl> <dt><strong>HDS_HIDDEN</strong></dt> </dl></td>
<td style="text-align: left;">Indicates a header control that is intended to be hidden. This style does not hide the control. Instead, when you send the <a href="hdm-layout.md"><strong>HDM_LAYOUT</strong></a> message to a header control with the HDS_HIDDEN style, the control returns zero in the <strong>cy</strong> member of the <a href="/windows/win32/api/winuser/ns-winuser-windowpos"><strong>WINDOWPOS</strong></a> structure. You would then hide the control by setting its height to zero. This can be useful when you want to use the control as an information container instead of a visual control. <br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="HDS_HORZ"></span><span id="hds_horz"></span><dl> <dt><strong>HDS_HORZ</strong></dt> </dl></td>
<td style="text-align: left;">Creates a header control with a horizontal orientation. <br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="HDS_HOTTRACK"></span><span id="hds_hottrack"></span><dl> <dt><strong>HDS_HOTTRACK</strong></dt> </dl></td>
<td style="text-align: left;">Enables hot tracking. <br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="HDS_CHECKBOXES"></span><span id="hds_checkboxes"></span><dl> <dt><strong>HDS_CHECKBOXES</strong></dt> </dl></td>
<td style="text-align: left;"><a href="common-control-versions.md">Version 6.00 and later</a>. Allows the placing of checkboxes on header items. For more information, see the <strong>fmt</strong> member of <a href="/windows/win32/api/commctrl/ns-commctrl-hditema"><strong>HDITEM</strong></a>.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="HDS_NOSIZING"></span><span id="hds_nosizing"></span><dl> <dt><strong>HDS_NOSIZING</strong></dt> </dl></td>
<td style="text-align: left;"><a href="common-control-versions.md">Version 6.00 and later</a>. The user cannot drag the divider on the header control.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="HDS_OVERFLOW"></span><span id="hds_overflow"></span><dl> <dt><strong>HDS_OVERFLOW</strong></dt> </dl></td>
<td style="text-align: left;"><a href="common-control-versions.md">Version 6.00 and later</a>. A button is displayed when not all items can be displayed within the header control's rectangle. When clicked, this button sends an <a href="hdn-overflowclick.md">HDN_OVERFLOWCLICK</a> notification.<br/></td>
</tr>
</tbody>
</table>



## Remarks

To retrieve and change the styles after creating the control, use the [**GetWindowLong**](/windows/desktop/api/winuser/nf-winuser-getwindowlonga) and [**SetWindowLong**](/windows/desktop/api/winuser/nf-winuser-setwindowlonga) functions.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



