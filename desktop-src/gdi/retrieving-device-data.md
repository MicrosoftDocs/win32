---
Description: Applications can use the following functions to retrieve device data using a device context GetDeviceCaps and DeviceCapabilities.
ms.assetid: eed6a323-b7eb-41a2-adb9-592f3f912884
title: Retrieving Device Data
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Retrieving Device Data

Applications can use the following functions to retrieve device data using a device context: [**GetDeviceCaps**](/windows/win32/Wingdi/nf-wingdi-getdevicecaps?branch=master) and [**DeviceCapabilities**](gdi.devicecapabilities).

[**GetDeviceCaps**](/windows/win32/Wingdi/nf-wingdi-getdevicecaps?branch=master) retrieves general device data for the following devices:

-   Raster displays
-   Dot-matrix printers
-   Ink-jet printers
-   Laser printers
-   Vector plotters
-   Raster cameras

The data includes the supported capabilities of the device, including device resolution (for video displays), color format (for video displays and color printers), number of graphic objects, raster capabilities, curve drawing, line drawing, polygon drawing, and text drawing. An application retrieves this data by supplying a handle identifying the appropriate device context, as well as an index specifying the type of data the function is to retrieve.

The [**DeviceCapabilities**](gdi.devicecapabilities) function retrieves data specific to printers, including the number of available paper bins, the duplex capabilities of the printer, the resolutions supported by the printer, the maximum and minimum supported paper size, and so on. An application retrieves this data by supplying strings specifying a printer device and port, as well as an index specifying the type of data that the function is to retrieve.

 

 



