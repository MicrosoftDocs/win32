---
title: High DPI Reference
description: .
ms.assetid: '07A2D45E-721C-4DA8-82A5-38B2FB94BC6D'
---

# High DPI Reference

## Functions



|                                                                                          |                                                                                                                                                                   |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Topic**                                                                                | **Description**                                                                                                                                                   |
| [**AdjustWindowRectExForDpi**](adjustwindowrectexfordpi.md)                             | A variant of [AdjustWindowRectEx](https://msdn.microsoft.com/library/windows/desktop/ms632667) that returns values scaled to a specific DPI.       |
| [**AreDpiAwarenessContextsEqual**](aredpiawarenesscontextsequal.md)                     | Determines whether two [**DPI\_AWARENESS\_CONTEXT**](dpi-awareness-context.md) values are equivalent.                                                            |
| [**EnableNonClientDpiScaling**](enablenonclientdpiscaling.md)                           | Enables automatic scaling of the non-client area of the specified top-level window.                                                                               |
| [**GetAwarenessFromDpiAwarenessContext**](getawarenessfromdpiawarenesscontext.md)       | Retrieves the [**DPI\_AWARENESS**](dpi-awareness.md) value from a [**DPI\_AWARENESS\_CONTEXT**](dpi-awareness-context.md)                                       |
| [**GetDpiForMonitor**](getdpiformonitor.md)                                             | Queries the DPI information associated with a monitor.                                                                                                            |
| [**GetDpiForSystem**](getdpiforsystem.md)                                               | Returns the system DPI.                                                                                                                                           |
| [**GetDpiForWindow**](getdpiforwindow.md)                                               | Returns the current DPI for the specified window.                                                                                                                 |
| [**GetProcessDpiAwareness**](getprocessdpiawareness.md)                                 | Retrieves the DPI virtualization mode of the specified process.                                                                                                   |
| [**GetSystemMetricsForDpi**](getsystemmetricsfordpi.md)                                 | A variant of [GetSystemMetrics](https://msdn.microsoft.com/library/windows/desktop/ms724385) that returns values scaled to a specific DPI.         |
| [**GetThreadDpiAwarenessContext**](getthreaddpiawarenesscontext.md)                     | Retrieves the active DPI awareness context for the current thread.                                                                                                |
| [**GetWindowDpiAwarenessContext**](getwindowdpiawarenesscontext.md)                     | Retrieves the DPI awareness context for a window.                                                                                                                 |
| [**IsValidDpiAwarenessContext**](isvaliddpiawarenesscontext.md)                         | Determines if a [**DPI\_AWARENESS\_CONTEXT**](dpi-awareness-context.md) is valid and supported by the current system.                                            |
| [**LogicalToPhysicalPointForPerMonitorDPI**](logicaltophysicalpointforpermonitordpi.md) | Converts a point in a window from logical coordinates into physical coordinates, regardless of the DPI awareness of the caller.                                   |
| [**PhysicalToLogicalPointForPerMonitorDPI**](physicaltologicalpointforpermonitordpi.md) | Converts a point in a window from physical coordinates into logical coordinates, regardless of the DPI awareness of the caller.                                   |
| [**SetProcessDpiAwareness**](setprocessdpiawareness.md)                                 | Sets the DPI virtualization mode for the current process.                                                                                                         |
| [**SetThreadDpiAwarenessContext**](setthreaddpiawarenesscontext.md)                     | Changes the active DPI awareness context for the current thread.                                                                                                  |
| [**SystemParametersInfoForDpi**](systemparametersinfofordpi.md)                         | A variant of [SystemParametersInfo](https://msdn.microsoft.com/library/windows/desktop/ms724947) that returns values scaled to a specific DPI.     |
| [**SetProcessDpiAwarenessContext**](setprocessdpiawarenesscontext.md)                   | Sets the DPI awareness context for the current process.                                                                                                           |
| [**SetDialogDpiChangeBehavior**](setdialogdpichangebehavior.md)                         | Overrides the default per-monitor DPI scaling behavior of a dialog.                                                                                               |
| [**GetDialogDpiChangeBehavior**](getdialogdpichangebehavior.md)                         | Retrieves the per-monitor DPI scaling behavior of a dialog.                                                                                                       |
| [**SetDialogControlDpiChangeBehavior**](setdialogresizebehavior.md)                     | Overrides the default per-monitor DPI scaling behavior of a child window in a dialog.                                                                             |
| [**GetDialogControlDpiChangeBehavior**](getdialogresizebehavior.md)                     | Retrieves any per-monitor DPI scaling behavior overrides of a child window in a dialog.                                                                           |
| [**OpenThemeDataForDpi**](openthemedatafordpi.md)                                       | A variant of [OpenThemeData](https://msdn.microsoft.com/library/windows/desktop/bb759821) that opens theme handles associated with a specific DPI. |
| [**GetSystemDpiForProcess**](getsystemdpiforprocess.md)                                 | Retrieves the system DPI associated with a given process.                                                                                                         |
| [**GetDpiFromDpiAwarenessContext**](getdpifromdpiawarenesscontext.md)                   | Retrieves the DPI from a given [DPI\_AWARENESS\_CONTEXT](dpi-awareness-context.md) handle.                                                                       |
| [**SetThreadDpiHostingBehavior**](setthreaddpihostingbehavior.md)                       | Overrides the default DPI hosting behavior of the current thread.                                                                                                 |
| [**GetThreadDpiHostingBehavior**](getthreaddpihostingbehavior.md)                       | Retrieves the DPI hosting behavior of the current thread.                                                                                                         |
| [**GetWindowDpiHostingBehavior**](getwindowdpihostingbehavior.md)                       | Retrieves the DPI hosting behavior of the specified window.                                                                                                       |



 

## Types



|                                                                            |                                                                                        |
|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| **Topic**                                                                  | **Description**                                                                        |
| [**DPI\_AWARENESS**](dpi-awareness.md)                                    | Represents DPI coordinate virtualization modes.                                        |
| [**DPI\_AWARENESS\_CONTEXT**](dpi-awareness-context.md)                   | A token which represents a DPI virtualization mode and associated behaviors.           |
| [**DIALOG\_CONTROL\_DPI\_CHANGE\_BEHAVIORS**](dialog-scaling-behavior.md) | Describes per-monitor DPI scaling behavior overrides for child windows within dialogs. |
| [**DIALOG\_DPI\_CHANGE\_BEHAVIORS**](dialog-dpi-change-behaviors.md)      | Describes per-monitor DPI scaling behavior overrides for dialogs.                      |
| [**MONITOR\_DPI\_TYPE**](monitor-dpi-type-enumeration.md)                 | Represents the type of DPI associated with a monitor.                                  |
| [**PROCESS\_DPI\_AWARENESS**](process-dpi-awareness.md)                   | Represents the DPI coordinate virtualization mode of a process.                        |
| [**DPI\_HOSTING\_BEHAVIOR**](-dpi-hosting-behavior.md)                    | Represents the DPI hosting behavior for a window.                                      |



 

## Messages



|                                                                    |                                                                                                                                         |
|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **Topic**                                                          | **Description**                                                                                                                         |
| [**WM\_DPICHANGED**](wm-dpichanged.md)                            | Notifies a top-level window that its DPI has changed.                                                                                   |
| [**WM\_DPICHANGED\_BEFOREPARENT**](wm-dpichanged-beforeparent.md) | Notifies a child window that the DPI associated with its containing window has changed. Delivered before the parent window is notified. |
| [**WM\_DPICHANGED\_AFTERPARENT**](wm-dpichanged-afterparent.md)   | Notifies a child window that the DPI associated with its containing window has changed. Delivered after the parent window is notified.  |
| [**WM\_GETDPISCALEDSIZE**](wm-getdpiscaledsize.md)                | Allows top-level windows to resize *non-linearly* in response to DPI changes.                                                           |



 

 

 




