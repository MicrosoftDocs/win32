---
description: When multiple monitors are part of the desktop, objects can travel seamlessly between monitors.
ms.assetid: eb7576c6-322c-48d0-abbb-bdc3b34976c3
title: About Multiple Display Monitors
ms.topic: article
ms.date: 05/31/2018
---

# About Multiple Display Monitors

When multiple monitors are part of the desktop, objects can travel seamlessly between monitors. That is, you can drag windows or shortcuts from one monitor to another, and you can size windows to cover more than one monitor. Also, if one monitor is installed above another, a cursor that leaves the bottom of the upper monitor appears at the top of the lower monitor.

Typically, a user arranges the monitors in the system to reflect the arrangement of the physical display units; for example, side-by-side or one-on-top-of-the-other. The user does this with the Monitors tab, which replaces the **Settings** tab in the **Display Properties** dialog box through Control Panel. The monitors must form one contiguous region, that is, each monitor touches another monitor on at least part of one edge.

When a window is moved or resized, some part of the caption is always visible so the user can move and resize the window using the mouse. Cursor movement is restricted to the area of the monitors, so it is always visible. Shell icons are positioned on the same monitor as the taskbar, and the taskbar can be on any monitor, see [Multiple Monitor Considerations for Older Programs](multiple-monitor-considerations-for-older-programs.md).

A multiple monitor system affects certain key combinations. The ALT+PRINTSCRN key combination takes a snapshot of the foreground window, as always. However, the PRINTSCRN key takes a snapshot of the monitor that has the mouse. The CTRL+PRINTSCRN key combination takes a snapshot of the entire virtual screen, see [The Virtual Screen](the-virtual-screen.md).

The support for multiple monitors does not affect the performance of applications when running in a single display environment. That is, when running on a single display system, no additional overhead will be present in the high-performance graphics operations code. However, in a multiple monitor system, performance is slightly affected if an application runs only on one of the graphics devices. Also, performance may be greatly affected if an application spans multiple displays, especially for graphics-intensive operations.

*Full-screen* is a feature provided by the operating system that allows a user to toggle an application into a special state where the application can access VGA graphics hardware directly. This is a key feature for games and other graphics-focused applications that require high performance. Also, it is often used by developers for text editing since it enables very fast text scrolling.

In a multiple monitor environment, only one graphics device can be VGA compatible. This is a limitation of computer hardware which requires that only one device respond to any hardware address. Because the VGA hardware compatibility standard requires specific hardware addresses, only one VGA graphics device can be present in a machine and only this device can physically respond to VGA addresses. Thus, applications that require going full screen will only run on the particular device that supports VGA hardware compatibility.

This overview provides information on the following topics.

-   [The Virtual Screen](the-virtual-screen.md)
-   [HMONITOR and the Device Context](hmonitor-and-the-device-context.md)
-   [Enumeration and Display Control](enumeration-and-display-control.md)
-   [Multiple Monitor System Metrics](multiple-monitor-system-metrics.md)
-   [Using Multiple Monitors as Independent Displays](using-multiple-monitors-as-independent-displays.md)
-   [Colors on Multiple Display Monitors](colors-on-multiple-display-monitors.md)
-   [Positioning Objects on Multiple Display Monitors](positioning-objects-on-multiple-display-monitors.md)
-   [Multiple Monitor Applications on Different Systems](multiple-monitor-applications-on-different-systems.md)
-   [Multiple Monitor Considerations for Older Programs](multiple-monitor-considerations-for-older-programs.md)

 

 



