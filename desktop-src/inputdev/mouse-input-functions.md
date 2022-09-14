---
title: Mouse Input Functions
description: Mouse Input Functions
ms.assetid: a666b25b-a75c-4500-8077-fabe07589a1d
ms.topic: article
ms.date: 05/31/2018
---

# Mouse Input Functions


## In this section




| Topic | Description | 
|-------|-------------|
| <a href="/windows/win32/api/commctrl/nf-commctrl-_trackmouseevent"><strong>_TrackMouseEvent</strong></a><br /> | Posts messages when the mouse pointer leaves a window or hovers over a window for a specified amount of time. This function calls <a href="/windows/desktop/api/winuser/nf-winuser-trackmouseevent"><strong>TrackMouseEvent</strong></a> if it exists, otherwise it emulates it.<br /> | 
| <a href="/windows/desktop/api/winuser/nf-winuser-dragdetect"><strong>DragDetect</strong></a><br /> | Captures the mouse and tracks its movement until the user releases the left button, presses the ESC key, or moves the mouse outside the drag rectangle around the specified point. The width and height of the drag rectangle are specified by the <strong>SM_CXDRAG</strong> and <strong>SM_CYDRAG</strong> values returned by the <a href="/windows/desktop/api/winuser/nf-winuser-getsystemmetrics"><strong>GetSystemMetrics</strong></a> function.<br /> | 
| <a href="/windows/desktop/api/winuser/nf-winuser-getcapture"><strong>GetCapture</strong></a><br /> | Retrieves a handle to the window (if any) that has captured the mouse. Only one window at a time can capture the mouse; this window receives mouse input whether or not the cursor is within its borders. <br /> | 
| <a href="/windows/desktop/api/winuser/nf-winuser-getdoubleclicktime"><strong>GetDoubleClickTime</strong></a><br /> | Retrieves the current double-click time for the mouse. A double-click is a series of two clicks of the mouse button, the second occurring within a specified time after the first. The double-click time is the maximum number of milliseconds that may occur between the first and second click of a double-click. The maximum double-click time is 5000 milliseconds.<br /> | 
| <a href="/windows/desktop/api/winuser/nf-winuser-getmousemovepointsex"><strong>GetMouseMovePointsEx</strong></a><br /> | Retrieves a history of up to 64 previous coordinates of the mouse or pen.<br /> | 
| <a href="/windows/desktop/api/winuser/nf-winuser-mouse_event"><strong>mouse_event</strong></a><br /> | The <a href="/windows/desktop/api/winuser/nf-winuser-mouse_event"><strong>mouse_event</strong></a> function synthesizes mouse motion and button clicks.<br /><blockquote>[!Note]<br />This function has been superseded. Use <a href="/windows/desktop/api/winuser/nf-winuser-sendinput"><strong>SendInput</strong></a> instead.</blockquote><br /> | 
| <a href="/windows/desktop/api/winuser/nf-winuser-releasecapture"><strong>ReleaseCapture</strong></a><br /> | Releases the mouse capture from a window in the current thread and restores normal mouse input processing. A window that has captured the mouse receives all mouse input, regardless of the position of the cursor, except when a mouse button is clicked while the cursor hot spot is in the window of another thread. <br /> | 
| <a href="/windows/desktop/api/winuser/nf-winuser-setcapture"><strong>SetCapture</strong></a><br /> | Sets the mouse capture to the specified window belonging to the current thread.<br /> | 
| <a href="/windows/desktop/api/winuser/nf-winuser-setdoubleclicktime"><strong>SetDoubleClickTime</strong></a><br /> | Sets the double-click time for the mouse. A double-click is a series of two clicks of a mouse button, the second occurring within a specified time after the first. The double-click time is the maximum number of milliseconds that may occur between the first and second clicks of a double-click. <br /> | 
| <a href="/windows/desktop/api/winuser/nf-winuser-swapmousebutton"><strong>SwapMouseButton</strong></a><br /> | Reverses or restores the meaning of the left and right mouse buttons. <br /> | 
| <a href="/windows/desktop/api/winuser/nf-winuser-trackmouseevent"><strong>TrackMouseEvent</strong></a><br /> | Posts messages when the mouse pointer leaves a window or hovers over a window for a specified amount of time.<br /><blockquote>[!Note]<br />The <a href="/windows/win32/api/commctrl/nf-commctrl-_trackmouseevent"><strong>_TrackMouseEvent</strong></a> function calls <a href="/windows/desktop/api/winuser/nf-winuser-trackmouseevent"><strong>TrackMouseEvent</strong></a> if it exists, otherwise <strong>_TrackMouseEvent</strong> emulates <strong>TrackMouseEvent</strong>.</blockquote><br /> | 




 

 

