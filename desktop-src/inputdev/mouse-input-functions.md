---
title: Mouse Input Functions
description: .
ms.assetid: a666b25b-a75c-4500-8077-fabe07589a1d
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Mouse Input Functions

## 

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
<td><a href="https://msdn.microsoft.com/en-us/library/ms646266(v=VS.85).aspx"><strong>_TrackMouseEvent</strong></a><br/></td>
<td>Posts messages when the mouse pointer leaves a window or hovers over a window for a specified amount of time. This function calls <a href="https://msdn.microsoft.com/en-us/library/ms646265(v=VS.85).aspx"><strong>TrackMouseEvent</strong></a> if it exists, otherwise it emulates it.<br/></td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/en-us/library/ms646256(v=VS.85).aspx"><strong>DragDetect</strong></a><br/></td>
<td>Captures the mouse and tracks its movement until the user releases the left button, presses the ESC key, or moves the mouse outside the drag rectangle around the specified point. The width and height of the drag rectangle are specified by the <strong>SM_CXDRAG</strong> and <strong>SM_CYDRAG</strong> values returned by the <a href="https://msdn.microsoft.com/library/windows/desktop/ms724385"><strong>GetSystemMetrics</strong></a> function.<br/></td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/en-us/library/ms646257(v=VS.85).aspx"><strong>GetCapture</strong></a><br/></td>
<td>Retrieves a handle to the window (if any) that has captured the mouse. Only one window at a time can capture the mouse; this window receives mouse input whether or not the cursor is within its borders. <br/></td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/en-us/library/ms646258(v=VS.85).aspx"><strong>GetDoubleClickTime</strong></a><br/></td>
<td>Retrieves the current double-click time for the mouse. A double-click is a series of two clicks of the mouse button, the second occurring within a specified time after the first. The double-click time is the maximum number of milliseconds that may occur between the first and second click of a double-click. The maximum double-click time is 5000 milliseconds.<br/></td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/en-us/library/ms646259(v=VS.85).aspx"><strong>GetMouseMovePointsEx</strong></a><br/></td>
<td>Retrieves a history of up to 64 previous coordinates of the mouse or pen.<br/></td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/en-us/library/ms646260(v=VS.85).aspx"><strong>mouse_event</strong></a><br/></td>
<td>The <a href="https://msdn.microsoft.com/en-us/library/ms646260(v=VS.85).aspx"><strong>mouse_event</strong></a> function synthesizes mouse motion and button clicks.<br/>
<blockquote>
[!Note]<br />
This function has been superseded. Use <a href="https://msdn.microsoft.com/en-us/library/ms646310(v=VS.85).aspx"><strong>SendInput</strong></a> instead.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/en-us/library/ms646261(v=VS.85).aspx"><strong>ReleaseCapture</strong></a><br/></td>
<td>Releases the mouse capture from a window in the current thread and restores normal mouse input processing. A window that has captured the mouse receives all mouse input, regardless of the position of the cursor, except when a mouse button is clicked while the cursor hot spot is in the window of another thread. <br/></td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/en-us/library/ms646262(v=VS.85).aspx"><strong>SetCapture</strong></a><br/></td>
<td>Sets the mouse capture to the specified window belonging to the current thread.<br/></td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/en-us/library/ms646263(v=VS.85).aspx"><strong>SetDoubleClickTime</strong></a><br/></td>
<td>Sets the double-click time for the mouse. A double-click is a series of two clicks of a mouse button, the second occurring within a specified time after the first. The double-click time is the maximum number of milliseconds that may occur between the first and second clicks of a double-click. <br/></td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/en-us/library/ms646264(v=VS.85).aspx"><strong>SwapMouseButton</strong></a><br/></td>
<td>Reverses or restores the meaning of the left and right mouse buttons. <br/></td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/en-us/library/ms646265(v=VS.85).aspx"><strong>TrackMouseEvent</strong></a><br/></td>
<td>Posts messages when the mouse pointer leaves a window or hovers over a window for a specified amount of time.<br/>
<blockquote>
[!Note]<br />
The <a href="https://msdn.microsoft.com/en-us/library/ms646266(v=VS.85).aspx"><strong>_TrackMouseEvent</strong></a> function calls <a href="https://msdn.microsoft.com/en-us/library/ms646265(v=VS.85).aspx"><strong>TrackMouseEvent</strong></a> if it exists, otherwise <strong>_TrackMouseEvent</strong> emulates <strong>TrackMouseEvent</strong>.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

 

 





