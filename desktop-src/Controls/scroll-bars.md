---
title: Scroll Bar
description: This section contains information about the programming elements used with scroll bars.
ms.assetid: 9cb3afad-79ef-4817-950a-c8c1de39401b
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Scroll Bar

This section contains information about the programming elements used with scroll bars. A window can display a data object, such as a document or a bitmap, that is larger than the window's client area. When provided with a *scroll bar*, the user can scroll a data object in the client area to bring into view the portions of the object that extend beyond the borders of the window.

### Overviews



| Topic                                      | Contents                                                                                                                                                                                                                                                                                                                         |
|--------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [About Scroll Bars](about-scroll-bars.md) | A scroll bar consists of a shaded shaft with an arrow button at each end and a *scroll box* (sometimes called a thumb) between the arrow buttons.<br/>                                                                                                                                                                     |
| [Using Scroll Bars](using-scroll-bars.md) | When creating an overlapped, pop-up, or child window, you can add standard scroll bars by using the [**CreateWindowEx**](https://msdn.microsoft.com/library/windows/desktop/ms632680) function and specifying [**WS\_HSCROLL**](https://msdn.microsoft.com/library/windows/desktop/ms632600#ws-hscroll), [**WS\_VSCROLL**](https://msdn.microsoft.com/library/windows/desktop/ms632600#ws-vscroll), or both styles.<br/> |



 

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
<td>[<strong>EnableScrollBar</strong>](/windows/win32/Winuser/nf-winuser-enablescrollbar?branch=master)</td>
<td>The [<strong>EnableScrollBar</strong>](/windows/win32/Winuser/nf-winuser-enablescrollbar?branch=master) function enables or disables one or both scroll bar arrows. <br/></td>
</tr>
<tr class="even">
<td>[<strong>GetScrollBarInfo</strong>](/windows/win32/Winuser/nf-winuser-getscrollbarinfo?branch=master)</td>
<td>The [<strong>GetScrollBarInfo</strong>](/windows/win32/Winuser/nf-winuser-getscrollbarinfo?branch=master) function retrieves information about the specified scroll bar.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetScrollInfo</strong>](/windows/win32/Winuser/nf-winuser-getscrollinfo?branch=master)</td>
<td>The [<strong>GetScrollInfo</strong>](/windows/win32/Winuser/nf-winuser-getscrollinfo?branch=master) function retrieves the parameters of a scroll bar, including the minimum and maximum scrolling positions, the page size, and the position of the scroll box (thumb).<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetScrollPos</strong>](/windows/win32/Winuser/nf-winuser-getscrollpos?branch=master)</td>
<td>The [<strong>GetScrollPos</strong>](/windows/win32/Winuser/nf-winuser-getscrollpos?branch=master) function retrieves the current position of the scroll box (thumb) in the specified scroll bar. The current position is a relative value that depends on the current scrolling range. For example, if the scrolling range is 0 through 100 and the scroll box is in the middle of the bar, the current position is 50.
<blockquote>
[!Note]<br />
The [<strong>GetScrollPos</strong>](/windows/win32/Winuser/nf-winuser-getscrollpos?branch=master) function is provided for backward compatibility. New applications should use the [<strong>GetScrollInfo</strong>](/windows/win32/Winuser/nf-winuser-getscrollinfo?branch=master) function.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetScrollRange</strong>](/windows/win32/Winuser/nf-winuser-getscrollrange?branch=master)</td>
<td>The [<strong>GetScrollRange</strong>](/windows/win32/Winuser/nf-winuser-getscrollrange?branch=master) function retrieves the current minimum and maximum scroll box (thumb) positions for the specified scroll bar.
<blockquote>
[!Note]<br />
The [<strong>GetScrollRange</strong>](/windows/win32/Winuser/nf-winuser-getscrollrange?branch=master) function is provided for compatibility only. New applications should use the [<strong>GetScrollInfo</strong>](/windows/win32/Winuser/nf-winuser-getscrollinfo?branch=master) function.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td>[<strong>ScrollDC</strong>](/windows/win32/Winuser/nf-winuser-scrolldc?branch=master)</td>
<td>The [<strong>ScrollDC</strong>](/windows/win32/Winuser/nf-winuser-scrolldc?branch=master) function scrolls a rectangle of bits horizontally and vertically. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>ScrollWindow</strong>](/windows/win32/Winuser/nf-winuser-scrollwindow?branch=master)</td>
<td>The [<strong>ScrollWindow</strong>](/windows/win32/Winuser/nf-winuser-scrollwindow?branch=master) function scrolls the contents of the specified window's client area.
<blockquote>
[!Note]<br />
The [<strong>ScrollWindow</strong>](/windows/win32/Winuser/nf-winuser-scrollwindow?branch=master) function is provided for backward compatibility. New applications should use the [<strong>ScrollWindowEx</strong>](/windows/win32/Winuser/nf-winuser-scrollwindowex?branch=master) function.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td>[<strong>ScrollWindowEx</strong>](/windows/win32/Winuser/nf-winuser-scrollwindowex?branch=master)</td>
<td>The [<strong>ScrollWindowEx</strong>](/windows/win32/Winuser/nf-winuser-scrollwindowex?branch=master) function scrolls the contents of the specified window's client area. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>SetScrollInfo</strong>](/windows/win32/Winuser/nf-winuser-setscrollinfo?branch=master)</td>
<td>The [<strong>SetScrollInfo</strong>](/windows/win32/Winuser/nf-winuser-setscrollinfo?branch=master) function sets the parameters of a scroll bar, including the minimum and maximum scrolling positions, the page size, and the position of the scroll box (thumb). The function also redraws the scroll bar, if requested.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SetScrollPos</strong>](/windows/win32/Winuser/nf-winuser-setscrollpos?branch=master)</td>
<td>The [<strong>SetScrollPos</strong>](/windows/win32/Winuser/nf-winuser-setscrollpos?branch=master) function sets the position of the scroll box (thumb) in the specified scroll bar and, if requested, redraws the scroll bar to reflect the new position of the scroll box.
<blockquote>
[!Note]<br />
The [<strong>SetScrollPos</strong>](/windows/win32/Winuser/nf-winuser-setscrollpos?branch=master) function is provided for backward compatibility. New applications should use the [<strong>SetScrollInfo</strong>](/windows/win32/Winuser/nf-winuser-setscrollinfo?branch=master) function.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="odd">
<td>[<strong>SetScrollRange</strong>](/windows/win32/Winuser/nf-winuser-setscrollrange?branch=master)</td>
<td>The [<strong>SetScrollRange</strong>](/windows/win32/Winuser/nf-winuser-setscrollrange?branch=master) function sets the minimum and maximum scroll box positions for the specified scroll bar.
<blockquote>
[!Note]<br />
The [<strong>SetScrollRange</strong>](/windows/win32/Winuser/nf-winuser-setscrollrange?branch=master) function is provided for backward compatibility. New applications should use the [<strong>SetScrollInfo</strong>](/windows/win32/Winuser/nf-winuser-setscrollinfo?branch=master) function.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td>[<strong>ShowScrollBar</strong>](/windows/win32/Winuser/nf-winuser-showscrollbar?branch=master)</td>
<td>The [<strong>ShowScrollBar</strong>](/windows/win32/Winuser/nf-winuser-showscrollbar?branch=master) function shows or hides the specified scroll bar. <br/></td>
</tr>
</tbody>
</table>



 

