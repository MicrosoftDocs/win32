---
Description: A window or menu that is on more than one monitor causes visual disruption for a viewer. To minimize this problem, the system displays menus and new and maximized windows on one monitor. The following table shows how the monitor is chosen.
ms.assetid: 9316c8dd-c9b7-49e2-a987-5949a87b0cfc
title: Positioning Objects on Multiple Display Monitors
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Positioning Objects on Multiple Display Monitors

A window or menu that is on more than one monitor causes visual disruption for a viewer. To minimize this problem, the system displays menus and new and maximized windows on one monitor. The following table shows how the monitor is chosen.



| Object         | Location                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| window         | [**CreateWindow**](_win32_createwindow_cpp)(Ex) displays a window on the monitor that contains the largest part of the window.Maximizes on the monitor that contains the largest part of the window before it was minimized.<br/> The ALT-TAB key combination displays a window on the monitor that has the currently active window.<br/>                                                                                                                                          |
| owned window   | on the same monitor as its owner.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| submenu        | Appears on the monitor that contains the largest part of the corresponding menu item.                                                                                                                                                                                                                                                                                                                                                                                                          |
| context menu   | Appears on the monitor where the right click occurred.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| drop-down list | Appears on the monitor that contains the rectangle of the combo box.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| dialog box     | Appears on the monitor of the window that owns it.If it is defined with DS\_CENTERMOUSE style, it appears on the monitor with the mouse.<br/> If it has no owner and the active window and the dialog box are in the same application, the dialog box appears on the monitor of the currently active window.<br/> If the dialog box has no owner and the active window is not in the same application as the dialog box, the dialog box appears on the primary monitor.<br/> |
| message box    | Appears on the monitor of the window that owns it.                                                                                                                                                                                                                                                                                                                                                                                                                                             |



 

If a window straddles two monitors and one of the monitors is repositioned, the system positions the window on the monitor that contains the largest part of the original window.

An application will also typically need to position objects. For example, a window may need to be created on the same monitor as another window.

**To position an object on a multiple monitor system**

1.  Determine the appropriate monitor.
2.  Get the coordinates to the monitor.
3.  Position the object using the coordinates.

Typically, you will position an object either on the primary monitor or on a monitor that has an object already on it. To identify the monitor for a given point, rectangle, or window, use [**MonitorFromPoint**](/windows/win32/Winuser/nf-winuser-monitorfrompoint?branch=master), [**MonitorFromRect**](/windows/win32/Winuser/nf-winuser-monitorfromrect?branch=master), and [**MonitorFromWindow**](/windows/win32/Winuser/nf-winuser-monitorfromwindow?branch=master).

To get the coordinates for the monitor, use [**GetMonitorInfo**](/windows/win32/Winuser/nf-winuser-getmonitorinfoa?branch=master), which provides both the work area and the entire monitor rectangle. Note that SM\_CXSCREEN and SM\_CYSCREEN always refer to the primary monitor, not necessarily the monitor that displays your application. Also, avoid SM\_xxVIRTUALSCREEN because this centers your window on the virtual screen, not a monitor.

To center dialog boxes in a window's work area, use the DS\_CENTER style. To center the dialog box to an application window, use [**GetWindowRect**](_win32_getwindowrect_cpp). Windows automatically restricts menus and dialog boxes to a monitor. However, there can be a problem for custom menus, custom drop-down boxes, custom tool palettes, and the saved application position.

For an example of how to position objects correctly, see [Positioning Objects on a Multiple Display Setup](positioning-objects-on-a-multiple-display-setup.md).

Using SM\_CXSCREEN and SM\_CYSCREEN to determine the location of an application desktop toolbar (also called *appbar*) restricts the appbar to the primary monitor. To allow an appbar to be on any edge of any monitor, use the appropriate system metrics to calculate the edges of the monitors. Also, use the **GET\_X\_LPARAM** and **GET\_Y\_LPARAM** macros to extract the coordinates, otherwise the sign of the coordinates may be wrong. These macros are included in Windowsx.h.

The size of a full-screen window needs to change as it moves among monitors with different resolutions. To do this, the application must check what window it is on, using [**MonitorFromWindow**](/windows/win32/Winuser/nf-winuser-monitorfromwindow?branch=master) or [**MonitorFromPoint**](/windows/win32/Winuser/nf-winuser-monitorfrompoint?branch=master) , and then use [**GetMonitorInfo**](/windows/win32/Winuser/nf-winuser-getmonitorinfoa?branch=master) to get the size of the monitor. As an alternative, you could use the **HMONITOR** from the DirectX **DirectDrawEnumerateEx** function. Then use [**SetWindowPos**](_win32_setwindowpos_cpp) to position and size the window to cover the monitor.

A maximized window does not cover a taskbar that has the "Always on top" property. However, a full-screen window covers the taskbar--for example, in Microsoft PowerPoint slide shows and games.

To save, and later restore, the position of a window when an application exits, use the [**GetWindowPlacement**](_win32_getwindowplacement_cpp) and [**SetWindowPlacement**](_win32_setwindowplacement_cpp) functions. However, check that the position is still valid before using it because the monitor could have been moved or removed from the system. The application displays the window on the primary monitor if the **HMONITOR** of a window is invalid.

The system tries to start an application on the monitor that contains its shortcut. So, one way to position an application is to have its shortcut on a desired monitor.

If you use [**ShellExecute**](_win32_shellexecute_cpp) or [**ShellExecuteEx**](_win32_ShellExecuteEx_cpp) , supply an *hWnd* so the system will open any new windows on the same monitor as the calling application.

Note that the values for the [**MINMAXINFO**](_win32_minmaxinfo_str_cpp) structure are slightly altered for a system with multiple monitors.

 

 




