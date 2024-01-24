---
description: The backlight control interface is a standardized IOCTL interface for controlling the brightness of the LCD backlight.
ms.assetid: edf2b7ed-2676-483a-80ba-f148951e0e58
title: Backlight Control Interface
ms.topic: article
ms.date: 05/31/2018
---

# Backlight Control Interface

The backlight control interface is a standardized IOCTL interface for controlling the brightness of the LCD backlight.

Applications that require programmatic control of the backlight brightness or provide controls for the user to do so should use this interface rather than a proprietary interface; otherwise, the system cannot query the current hardware brightness and may become unsynchronized.

The first step is to query the device for the supported brightness using the [**IOCTL\_VIDEO\_QUERY\_SUPPORTED\_BRIGHTNESS**](ioctl-video-query-supported-brightness.md) control code. This operation returns a buffer that specifies the available brightness levels. Next, you can query the device for the current display brightness using the [**IOCTL\_VIDEO\_QUERY\_DISPLAY\_BRIGHTNESS**](ioctl-video-query-display-brightness.md) control code. This operation returns the current settings for alternating current (AC) brightness, direct current (DC) brightness, and the power state.

To change the display brightness, use the [**IOCTL\_VIDEO\_SET\_DISPLAY\_BRIGHTNESS**](ioctl-video-set-display-brightness.md) control code. You can set the AC brightness, the DC brightness, or both.

## Related topics

<dl> <dt>

[About Power Management](about-power-management.md)
</dt> </dl>

 

 



