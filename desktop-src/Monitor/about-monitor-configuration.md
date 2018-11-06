---
title: About Monitor Configuration
description: About Monitor Configuration
ms.assetid: 66345021-41e8-429a-bbf7-a4aa72a57337
keywords:
- monitor,about
- monitor,color calibration
- monitor,adjusting monitor display area
- monitor,saving monitor settings
- monitor,restoring monitor settings
- monitor,vendor features
- color calibration
- adjusting monitor display area
- saving monitor settings
- restoring monitor settings
- vendor features
- monitor configuration,color calibration
- monitor configuration,about
- monitor configuration,adjusting monitor display area
- monitor configuration,saving monitor settings
- monitor configuration,restoring monitor settings
- monitor configuration,vendor features
ms.topic: article
ms.date: 05/31/2018
---

# About Monitor Configuration

Uses for the monitor configuration functions include:

-   Color calibration. A properly calibrated monitor reproduces colors correctly. Typically, a color calibration application displays a test pattern and has controls to change a monitor setting. The user changes the setting until a condition is met, and repeats this process for each monitor setting until the monitor is calibrated.
-   Adjusting the monitor's display area. The monitor configuration functions can be used to change the size and position of a monitor's display area. For example, when an LCD monitor is connected to a computer by using an analog connector, the best image quality is obtained when there is a one-to-one mapping between pixels in the graphics card's frame buffer and pixels on the LCD monitor.
-   Saving and restoring monitor settings. Some users need multiple sets of monitor settings, because different scenarios require different monitor settings. For example, monitor settings that are optimal for desktop applications are not optimal for watching television.
-   Using vendor-specific monitor features. Using the monitor configuration functions, manufacturers can create applications that use the vendor-specific features of the monitor.

The monitor configuration functions are divided into high-level and low-level functions. The high-level functions are easier to use than the low-level functions. To use the high-level functions, you do not need to know anything about the Display Data Channel Command Interface (DDC/CI). However, the high-level functions do not give you access to vendor-specific features of the monitor.

The low-level functions are a thin wrapper around the DDC/CI commands. To use the low-level functions, you must be familiar with the DDC/CI standard and also with the VESA Monitor Control Command Set (MCCS) standard. Generally, you should use the high-level functions unless you need to use features that are available only in the low-level functions.

The high-level monitor configuration functions are designed so that an application cannot put a monitor into an unusable state. The low-level functions can be used to send VCP codes to the monitor. However, be aware that some VCP codes can disable important functionality or put the monitor into a state where the user cannot see the display image. For more information, see the VESA Monitor Control Command Set (MCCS) standard.

## Related topics

<dl> <dt>

[Monitor Configuration](monitor-configuration.md)
</dt> </dl>

 

 




