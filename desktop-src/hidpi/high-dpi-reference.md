---
title: High DPI Reference
description: .
ms.assetid: 07A2D45E-721C-4DA8-82A5-38B2FB94BC6D
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# High DPI Reference

## Functions



|                                                                                          |                                                                                                                                                                   |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Topic**                                                                                | **Description**                                                                                                                                                   |
| [**AdjustWindowRectExForDpi**](/windows/win32/Winuser/nf-winuser-adjustwindowrectexfordpi?branch=master)                             | A variant of [AdjustWindowRectEx](https://msdn.microsoft.com/library/windows/desktop/ms632667) that returns values scaled to a specific DPI.       |
| [**AreDpiAwarenessContextsEqual**](/windows/win32/Winuser/nf-winuser-aredpiawarenesscontextsequal?branch=master)                     | Determines whether two [**DPI\_AWARENESS\_CONTEXT**](dpi-awareness-context.md) values are equivalent.                                                            |
| [**EnableNonClientDpiScaling**](/windows/win32/Winuser/nf-winuser-enablenonclientdpiscaling?branch=master)                           | Enables automatic scaling of the non-client area of the specified top-level window.                                                                               |
| [**GetAwarenessFromDpiAwarenessContext**](/windows/win32/Winuser/nf-winuser-getawarenessfromdpiawarenesscontext?branch=master)       | Retrieves the [**DPI\_AWARENESS**](/windows/win32/windef/ne-windef-dpi_awareness?branch=master) value from a [**DPI\_AWARENESS\_CONTEXT**](dpi-awareness-context.md)                                       |
| [**GetDpiForMonitor**](/windows/win32/ShellScalingAPI/nf-shellscalingapi-getdpiformonitor?branch=master)                                             | Queries the DPI information associated with a monitor.                                                                                                            |
| [**GetDpiForSystem**](/windows/win32/Winuser/nf-winuser-getdpiforsystem?branch=master)                                               | Returns the system DPI.                                                                                                                                           |
| [**GetDpiForWindow**](/windows/win32/Winuser/nf-winuser-getdpiforwindow?branch=master)                                               | Returns the current DPI for the specified window.                                                                                                                 |
| [**GetProcessDpiAwareness**](/windows/win32/ShellScalingAPI/nf-shellscalingapi-getprocessdpiawareness?branch=master)                                 | Retrieves the DPI virtualization mode of the specified process.                                                                                                   |
| [**GetSystemMetricsForDpi**](/windows/win32/Winuser/nf-winuser-getsystemmetricsfordpi?branch=master)                                 | A variant of [GetSystemMetrics](https://msdn.microsoft.com/library/windows/desktop/ms724385) that returns values scaled to a specific DPI.         |
| [**GetThreadDpiAwarenessContext**](/windows/win32/Winuser/nf-winuser-getthreaddpiawarenesscontext?branch=master)                     | Retrieves the active DPI awareness context for the current thread.                                                                                                |
| [**GetWindowDpiAwarenessContext**](/windows/win32/Winuser/nf-winuser-getwindowdpiawarenesscontext?branch=master)                     | Retrieves the DPI awareness context for a window.                                                                                                                 |
| [**IsValidDpiAwarenessContext**](/windows/win32/Winuser/nf-winuser-isvaliddpiawarenesscontext?branch=master)                         | Determines if a [**DPI\_AWARENESS\_CONTEXT**](dpi-awareness-context.md) is valid and supported by the current system.                                            |
| [**LogicalToPhysicalPointForPerMonitorDPI**](/windows/win32/winuser/nf-winuser-logicaltophysicalpointforpermonitordpi?branch=master) | Converts a point in a window from logical coordinates into physical coordinates, regardless of the DPI awareness of the caller.                                   |
| [**PhysicalToLogicalPointForPerMonitorDPI**](/windows/win32/winuser/nf-winuser-physicaltologicalpointforpermonitordpi?branch=master) | Converts a point in a window from physical coordinates into logical coordinates, regardless of the DPI awareness of the caller.                                   |
| [**SetProcessDpiAwareness**](/windows/win32/ShellScalingAPI/nf-shellscalingapi-setprocessdpiawareness?branch=master)                                 | Sets the DPI virtualization mode for the current process.                                                                                                         |
| [**SetThreadDpiAwarenessContext**](/windows/win32/Winuser/nf-winuser-setthreaddpiawarenesscontext?branch=master)                     | Changes the active DPI awareness context for the current thread.                                                                                                  |
| [**SystemParametersInfoForDpi**](/windows/win32/Winuser/nf-winuser-systemparametersinfofordpi?branch=master)                         | A variant of [SystemParametersInfo](https://msdn.microsoft.com/library/windows/desktop/ms724947) that returns values scaled to a specific DPI.     |
| [**SetProcessDpiAwarenessContext**](/windows/win32/winuser/nf-winuser-setprocessdpiawarenesscontext?branch=master)                   | Sets the DPI awareness context for the current process.                                                                                                           |
| [**SetDialogDpiChangeBehavior**](/windows/win32/winuser/nf-winuser-setdialogdpichangebehavior?branch=master)                         | Overrides the default per-monitor DPI scaling behavior of a dialog.                                                                                               |
| [**GetDialogDpiChangeBehavior**](/windows/win32/winuser/nf-winuser-getdialogdpichangebehavior?branch=master)                         | Retrieves the per-monitor DPI scaling behavior of a dialog.                                                                                                       |
| [**SetDialogControlDpiChangeBehavior**](/windows/win32/winuser/nf-winuser-setdialogcontroldpichangebehavior?branch=master)                     | Overrides the default per-monitor DPI scaling behavior of a child window in a dialog.                                                                             |
| [**GetDialogControlDpiChangeBehavior**](/windows/win32/winuser/nf-winuser-getdialogcontroldpichangebehavior?branch=master)                     | Retrieves any per-monitor DPI scaling behavior overrides of a child window in a dialog.                                                                           |
| [**OpenThemeDataForDpi**](/windows/win32/uxtheme/nf-uxtheme-openthemedatafordpi?branch=master)                                       | A variant of [OpenThemeData](https://msdn.microsoft.com/library/windows/desktop/bb759821) that opens theme handles associated with a specific DPI. |
| [**GetSystemDpiForProcess**](/windows/win32/winuser/nf-winuser-getsystemdpiforprocess?branch=master)                                 | Retrieves the system DPI associated with a given process.                                                                                                         |
| [**GetDpiFromDpiAwarenessContext**](/windows/win32/winuser/nf-winuser-getdpifromdpiawarenesscontext?branch=master)                   | Retrieves the DPI from a given [DPI\_AWARENESS\_CONTEXT](dpi-awareness-context.md) handle.                                                                       |
| [**SetThreadDpiHostingBehavior**](/windows/win32/winuser/nf-winuser-setthreaddpihostingbehavior?branch=master)                       | Overrides the default DPI hosting behavior of the current thread.                                                                                                 |
| [**GetThreadDpiHostingBehavior**](/windows/win32/winuser/nf-winuser-getthreaddpihostingbehavior?branch=master)                       | Retrieves the DPI hosting behavior of the current thread.                                                                                                         |
| [**GetWindowDpiHostingBehavior**](/windows/win32/winuser/nf-winuser-getwindowdpihostingbehavior?branch=master)                       | Retrieves the DPI hosting behavior of the specified window.                                                                                                       |



 

## Types



|                                                                            |                                                                                        |
|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| **Topic**                                                                  | **Description**                                                                        |
| [**DPI\_AWARENESS**](/windows/win32/windef/ne-windef-dpi_awareness?branch=master)                                    | Represents DPI coordinate virtualization modes.                                        |
| [**DPI\_AWARENESS\_CONTEXT**](dpi-awareness-context.md)                   | A token which represents a DPI virtualization mode and associated behaviors.           |
| [**DIALOG\_CONTROL\_DPI\_CHANGE\_BEHAVIORS**](/windows/win32/winuser/ne-winuser-dialog_control_dpi_change_behaviors?branch=master) | Describes per-monitor DPI scaling behavior overrides for child windows within dialogs. |
| [**DIALOG\_DPI\_CHANGE\_BEHAVIORS**](/windows/win32/winuser/ne-winuser-dialog_dpi_change_behaviors?branch=master)      | Describes per-monitor DPI scaling behavior overrides for dialogs.                      |
| [**MONITOR\_DPI\_TYPE**](/windows/win32/ShellScalingApi/ne-shellscalingapi-monitor_dpi_type?branch=master)                 | Represents the type of DPI associated with a monitor.                                  |
| [**PROCESS\_DPI\_AWARENESS**](/windows/win32/ShellScalingApi/ne-shellscalingapi-process_dpi_awareness?branch=master)                   | Represents the DPI coordinate virtualization mode of a process.                        |
| [**DPI\_HOSTING\_BEHAVIOR**](-dpi-hosting-behavior.md)                    | Represents the DPI hosting behavior for a window.                                      |



 

## Messages



|                                                                    |                                                                                                                                         |
|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **Topic**                                                          | **Description**                                                                                                                         |
| [**WM\_DPICHANGED**](wm-dpichanged.md)                            | Notifies a top-level window that its DPI has changed.                                                                                   |
| [**WM\_DPICHANGED\_BEFOREPARENT**](wm-dpichanged-beforeparent.md) | Notifies a child window that the DPI associated with its containing window has changed. Delivered before the parent window is notified. |
| [**WM\_DPICHANGED\_AFTERPARENT**](wm-dpichanged-afterparent.md)   | Notifies a child window that the DPI associated with its containing window has changed. Delivered after the parent window is notified.  |
| [**WM\_GETDPISCALEDSIZE**](wm-getdpiscaledsize.md)                | Allows top-level windows to resize *non-linearly* in response to DPI changes.                                                           |



 

 

 




