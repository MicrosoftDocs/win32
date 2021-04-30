---
title: High DPI Reference
description: High DPI Reference
ms.assetid: 07A2D45E-721C-4DA8-82A5-38B2FB94BC6D
ms.topic: article
ms.date: 05/31/2018
---

# High DPI Reference

## Functions



|                                                                                          |                                                                                                                                                                   |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Topic**                                                                                | **Description**                                                                                                                                                   |
| [**AdjustWindowRectExForDpi**](/windows/desktop/api/Winuser/nf-winuser-adjustwindowrectexfordpi)                             | A variant of [AdjustWindowRectEx](/windows/desktop/api/winuser/nf-winuser-adjustwindowrectex) that returns values scaled to a specific DPI.       |
| [**AreDpiAwarenessContextsEqual**](/windows/desktop/api/Winuser/nf-winuser-aredpiawarenesscontextsequal)                     | Determines whether two [**DPI\_AWARENESS\_CONTEXT**](dpi-awareness-context.md) values are equivalent.                                                            |
| [**EnableNonClientDpiScaling**](/windows/desktop/api/Winuser/nf-winuser-enablenonclientdpiscaling)                           | Enables automatic scaling of the non-client area of the specified top-level window.                                                                               |
| [**GetAwarenessFromDpiAwarenessContext**](/windows/desktop/api/Winuser/nf-winuser-getawarenessfromdpiawarenesscontext)       | Retrieves the [**DPI\_AWARENESS**](/windows/desktop/api/windef/ne-windef-dpi_awareness) value from a [**DPI\_AWARENESS\_CONTEXT**](dpi-awareness-context.md)                                       |
| [**GetDpiForMonitor**](/windows/desktop/api/ShellScalingAPI/nf-shellscalingapi-getdpiformonitor)                                             | Queries the DPI information associated with a monitor.                                                                                                            |
| [**GetDpiForSystem**](/windows/desktop/api/Winuser/nf-winuser-getdpiforsystem)                                               | Returns the system DPI.                                                                                                                                           |
| [**GetDpiForWindow**](/windows/desktop/api/Winuser/nf-winuser-getdpiforwindow)                                               | Returns the current DPI for the specified window.                                                                                                                 |
| [**GetProcessDpiAwareness**](/windows/desktop/api/ShellScalingAPI/nf-shellscalingapi-getprocessdpiawareness)                                 | Retrieves the DPI virtualization mode of the specified process.                                                                                                   |
| [**GetSystemMetricsForDpi**](/windows/desktop/api/Winuser/nf-winuser-getsystemmetricsfordpi)                                 | A variant of [GetSystemMetrics](/windows/desktop/api/winuser/nf-winuser-getsystemmetrics) that returns values scaled to a specific DPI.         |
| [**GetThreadDpiAwarenessContext**](/windows/desktop/api/Winuser/nf-winuser-getthreaddpiawarenesscontext)                     | Retrieves the active DPI awareness context for the current thread.                                                                                                |
| [**GetWindowDpiAwarenessContext**](/windows/desktop/api/Winuser/nf-winuser-getwindowdpiawarenesscontext)                     | Retrieves the DPI awareness context for a window.                                                                                                                 |
| [**IsValidDpiAwarenessContext**](/windows/desktop/api/Winuser/nf-winuser-isvaliddpiawarenesscontext)                         | Determines if a [**DPI\_AWARENESS\_CONTEXT**](dpi-awareness-context.md) is valid and supported by the current system.                                            |
| [**LogicalToPhysicalPointForPerMonitorDPI**](/windows/desktop/api/winuser/nf-winuser-logicaltophysicalpointforpermonitordpi) | Converts a point in a window from logical coordinates into physical coordinates, regardless of the DPI awareness of the caller.                                   |
| [**PhysicalToLogicalPointForPerMonitorDPI**](/windows/desktop/api/winuser/nf-winuser-physicaltologicalpointforpermonitordpi) | Converts a point in a window from physical coordinates into logical coordinates, regardless of the DPI awareness of the caller.                                   |
| [**SetProcessDpiAwareness**](/windows/desktop/api/ShellScalingAPI/nf-shellscalingapi-setprocessdpiawareness)                                 | Sets the DPI virtualization mode for the current process.                                                                                                         |
| [**SetThreadDpiAwarenessContext**](/windows/desktop/api/Winuser/nf-winuser-setthreaddpiawarenesscontext)                     | Changes the active DPI awareness context for the current thread.                                                                                                  |
| [**SystemParametersInfoForDpi**](/windows/desktop/api/Winuser/nf-winuser-systemparametersinfofordpi)                         | A variant of [SystemParametersInfo](/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa) that returns values scaled to a specific DPI.     |
| [**SetProcessDpiAwarenessContext**](/windows/desktop/api/winuser/nf-winuser-setprocessdpiawarenesscontext)                   | Sets the DPI awareness context for the current process.                                                                                                           |
| [**SetDialogDpiChangeBehavior**](/windows/desktop/api/winuser/nf-winuser-setdialogdpichangebehavior)                         | Overrides the default per-monitor DPI scaling behavior of a dialog.                                                                                               |
| [**GetDialogDpiChangeBehavior**](/windows/desktop/api/winuser/nf-winuser-getdialogdpichangebehavior)                         | Retrieves the per-monitor DPI scaling behavior of a dialog.                                                                                                       |
| [**SetDialogControlDpiChangeBehavior**](/windows/desktop/api/winuser/nf-winuser-setdialogcontroldpichangebehavior)                     | Overrides the default per-monitor DPI scaling behavior of a child window in a dialog.                                                                             |
| [**GetDialogControlDpiChangeBehavior**](/windows/desktop/api/winuser/nf-winuser-getdialogcontroldpichangebehavior)                     | Retrieves any per-monitor DPI scaling behavior overrides of a child window in a dialog.                                                                           |
| [**OpenThemeDataForDpi**](/windows/desktop/api/uxtheme/nf-uxtheme-openthemedatafordpi)                                       | A variant of [OpenThemeData](/windows/desktop/api/uxtheme/nf-uxtheme-openthemedata) that opens theme handles associated with a specific DPI. |
| [**GetSystemDpiForProcess**](/windows/desktop/api/winuser/nf-winuser-getsystemdpiforprocess)                                 | Retrieves the system DPI associated with a given process.                                                                                                         |
| [**GetDpiFromDpiAwarenessContext**](/windows/desktop/api/winuser/nf-winuser-getdpifromdpiawarenesscontext)                   | Retrieves the DPI from a given [DPI\_AWARENESS\_CONTEXT](dpi-awareness-context.md) handle.                                                                       |
| [**SetThreadDpiHostingBehavior**](/windows/desktop/api/winuser/nf-winuser-setthreaddpihostingbehavior)                       | Overrides the default DPI hosting behavior of the current thread.                                                                                                 |
| [**GetThreadDpiHostingBehavior**](/windows/desktop/api/winuser/nf-winuser-getthreaddpihostingbehavior)                       | Retrieves the DPI hosting behavior of the current thread.                                                                                                         |
| [**GetWindowDpiHostingBehavior**](/windows/desktop/api/winuser/nf-winuser-getwindowdpihostingbehavior)                       | Retrieves the DPI hosting behavior of the specified window.                                                                                                       |



 

