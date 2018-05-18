---
title: Providing Status Updates
description: Providing Status Updates
ms.assetid: '0f22c5d5-c85b-411e-a4dd-b7ad768be975'
keywords: ["MCIWndSetActiveTimer macro", "MCIWndSetInactiveTimer macro", "MCIWndGetActiveTimer macro", "MCIWndGetInactiveTimer macro", "MCIWndSetTimers macro"]
---

# Providing Status Updates

MCIWnd uses timers to periodically update information in the window title bar and scroll bar, and to send notification messages to the parent window. One timer controls the update period of the active MCIWnd window, and a second timer controls the update period for MCIWnd windows that are inactive. Your application can use the MCIWnd timer macros to retrieve the current timer settings and to adjust the update periods.

You can set the update period used by the active window timer by using the [**MCIWndSetActiveTimer**](mciwndsetactivetimer.md) macro. This macro sets the period used by MCIWnd to update the trackbar, to update the playback position reported in the window title bar, and to notify the parent window that the media has changed. You can retrieve the current update period used by the active window timer by using the [**MCIWndGetActiveTimer**](mciwndgetactivetimer.md) macro. The default update period for the active window timer is 500 milliseconds.

You can set the update period used by the inactive window timer by using the [**MCIWndSetInactiveTimer**](mciwndsetinactivetimer.md) macro. This macro sets the period used by MCIWnd to update the trackbar, to update the playback position reported in the window caption, and to notify the parent window that the media has changed. You can retrieve the current update period used by the inactive window timer by using the [**MCIWndGetInactiveTimer**](mciwndgetinactivetimer.md) macro. The default update period for the inactive window timer is 2000 milliseconds.

Your application can simultaneously set the update period for both timers by using the [**MCIWndSetTimers**](mciwndsettimers.md) macro. The storage for the value of the update period is limited to 16 bits. If a larger quantity for either update period is needed, set the timers individually.

 

 




