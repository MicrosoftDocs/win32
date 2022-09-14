---
description: The following functions provide support for multiple monitors.
ms.assetid: a64b256c-e7a1-4ee2-a346-4b7abcab9e90
title: Multiple Display Monitors Functions
ms.topic: article
ms.date: 05/31/2018
---

# Multiple Display Monitors Functions

The following functions provide support for multiple monitors.



| Function                                           | Description                                                                                                                                                  |
|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EnumDisplayMonitors**](/windows/desktop/api/Winuser/nf-winuser-enumdisplaymonitors) | Enumerates display monitors that intersect a region formed by the intersection of a specified clipping rectangle and the visible region of a device context. |
| [**GetMonitorInfo**](/windows/desktop/api/Winuser/nf-winuser-getmonitorinfoa)           | Retrieves information about a display monitor.                                                                                                               |
| [**MonitorEnumProc**](/windows/desktop/api/Winuser/nc-winuser-monitorenumproc)         | An application-defined callback function that is called by the [**EnumDisplayMonitors**](/windows/desktop/api/Winuser/nf-winuser-enumdisplaymonitors) function.                                  |
| [**MonitorFromPoint**](/windows/desktop/api/Winuser/nf-winuser-monitorfrompoint)       | Retrieves a handle to the display monitor that contains a specified point.                                                                                   |
| [**MonitorFromRect**](/windows/desktop/api/Winuser/nf-winuser-monitorfromrect)         | Retrieves a handle to the display monitor that has the largest area of intersection with a specified rectangle.                                              |
| [**MonitorFromWindow**](/windows/desktop/api/Winuser/nf-winuser-monitorfromwindow)     | Retrieves a handle to the display monitor that has the largest area of intersection with the bounding rectangle of a specified window.                       |



 

 

 



