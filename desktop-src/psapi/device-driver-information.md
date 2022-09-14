---
title: Device Driver Information
description: Device drivers and modules are similar in that they are both based on PE files.
ms.assetid: 4f4ec15b-5592-4fe3-b754-fda25ab24159
ms.topic: article
ms.date: 05/31/2018
---

# Device Driver Information

Device drivers and modules are similar in that they are both based on PE files. However, while each process has its own private list of loaded modules, device drivers have modules that are global to the system. Therefore, PSAPI has specific functions for obtaining the list of device drivers and their names.

You can retrieve the load address for each device driver by calling the [**EnumDeviceDrivers**](/windows/desktop/api/Psapi/nf-psapi-enumdevicedrivers) function. This function fills an array of **LPVOID** values with the load addresses of all device drivers in the system.

The [**GetDeviceDriverBaseName**](/windows/desktop/api/Psapi/nf-psapi-getdevicedriverbasenamea) function takes a driver load address as input and fills in a buffer with the base name of the driver (for example, Win32k.sys). A related function, [**GetDeviceDriverFileName**](/windows/desktop/api/Psapi/nf-psapi-getdevicedriverfilenamea), takes the same parameters and returns the path to the device driver (for example, C:\\Windows\\System32\\Win32k.sys).

 

 




