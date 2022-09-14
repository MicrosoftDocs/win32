---
title: High DPI
description: High DPI
ms.assetid: 476fe65c-2acd-4a7a-8a76-72d9f010b772
ms.topic: article
ms.date: 05/31/2018
---

# High DPI

As display technologies advance, manufacturers have increased the number of pixels supported by their displays. While text, images, and user interface elements look much sharper and more readable on high resolution displays, the operating system must scale up to support the visual experience; otherwise, everything just looks smaller.

Windows 7 supports high *DPI* displays. Market data suggests that deployments of high *DPI* screens (120-144 dots per inch (dpi)) will increase in the Windows 7 timeframe. When running native resolutions on these screens, many applications appear very small unless they use *High DPI*. Some applications (such as Windows Internet Explorer) have font scaling features that allow users to zoom in and out, but many applications do not. The *High DPI* feature in Windows 7:

-   Ensures that Windows and application experiences are optimal on standard hardware (*DPI* settings are optimized to match the capabilities of the hardware).
-   Enables the Windows Shell and other Windows-based applications to look good with different *DPI* settings.
-   Respects default *DPI* settings based on hardware specifications and capabilities.
-   Enables users to personalize *DPI* settings without rebooting.
-   Ensures the screen is always set to native resolution.

The Windows*DPI* scaling feature scales fonts and user interface elements (such as buttons, icons, and input fields) by a calculated percentage, as specified by the *DPI* setting. This is different from the scaling that occurs when the display resolution is lowered. In the case of *DPI* scaling, Windows provides fonts and user interface elements that are drawn with more pixels, resulting in a larger, higher fidelity, and sharper Windows experience. Third-party Windows applications can leverage *High DPI* settings and adjust the user interface accordingly, by declaring themselves *High DPI* aware. Application developers should no longer assume that 96 dpi is the ideal resolution for all applications.

For more information about *High DPI* and about writing applications that are *High DPI* aware, see [High DPI](../hidpi/high-dpi-desktop-application-development-on-windows.md).

 

 
