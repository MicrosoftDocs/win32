---
title: Flat Scroll Bar
description: This section contains information about the programming elements used to control flat scroll bars.
ms.assetid: 'c9f6bd60-c55f-49ad-b6e7-193743a1cdec'
---

# Flat Scroll Bar

This section contains information about the programming elements used to control flat scroll bars.

### Overviews



| Topic                                    | Contents                                                                                                                                                                                                                                                                              |
|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Flat Scroll Bars](flat-scroll-bars.md) | Microsoft Internet Explorer 4.0 introduced a new visual technology called flat scroll bars. Functionally, flat scroll bars behave just like standard scroll bars. The difference is that you can customize their appearance to a greater extent than standard scroll bars.<br/> |



 

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
<td>[<strong>FlatSB_EnableScrollBar</strong>](flatsb-enablescrollbar.md)</td>
<td>Enables or disables one or both flat scroll bar direction buttons. If flat scroll bars are not initialized for the window, this function calls the standard [<strong>EnableScrollBar</strong>](enablescrollbar.md) function. <br/></td>
</tr>
<tr class="even">
<td>[<strong>FlatSB_GetScrollInfo</strong>](flatsb-getscrollinfo.md)</td>
<td>Gets the information for a flat scroll bar. If flat scroll bars are not initialized for the window, this function calls the standard [<strong>GetScrollInfo</strong>](getscrollinfo.md) function. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>FlatSB_GetScrollPos</strong>](flatsb-getscrollpos.md)</td>
<td>Gets the thumb position in a flat scroll bar. If flat scroll bars are not initialized for the window, this function calls the standard [<strong>GetScrollPos</strong>](getscrollpos.md) function. <br/></td>
</tr>
<tr class="even">
<td>[<strong>FlatSB_GetScrollProp</strong>](flatsb-getscrollprop.md)</td>
<td>Gets the properties for a flat scroll bar. This function can also be used to determine if [<strong>InitializeFlatSB</strong>](initializeflatsb.md) has been called for this window. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>FlatSB_GetScrollPropPtr</strong>](flatsb-getscrollpropptr.md)</td>
<td>Gets the properties for a flat scroll bar. This function can also be used to determine if [<strong>InitializeFlatSB</strong>](initializeflatsb.md) has been called for this window.
<blockquote>
[!Note]<br />
This is identical to [<strong>FlatSB_GetScrollProp</strong>](flatsb-getscrollprop.md).
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td>[<strong>FlatSB_GetScrollRange</strong>](flatsb-getscrollrange.md)</td>
<td>Gets the scroll range for a flat scroll bar. If flat scroll bars are not initialized for the window, this function calls the standard [<strong>GetScrollRange</strong>](getscrollrange.md) function. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>FlatSB_SetScrollInfo</strong>](flatsb-setscrollinfo.md)</td>
<td>Sets the information for a flat scroll bar. If flat scroll bars are not initialized for the window, this function calls the standard [<strong>SetScrollInfo</strong>](setscrollinfo.md) function. <br/></td>
</tr>
<tr class="even">
<td>[<strong>FlatSB_SetScrollPos</strong>](flatsb-setscrollpos.md)</td>
<td>Sets the current position of the thumb in a flat scroll bar. If flat scroll bars are not initialized for the window, this function calls the standard [<strong>SetScrollPos</strong>](setscrollpos.md) function. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>FlatSB_SetScrollProp</strong>](flatsb-setscrollprop.md)</td>
<td>Sets the properties for a flat scroll bar. <br/></td>
</tr>
<tr class="even">
<td>[<strong>FlatSB_SetScrollRange</strong>](flatsb-setscrollrange.md)</td>
<td>Sets the scroll range of a flat scroll bar. If flat scroll bars are not initialized for the window, this function calls the standard [<strong>SetScrollRange</strong>](setscrollrange.md) function. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>FlatSB_ShowScrollBar</strong>](flatsb-showscrollbar.md)</td>
<td>Shows or hides a flat scroll bar. If flat scroll bars are not initialized for the window, this function calls the standard [<strong>ShowScrollBar</strong>](showscrollbar.md) function. <br/></td>
</tr>
<tr class="even">
<td>[<strong>InitializeFlatSB</strong>](initializeflatsb.md)</td>
<td>Initializes flat scroll bars for a particular window. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>UninitializeFlatSB</strong>](uninitializeflatsb.md)</td>
<td>Uninitializes flat scroll bars for a particular window. The specified window will revert to standard scroll bars. <br/></td>
</tr>
</tbody>
</table>



 

 

 