### Messages



| Topic                                                 | Contents                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SBM\_ENABLE\_ARROWS**](sbm-enable-arrows.md)      | An application sends the [**SBM\_ENABLE\_ARROWS**](sbm-enable-arrows.md) message to enable or disable one or both arrows of a scroll bar control.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**SBM\_GETPOS**](sbm-getpos.md)                     | The [**SBM\_GETPOS**](sbm-getpos.md) message is sent to retrieve the current position of the scroll box of a scroll bar control. The current position is a relative value that depends on the current scrolling range. For example, if the scrolling range is 0 through 100 and the scroll box is in the middle of the bar, the current position is 50. <br/> Applications should not send this message directly. Instead, they should use the [**GetScrollPos**](/windows/win32/Winuser/nf-winuser-getscrollpos?branch=master) function. A window receives this message through its [*WindowProc*](https://msdn.microsoft.com/library/windows/desktop/ms633573) function. Applications which implement a custom scroll bar control must respond to these messages for the **GetScrollPos** function to function properly.<br/> |
| [**SBM\_GETRANGE**](sbm-getrange.md)                 | The [**SBM\_GETRANGE**](sbm-getrange.md) message is sent to retrieve the minimum and maximum position values for the scroll bar control. <br/> Applications should not send this message directly. Instead, they should use the [**GetScrollRange**](/windows/win32/Winuser/nf-winuser-getscrollrange?branch=master) function. A window receives this message through its [*WindowProc*](https://msdn.microsoft.com/library/windows/desktop/ms633573) function. Applications which implement a custom scroll bar control must respond to these messages for the **GetScrollRange** function to work properly.<br/>                                                                                                                                                                                                              |
| [**SBM\_GETSCROLLBARINFO**](sbm-getscrollbarinfo.md) | Sent by an application to retrieve information about the specified scroll bar.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [**SBM\_GETSCROLLINFO**](sbm-getscrollinfo.md)       | The [**SBM\_GETSCROLLINFO**](sbm-getscrollinfo.md) message is sent to retrieve the parameters of a scroll bar. <br/> Applications should not send this message directly. Instead, they should use the [**GetScrollInfo**](/windows/win32/Winuser/nf-winuser-getscrollinfo?branch=master) function. A window receives this message through its [*WindowProc*](https://msdn.microsoft.com/library/windows/desktop/ms633573) function. Applications which implement a custom scroll bar control must respond to these messages for the **GetScrollInfo** function to work properly.<br/>                                                                                                                                                                                                                                           |
| [**SBM\_SETPOS**](sbm-setpos.md)                     | The [**SBM\_SETPOS**](sbm-setpos.md) message is sent to set the position of the scroll box (thumb) and, if requested, redraw the scroll bar to reflect the new position of the scroll box. <br/> Applications should not send this message directly. Instead, they should use the [**SetScrollPos**](/windows/win32/Winuser/nf-winuser-setscrollpos?branch=master) function. A window receives this message through its [*WindowProc*](https://msdn.microsoft.com/library/windows/desktop/ms633573) function. Applications which implement a custom scroll bar control must respond to these messages for the **SetScrollPos** function to work properly.<br/>                                                                                                                                                                  |
| [**SBM\_SETRANGE**](sbm-setrange.md)                 | The [**SBM\_SETRANGE**](sbm-setrange.md) message is sent to set the minimum and maximum position values for the scroll bar control. <br/> Applications should not send this message directly. Instead, they should use the [**SetScrollRange**](/windows/win32/Winuser/nf-winuser-setscrollrange?branch=master) function. A window receives this message through its [*WindowProc*](https://msdn.microsoft.com/library/windows/desktop/ms633573) function. Applications which implement a custom scroll bar control must respond to these messages for the **SetScrollRange** function to work properly.<br/>                                                                                                                                                                                                                   |
| [**SBM\_SETRANGEREDRAW**](sbm-setrangeredraw.md)     | An application sends the [**SBM\_SETRANGEREDRAW**](sbm-setrangeredraw.md) message to a scroll bar control to set the minimum and maximum position values and to redraw the control.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [**SBM\_SETSCROLLINFO**](sbm-setscrollinfo.md)       | The [**SBM\_SETSCROLLINFO**](sbm-setscrollinfo.md) message is sent to set the parameters of a scroll bar. <br/> Applications should not send this message directly. Instead, they should use the [**SetScrollInfo**](/windows/win32/Winuser/nf-winuser-setscrollinfo?branch=master) function. A window receives this message through its [*WindowProc*](https://msdn.microsoft.com/library/windows/desktop/ms633573) function. Applications which implement a custom scroll bar control must respond to these messages for the **SetScrollInfo** function to function properly.<br/>                                                                                                                                                                                                                                            |



 

### Notifications



| Topic                                                 | Contents                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WM\_CTLCOLORSCROLLBAR**](wm-ctlcolorscrollbar.md) | The [**WM\_CTLCOLORSCROLLBAR**](wm-ctlcolorscrollbar.md) message is sent to the parent window of a scroll bar control when the control is about to be drawn. By responding to this message, the parent window can use the display context handle to set the background color of the scroll bar control. <br/> A window receives this message through its [*WindowProc*](https://msdn.microsoft.com/library/windows/desktop/ms633573) function. <br/> |
| [**WM\_HSCROLL**](wm-hscroll.md)                     | The [**WM\_HSCROLL**](wm-hscroll.md) message is sent to a window when a scroll event occurs in the window's standard horizontal scroll bar. This message is also sent to the owner of a horizontal scroll bar control when a scroll event occurs in the control. <br/> A window receives this message through its [*WindowProc*](https://msdn.microsoft.com/library/windows/desktop/ms633573) function. <br/>                                        |
| [**WM\_VSCROLL**](wm-vscroll.md)                     | The [**WM\_VSCROLL**](wm-vscroll.md) message is sent to a window when a scroll event occurs in the window's standard vertical scroll bar. This message is also sent to the owner of a vertical scroll bar control when a scroll event occurs in the control. <br/> A window receives this message through its [*WindowProc*](https://msdn.microsoft.com/library/windows/desktop/ms633573) function. <br/>                                            |



 

### Structures



| Topic                                  | Contents                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SCROLLBARINFO**](/windows/win32/Winuser/ns-winuser-tagscrollbarinfo?branch=master) | The [**SCROLLBARINFO**](/windows/win32/Winuser/ns-winuser-tagscrollbarinfo?branch=master) structure contains scroll bar information.<br/>                                                                                                                                                                                                                                                           |
| [**SCROLLINFO**](/windows/win32/Winuser/ns-winuser-tagscrollinfo?branch=master)       | The [**SCROLLINFO**](/windows/win32/Winuser/ns-winuser-tagscrollinfo?branch=master) structure contains scroll bar parameters to be set by the [**SetScrollInfo**](/windows/win32/Winuser/nf-winuser-setscrollinfo?branch=master) function (or [**SBM\_SETSCROLLINFO**](sbm-setscrollinfo.md) message), or retrieved by the [**GetScrollInfo**](/windows/win32/Winuser/nf-winuser-getscrollinfo?branch=master) function (or [**SBM\_GETSCROLLINFO**](sbm-getscrollinfo.md) message). <br/> |



 

### Constants



| Topic                                                      | Contents                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Scroll Bar Control Styles](scroll-bar-control-styles.md) | To create a scroll bar control using the [**CreateWindow**](https://msdn.microsoft.com/library/windows/desktop/ms632679) or [**CreateWindowEx**](https://msdn.microsoft.com/library/windows/desktop/ms632680) function specify the SCROLLBAR class, appropriate window style constants, and a combination of the following scroll bar control styles. Some of the styles create a scroll bar control that uses a default width or height. However, you must always specify the x- and y-coordinates and the other dimensions of the scroll bar when you call **CreateWindow** or **CreateWindowEx**. <br/> |



 

 

 





