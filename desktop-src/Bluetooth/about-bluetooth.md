---
title: About Bluetooth
description: Bluetooth is an industry-standard protocol that enables wireless connectivity for a multitude of devices, including computers, printers, mobile phones, and handheld devices.
ms.assetid: 424168a1-e55c-4947-9a80-8594b4d83bbd
keywords:
- Bluetooth Bluetooth , described
- Bluetooth Bluetooth , about
ms.topic: article
ms.date: 05/31/2018
---

# About Bluetooth

Bluetooth is an industry-standard protocol that enables wireless connectivity for a multitude of devices, including computers, printers, mobile phones, and handheld devices.

Key Bluetooth features include:

-   A low-cost, low-power consumption wireless protocol with industry-standard support and worldwide acceptance.
-   A defined and familiar programming interface that developers can use to quickly develop or port applications.
-   An official Web site and an industry-wide cooperative organization that explains, promotes, and standardizes Bluetooth technology. For more information, see [www.bluetooth.com](https://www.bluetooth.com/).

Bluetooth on Windows provides core services that are similar to those exposed by Transmission Control Protocol (the TCP part of TCP/IP). Like many networking protocols and services, Bluetooth connectivity and data transfer are programmed through Windows Sockets function calls, using common Windows Sockets programming techniques and specific Bluetooth extensions. However, because significant differences exist between a wired, fixed network and a wireless ad-hoc network, Bluetooth provides extensions such as service/device discovery and notification that enable applications to operate properly in the wireless environment. These extensions also pave the way for simple porting to similar technologies, such as IrDA, or future wireless transports.

Microsoft provides support for Bluetooth on Windows XP with Service Pack 1 (SP1) and later, on Windows XP Embedded with Service Pack 2, and on Windows CE. Bluetooth applications that run on Windows XP should be able to run on a Windows XP Embedded-based run-time image that includes the required dependencies. For more information about Windows XP Embedded, see the Windows XP Embedded Help documentation on MSDN. For more information about Windows CE programming, consult the Windows CE SDK.

Microsoft provides two approaches for programming Bluetooth on Windows:

-   Using the Windows Sockets interface
-   Managing devices directly by using nonsocket Bluetooth interfaces

This section provides overview information about both of these approaches in the following topics. For more information about using Windows Sockets API elements to program Bluetooth, see [Bluetooth Programming with Windows Sockets](bluetooth-programming-with-windows-sockets.md).



| Section                                                                                | Content                                                           |
|----------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| [Windows Sockets Support for Bluetooth](windows-sockets-support-for-bluetooth.md)     | Describes the relationship between Bluetooth and Windows Sockets. |
| [Managing Bluetooth Devices and Services](managing-bluetooth-devices-and-services.md) | Describes how to manage Bluetooth devices and services.           |



 

 

 