## Types



|                                                                            |                                                                                        |
|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| **Topic**                                                                  | **Description**                                                                        |
| [**DPI\_AWARENESS**](/windows/desktop/api/windef/ne-windef-dpi_awareness)                                    | Represents DPI coordinate virtualization modes.                                        |
| [**DPI\_AWARENESS\_CONTEXT**](dpi-awareness-context.md)                   | A token which represents a DPI virtualization mode and associated behaviors.           |
| [**DIALOG\_CONTROL\_DPI\_CHANGE\_BEHAVIORS**](/windows/desktop/api/winuser/ne-winuser-dialog_control_dpi_change_behaviors) | Describes per-monitor DPI scaling behavior overrides for child windows within dialogs. |
| [**DIALOG\_DPI\_CHANGE\_BEHAVIORS**](/windows/desktop/api/winuser/ne-winuser-dialog_dpi_change_behaviors)      | Describes per-monitor DPI scaling behavior overrides for dialogs.                      |
| [**MONITOR\_DPI\_TYPE**](/windows/desktop/api/ShellScalingApi/ne-shellscalingapi-monitor_dpi_type)                 | Represents the type of DPI associated with a monitor.                                  |
| [**PROCESS\_DPI\_AWARENESS**](/windows/desktop/api/ShellScalingApi/ne-shellscalingapi-process_dpi_awareness)                   | Represents the DPI coordinate virtualization mode of a process.                        |
| [**DPI\_HOSTING\_BEHAVIOR**](/windows/win32/api/windef/ne-windef-dpi_hosting_behavior)                    | Represents the DPI hosting behavior for a window.                                      |



 

## Messages



|                                                                    |                                                                                                                                         |
|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **Topic**                                                          | **Description**                                                                                                                         |
| [**WM\_DPICHANGED**](wm-dpichanged.md)                            | Notifies a top-level window that its DPI has changed.                                                                                   |
| [**WM\_DPICHANGED\_BEFOREPARENT**](wm-dpichanged-beforeparent.md) | Notifies a child window that the DPI associated with its containing window has changed. Delivered before the parent window is notified. |
| [**WM\_DPICHANGED\_AFTERPARENT**](wm-dpichanged-afterparent.md)   | Notifies a child window that the DPI associated with its containing window has changed. Delivered after the parent window is notified.  |
| [**WM\_GETDPISCALEDSIZE**](wm-getdpiscaledsize.md)                | Allows top-level windows to resize *non-linearly* in response to DPI changes.                                                           |



 

 

 
