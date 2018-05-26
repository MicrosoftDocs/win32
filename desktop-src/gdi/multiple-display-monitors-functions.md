---
Description: The following functions provide support for multiple monitors.
ms.assetid: a64b256c-e7a1-4ee2-a346-4b7abcab9e90
title: Multiple Display Monitors Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Multiple Display Monitors Functions

The following functions provide support for multiple monitors.



| Function                                           | Description                                                                                                                                                  |
|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EnumDisplayMonitors**](/windows/win32/Winuser/nf-winuser-enumdisplaymonitors?branch=master) | Enumerates display monitors that intersect a region formed by the intersection of a specified clipping rectangle and the visible region of a device context. |
| [**GetMonitorInfo**](/windows/win32/Winuser/nf-winuser-getmonitorinfoa?branch=master)           | Retrieves information about a display monitor.                                                                                                               |
| [**MonitorEnumProc**](/windows/win32/Winuser/nc-winuser-monitorenumproc?branch=master)         | An application-defined callback function that is called by the [**EnumDisplayMonitors**](/windows/win32/Winuser/nf-winuser-enumdisplaymonitors?branch=master) function.                                  |
| [**MonitorFromPoint**](/windows/win32/Winuser/nf-winuser-monitorfrompoint?branch=master)       | Retrieves a handle to the display monitor that contains a specified point.                                                                                   |
| [**MonitorFromRect**](/windows/win32/Winuser/nf-winuser-monitorfromrect?branch=master)         | Retrieves a handle to the display monitor that has the largest area of intersection with a specified rectangle.                                              |
| [**MonitorFromWindow**](/windows/win32/Winuser/nf-winuser-monitorfromwindow?branch=master)     | Retrieves a handle to the display monitor that has the largest area of intersection with the bounding rectangle of a specified window.                       |



 

 

 



