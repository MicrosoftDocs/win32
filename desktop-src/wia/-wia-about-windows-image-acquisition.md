---
description: The Windows Image Acquisition (WIA) interface is both an API and a device driver interface (DDI).
ms.assetid: 725543f8-6e33-4e22-904c-95cbec0388c8
title: About Windows Image Acquisition
ms.topic: article
ms.date: 05/31/2018
---

# About Windows Image Acquisition

The Windows Image Acquisition (WIA) interface is both an API and a device driver interface (DDI). The WIA API is designed to allow applications to:

-   Run in a robust and stable environment.
-   Minimize interoperability problems.
-   Enumerate available image acquisition devices.
-   Create connections to multiple devices simultaneously.
-   Query properties of devices in a standard and expandable manner.
-   Acquire device data using standard and high performance transfer mechanisms.
-   Maintain image properties across data transfers.
-   Be notified of a wide variety of device events.

The WIADDI is designed to minimize the amount of code a hardware vendor must write, while maintaining the flexibility to craft individual solutions. This is accomplished by:

-   Providing a standard device service library that performs most driver operations.
-   Promoting industry device communications standards so that one WIA driver supports most WIA devices. For example, Picture Transfer Protocol (PTP).
-   Allowing the device driver to support custom interfaces, while not requiring that it use the standard device service library. However, drivers still need to implement the standard WIA interfaces.

This section presents a brief overview of the WIA interface in the following areas:

-   [WIA Architecture](-wia-wia-architecture.md)
-   [STI Compatibility](-wia-sti-compatibility.md)
-   [TWAIN Compatibility](-wia-twain-compatibility.md)
-   [WIA Device Manager](-wia-wia-device-manager.md)
-   [WIA Minidriver Service Library](-wia-wia-minidriver-service-library.md)
-   [WIA Minidriver](-wia-wia-minidriver.md)

 

 



