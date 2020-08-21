---
title: Opening and Closing Mixer Devices
description: Opening and Closing Mixer Devices
ms.assetid: b1943308-3778-485e-80f3-6d80cb583e00
keywords:
- multimedia audio,opening mixer devices
- audio,opening mixer devices
- audio mixers,opening
- mixers,opening
- multimedia audio,closing mixer devices
- audio,closing mixer devices
- audio mixers,closing
- mixers,closing
- opening mixer devices
- closing mixer devices
- device identifiers vs. device handles
- audio mixers,device identifiers vs. device handles
- mixers,device identifiers vs. device handles
ms.topic: article
ms.date: 05/31/2018
---

# Opening and Closing Mixer Devices

When you want to use a mixer device, you can either simply begin using it or you can explicitly open the device before using it. Explicitly opening a mixer device offers two main benefits:

-   It guarantees the continued existence of that mixer device.
-   It lets you receive notification of audio line and control changes.

You can use the [**mixerOpen**](/windows/win32/api/mmeapi/nf-mmeapi-mixeropen) function to explicitly open a mixer device. This function takes as parameters a device identifier, a pointer to a memory location, and other values unique to each type of device. The memory location is filled with a device handle. Use this device handle to identify the open mixer device when calling other audio mixer functions. As long as a handle of a mixer device exists, the device continues to exist in the system. If a configuration change occurs to the mixer device and it hasn't been explicitly opened, your application might suddenly be unable to access it.

> [!Note]  
> The difference between device identifiers and device handles is important. Device handles are returned when you open a device driver by using **mixerOpen**. Device identifiers are determined implicitly from the number of devices present in a system; this number is obtained by using the [**mixerGetNumDevs**](/windows/win32/api/mmeapi/nf-mmeapi-mixergetnumdevs) function.

 

You can use the [**mixerClose**](/windows/win32/api/mmeapi/nf-mmeapi-mixerclose) function to close a mixer device. You should close the device after you finish using it.

 

 