---
title: Desktop Window Manager
description: The desktop composition feature, introduced in Windows Vista, fundamentally changed the way applications display pixels on the screen.
ms.assetid: VS|winui|~\winui\desktopwindowmanager\overviews\dwm_overview.htm
keywords:
- Desktop Window Manager (DWM),about
- DWM (Desktop Window Manager),about
- Desktop Window Manager (DWM),composition
- DWM (Desktop Window Manager),composition
- desktop composition
- composition
ms.topic: article
ms.date: 05/31/2018
---

# Desktop Window Manager

The desktop composition feature, introduced in Windows Vista, fundamentally changed the way applications display pixels on the screen. When desktop composition is enabled, individual windows no longer draw directly to the screen or primary display device as they did in previous versions of Windows. Instead, their drawing is redirected to off-screen surfaces in video memory, which are then rendered into a desktop image and presented on the display.

Desktop composition is performed by the Desktop Window Manager (DWM). Through desktop composition, DWM enables visual effects on the desktop as well as various features such as glass window frames, 3-D window transition animations, Windows Flip and Windows Flip3D, and high resolution support.

The Desktop Window Manager runs as a Windows service. It can be enabled and disabled through the Administrative Tools Control Panel item, under Services, as Desktop Window Manager Session Manager.

Many of the DWM features can be controlled or accessed by an application through the DWM APIs. The following documentation describes the features and requirements of the DWM APIs.

-   [DWM Overviews](desktop-window-manager-overviews.md)
-   [DWM Sample Code](dwm-samples.md)
-   [DWM Reference](reference.md)

 

 




