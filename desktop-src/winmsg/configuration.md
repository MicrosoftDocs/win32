---
description: This reference section describes configuration for Windows and Messages. Learn about display elements and system metrics.
ms.assetid: aba21473-07cc-4de9-a310-ad9b43c133eb
title: Configuration (Windows and Messages)
ms.topic: article
ms.date: 05/31/2018
---

# Configuration (Windows and Messages)

*Display elements* are the parts of a window and the display that appear on the system display screen. *System metrics* are the dimensions of various display elements. Typical system metrics include the window border width, icon height, and so on. System metrics also describe other aspects of the system, such as whether a mouse is installed, double-byte characters are supported, or a debugging version of the operating system is installed. The [**GetSystemMetrics**](/windows/win32/api/winuser/nf-winuser-getsystemmetrics) function retrieves the specified system metric.

Applications can also retrieve and set the color of window elements such as menus, scroll bars, and buttons by using the [**GetSysColor**](/windows/desktop/api/winuser/nf-winuser-getsyscolor) and [**SetSysColors**](/windows/desktop/api/winuser/nf-winuser-setsyscolors) functions, respectively.

The [**SystemParametersInfo**](/windows/win32/api/winuser/nf-winuser-systemparametersinfoa) function retrieves or sets various system attributes, such as double-click time, screen saver time-out, window border width, and desktop pattern. When an application uses **SystemParametersInfo** to set a parameter, the change takes place immediately. This function also enables applications to update the user profile, so changes to the system will be preserved when the system is restarted.

 

 
