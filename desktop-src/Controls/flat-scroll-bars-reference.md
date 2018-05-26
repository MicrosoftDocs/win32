---
title: Flat Scroll Bar
description: This section contains information about the programming elements used to control flat scroll bars.
ms.assetid: c9f6bd60-c55f-49ad-b6e7-193743a1cdec
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Flat Scroll Bar

This section contains information about the programming elements used to control flat scroll bars.

### Overviews



| Topic                                    | Contents                                                                                                                                                                                                                                                                              |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Flat Scroll Bars](flat-scroll-bars.md) | Microsoft Internet Explorer 4.0 introduced a new visual technology called flat scroll bars. Functionally, flat scroll bars behave just like standard scroll bars. The difference is that you can customize their appearance to a greater extent than standard scroll bars.<br/> |



 

### Functions



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Contents</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>FlatSB_EnableScrollBar</strong>](/windows/win32/Commctrl/nf-commctrl-flatsb_enablescrollbar?branch=master)</td>
<td>Enables or disables one or both flat scroll bar direction buttons. If flat scroll bars are not initialized for the window, this function calls the standard [<strong>EnableScrollBar</strong>](/windows/win32/Winuser/nf-winuser-enablescrollbar?branch=master) function. <br/></td>
</tr>
<tr class="even">
<td>[<strong>FlatSB_GetScrollInfo</strong>](/windows/win32/Commctrl/nf-commctrl-flatsb_getscrollinfo?branch=master)</td>
<td>Gets the information for a flat scroll bar. If flat scroll bars are not initialized for the window, this function calls the standard [<strong>GetScrollInfo</strong>](/windows/win32/Winuser/nf-winuser-getscrollinfo?branch=master) function. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>FlatSB_GetScrollPos</strong>](/windows/win32/Commctrl/nf-commctrl-flatsb_getscrollpos?branch=master)</td>
<td>Gets the thumb position in a flat scroll bar. If flat scroll bars are not initialized for the window, this function calls the standard [<strong>GetScrollPos</strong>](/windows/win32/Winuser/nf-winuser-getscrollpos?branch=master) function. <br/></td>
</tr>
<tr class="even">
<td>[<strong>FlatSB_GetScrollProp</strong>](/windows/win32/Commctrl/nf-commctrl-flatsb_getscrollprop?branch=master)</td>
<td>Gets the properties for a flat scroll bar. This function can also be used to determine if [<strong>InitializeFlatSB</strong>](/windows/win32/Commctrl/nf-commctrl-initializeflatsb?branch=master) has been called for this window. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>FlatSB_GetScrollPropPtr</strong>](/windows/win32/Commctrl/nf-commctrl-flatsb_getscrollpropptr?branch=master)</td>
<td>Gets the properties for a flat scroll bar. This function can also be used to determine if [<strong>InitializeFlatSB</strong>](/windows/win32/Commctrl/nf-commctrl-initializeflatsb?branch=master) has been called for this window.
<blockquote>
[!Note]<br />
This is identical to [<strong>FlatSB_GetScrollProp</strong>](/windows/win32/Commctrl/nf-commctrl-flatsb_getscrollprop?branch=master).
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td>[<strong>FlatSB_GetScrollRange</strong>](/windows/win32/Commctrl/nf-commctrl-flatsb_getscrollrange?branch=master)</td>
<td>Gets the scroll range for a flat scroll bar. If flat scroll bars are not initialized for the window, this function calls the standard [<strong>GetScrollRange</strong>](/windows/win32/Winuser/nf-winuser-getscrollrange?branch=master) function. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>FlatSB_SetScrollInfo</strong>](/windows/win32/Commctrl/nf-commctrl-flatsb_setscrollinfo?branch=master)</td>
<td>Sets the information for a flat scroll bar. If flat scroll bars are not initialized for the window, this function calls the standard [<strong>SetScrollInfo</strong>](/windows/win32/Winuser/nf-winuser-setscrollinfo?branch=master) function. <br/></td>
</tr>
<tr class="even">
<td>[<strong>FlatSB_SetScrollPos</strong>](/windows/win32/Commctrl/nf-commctrl-flatsb_setscrollpos?branch=master)</td>
<td>Sets the current position of the thumb in a flat scroll bar. If flat scroll bars are not initialized for the window, this function calls the standard [<strong>SetScrollPos</strong>](/windows/win32/Winuser/nf-winuser-setscrollpos?branch=master) function. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>FlatSB_SetScrollProp</strong>](/windows/win32/Commctrl/nf-commctrl-flatsb_setscrollprop?branch=master)</td>
<td>Sets the properties for a flat scroll bar. <br/></td>
</tr>
<tr class="even">
<td>[<strong>FlatSB_SetScrollRange</strong>](/windows/win32/Commctrl/nf-commctrl-flatsb_setscrollrange?branch=master)</td>
<td>Sets the scroll range of a flat scroll bar. If flat scroll bars are not initialized for the window, this function calls the standard [<strong>SetScrollRange</strong>](/windows/win32/Winuser/nf-winuser-setscrollrange?branch=master) function. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>FlatSB_ShowScrollBar</strong>](/windows/win32/Commctrl/nf-commctrl-flatsb_showscrollbar?branch=master)</td>
<td>Shows or hides a flat scroll bar. If flat scroll bars are not initialized for the window, this function calls the standard [<strong>ShowScrollBar</strong>](/windows/win32/Winuser/nf-winuser-showscrollbar?branch=master) function. <br/></td>
</tr>
<tr class="even">
<td>[<strong>InitializeFlatSB</strong>](/windows/win32/Commctrl/nf-commctrl-initializeflatsb?branch=master)</td>
<td>Initializes flat scroll bars for a particular window. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>UninitializeFlatSB</strong>](/windows/win32/Commctrl/nf-commctrl-uninitializeflatsb?branch=master)</td>
<td>Uninitializes flat scroll bars for a particular window. The specified window will revert to standard scroll bars. <br/></td>
</tr>
</tbody>
</table>



 

 

 





