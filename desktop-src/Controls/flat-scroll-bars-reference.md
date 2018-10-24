---
title: Flat Scroll Bar
description: This section contains information about the programming elements used to control flat scroll bars.
ms.assetid: 'vs|controls|~\controls\flatsb\reflist.htm'
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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
<td><a href="/windows/desktop/api/Commctrl/nf-commctrl-flatsb_enablescrollbar"><strong>FlatSB_EnableScrollBar</strong></a></td>
<td>Enables or disables one or both flat scroll bar direction buttons. If flat scroll bars are not initialized for the window, this function calls the standard <a href="/windows/desktop/api/Winuser/nf-winuser-enablescrollbar"><strong>EnableScrollBar</strong></a> function. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Commctrl/nf-commctrl-flatsb_getscrollinfo"><strong>FlatSB_GetScrollInfo</strong></a></td>
<td>Gets the information for a flat scroll bar. If flat scroll bars are not initialized for the window, this function calls the standard <a href="/windows/desktop/api/Winuser/nf-winuser-getscrollinfo"><strong>GetScrollInfo</strong></a> function. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Commctrl/nf-commctrl-flatsb_getscrollpos"><strong>FlatSB_GetScrollPos</strong></a></td>
<td>Gets the thumb position in a flat scroll bar. If flat scroll bars are not initialized for the window, this function calls the standard <a href="/windows/desktop/api/Winuser/nf-winuser-getscrollpos"><strong>GetScrollPos</strong></a> function. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Commctrl/nf-commctrl-flatsb_getscrollprop"><strong>FlatSB_GetScrollProp</strong></a></td>
<td>Gets the properties for a flat scroll bar. This function can also be used to determine if <a href="/windows/desktop/api/Commctrl/nf-commctrl-initializeflatsb"><strong>InitializeFlatSB</strong></a> has been called for this window. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Commctrl/nf-commctrl-flatsb_getscrollpropptr"><strong>FlatSB_GetScrollPropPtr</strong></a></td>
<td>Gets the properties for a flat scroll bar. This function can also be used to determine if <a href="/windows/desktop/api/Commctrl/nf-commctrl-initializeflatsb"><strong>InitializeFlatSB</strong></a> has been called for this window.
<blockquote>
[!Note]<br />
This is identical to <a href="/windows/desktop/api/Commctrl/nf-commctrl-flatsb_getscrollprop"><strong>FlatSB_GetScrollProp</strong></a>.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Commctrl/nf-commctrl-flatsb_getscrollrange"><strong>FlatSB_GetScrollRange</strong></a></td>
<td>Gets the scroll range for a flat scroll bar. If flat scroll bars are not initialized for the window, this function calls the standard <a href="/windows/desktop/api/Winuser/nf-winuser-getscrollrange"><strong>GetScrollRange</strong></a> function. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Commctrl/nf-commctrl-flatsb_setscrollinfo"><strong>FlatSB_SetScrollInfo</strong></a></td>
<td>Sets the information for a flat scroll bar. If flat scroll bars are not initialized for the window, this function calls the standard <a href="/windows/desktop/api/Winuser/nf-winuser-setscrollinfo"><strong>SetScrollInfo</strong></a> function. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Commctrl/nf-commctrl-flatsb_setscrollpos"><strong>FlatSB_SetScrollPos</strong></a></td>
<td>Sets the current position of the thumb in a flat scroll bar. If flat scroll bars are not initialized for the window, this function calls the standard <a href="/windows/desktop/api/Winuser/nf-winuser-setscrollpos"><strong>SetScrollPos</strong></a> function. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Commctrl/nf-commctrl-flatsb_setscrollprop"><strong>FlatSB_SetScrollProp</strong></a></td>
<td>Sets the properties for a flat scroll bar. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Commctrl/nf-commctrl-flatsb_setscrollrange"><strong>FlatSB_SetScrollRange</strong></a></td>
<td>Sets the scroll range of a flat scroll bar. If flat scroll bars are not initialized for the window, this function calls the standard <a href="/windows/desktop/api/Winuser/nf-winuser-setscrollrange"><strong>SetScrollRange</strong></a> function. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Commctrl/nf-commctrl-flatsb_showscrollbar"><strong>FlatSB_ShowScrollBar</strong></a></td>
<td>Shows or hides a flat scroll bar. If flat scroll bars are not initialized for the window, this function calls the standard <a href="/windows/desktop/api/Winuser/nf-winuser-showscrollbar"><strong>ShowScrollBar</strong></a> function. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Commctrl/nf-commctrl-initializeflatsb"><strong>InitializeFlatSB</strong></a></td>
<td>Initializes flat scroll bars for a particular window. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Commctrl/nf-commctrl-uninitializeflatsb"><strong>UninitializeFlatSB</strong></a></td>
<td>Uninitializes flat scroll bars for a particular window. The specified window will revert to standard scroll bars. <br/></td>
</tr>
</tbody>
</table>



 

 

 





