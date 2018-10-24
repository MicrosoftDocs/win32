---
Description: The GetSystemMetrics function returns values for the primary monitor, except for SM\_CXMAXTRACK and SM\_CYMAXTRACK, which refer to the entire desktop.
ms.assetid: d0105363-1895-4e10-8a33-648a6fc4c20a
title: Multiple Monitor System Metrics
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Multiple Monitor System Metrics

The [**GetSystemMetrics**](https://msdn.microsoft.com/library/ms724385(v=VS.85).aspx) function returns values for the primary monitor, except for SM\_CXMAXTRACK and SM\_CYMAXTRACK, which refer to the entire desktop. The following metrics are the same for all device drivers: SM\_CXCURSOR, SM\_CYCURSOR, SM\_CXICON, SMCYICON. The following display capabilities are the same for all monitors: LOGPIXELSX, LOGPIXELSY, DESTOPHORZRES, DESKTOPVERTRES.

[**GetSystemMetrics**](https://msdn.microsoft.com/library/ms724385(v=VS.85).aspx) also has constants that refer only to a Multiple Monitor system. SM\_XVIRTUALSCREEN and SM\_YVIRTUALSCREEN identify the upper-left corner of the virtual screen, SM\_CXVIRTUALSCREEN and SM\_CYVIRTUALSCREEN are the vertical and horizontal measurements of the virtual screen, SM\_CMONITORS is the number of monitors attached to the desktop, and SM\_SAMEDISPLAYFORMAT indicates whether all the monitors on the desktop have the same color format.

To get information about a single display monitor or all of the display monitors in a desktop, use EnumDisplayMonitors. The rectangle of the desktop window returned by [**GetWindowRect**](https://msdn.microsoft.com/library/ms633519(v=VS.85).aspx) or [**GetClientRect**](https://msdn.microsoft.com/library/ms633503(v=VS.85).aspx) is always equal to the rectangle of the primary monitor, for compatibility with existing applications. Thus, the result of


```C++
GetWindowRect(GetDesktopWindow(), &rc);
```



will be:


```C++
rc.left = 0; 
rc.top = 0; 
rc.right = GetSystemMetrics (SM_CXSCREEN); 
rc.bottom = GetSystemMetrics (SM_CYSCREEN);
```



To change the work area of a monitor, call [**SystemParametersInfo**](https://msdn.microsoft.com/library/ms724947(v=VS.85).aspx) with SPI\_SETWORKAREA and *pvParam* pointing to a [**RECT**](https://msdn.microsoft.com/en-us/library/Dd162897(v=VS.85).aspx) structure that is on the desired monitor. If *pvParam* is **NULL**, the work area of the primary monitor is modified. Using SPI\_GETWORKAREA always returns the work area of the primary monitor. To get the work area of a monitor other than the primary monitor, call [**GetMonitorInfo**](/windows/desktop/api/Winuser/nf-winuser-getmonitorinfoa).

 

 



