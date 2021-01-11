---
description: About Video Capture Devices
ms.assetid: 1bf6e64f-c3cf-45a4-9f87-1b8cf503d98b
title: About Video Capture Devices
ms.topic: article
ms.date: 05/31/2018
---

# About Video Capture Devices

Most new video capture devices use Windows Driver Model (WDM) drivers. In the WDM architecture, Microsoft supplies a set of hardware-independent drivers, called class drivers, and the hardware vendor provides hardware-specific minidrivers. A minidriver implements any functions that are specific to the device; for most functions, the minidriver calls the Microsoft class driver.

In a DirectShow filter graph, any WDM capture device appears as the [WDM Video Capture](wdm-video-capture-filter.md) filter. The WDM Video Capture filter configures itself based on the characteristics of the driver. It appears under a name provided by the driver — you will not see a filter called "WDM Video Capture Filter" anywhere in the graph.

Some older capture devices still use Video for Windows (VFW) drivers. Although these drivers are now obsolete, they are supported in DirectShow through the [VFW Capture](vfw-capture-filter.md) filter.

## Related topics

<dl> <dt>

[About Video Capture in DirectShow](about-video-capture-in-directshow.md)
</dt> </dl>

 

 



