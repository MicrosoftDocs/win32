---
title: About Bluetooth
description: Bluetooth is an industry-standard protocol that enables wireless connectivity for a multitude of devices, including computers, printers, mobile phones, and handheld devices.
ms.assetid: 424168a1-e55c-4947-9a80-8594b4d83bbd
keywords:
- Bluetooth Bluetooth , described
- Bluetooth Bluetooth , about
ms.topic: concept-article
ms.date: 07/16/2026
---

# About Bluetooth

Bluetooth is an industry-standard protocol that enables wireless connectivity for a multitude of devices, including computers, printers, mobile phones, and handheld devices.

Key Bluetooth features include:

-   A low-cost, low-power consumption wireless protocol with industry-standard support and worldwide acceptance.
-   A defined and familiar programming interface that developers can use to quickly develop or port applications.
-   An official Web site and an industry-wide cooperative organization that explains, promotes, and standardizes Bluetooth technology. For more information, see [www.bluetooth.com](https://www.bluetooth.com/).

## Classic Bluetooth and Bluetooth Low Energy (BLE)

The Win32 Bluetooth APIs documented in this section support **classic Bluetooth** (BR/EDR) scenarios—device discovery, pairing, RFCOMM socket communication, and SDP service registration.

> [!NOTE]
> **For Bluetooth Low Energy (BLE) GATT scenarios**, use the Windows Runtime (WinRT) APIs instead:
>
> - [**Windows.Devices.Bluetooth.GenericAttributeProfile**](/uwp/api/windows.devices.bluetooth.genericattributeprofile) — GATT client and server operations.
> - [**Windows.Devices.Bluetooth.Advertisement**](/uwp/api/windows.devices.bluetooth.advertisement) — BLE advertisement scanning and publishing.
> - [**Windows.Devices.Bluetooth**](/uwp/api/windows.devices.bluetooth) — Device enumeration and pairing for BLE.
>
> These WinRT APIs (from the Windows SDK) can be called from C++ desktop applications via [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/). They are also accessible from [Windows App SDK](/windows/apps/windows-app-sdk/) apps. They support BLE GATT profiles commonly used by IoT sensors, fitness devices, and peripherals on Windows 10 and later.

Bluetooth on Windows provides core services that are similar to those exposed by Transmission Control Protocol (the TCP part of TCP/IP). Like many networking protocols and services, Bluetooth connectivity and data transfer are programmed through Windows Sockets function calls, using common Windows Sockets programming techniques and specific Bluetooth extensions. However, because significant differences exist between a wired, fixed network and a wireless ad-hoc network, Bluetooth provides extensions such as service/device discovery and notification that enable applications to operate properly in the wireless environment. These extensions also pave the way for simple porting to similar technologies, such as IrDA, or future wireless transports.

Microsoft provides two approaches for programming classic Bluetooth on Windows:

-   Using the Windows Sockets interface
-   Managing devices directly by using nonsocket Bluetooth interfaces

This section provides overview information about both of these approaches in the following topics. For more information about using Windows Sockets API elements to program Bluetooth, see [Bluetooth Programming with Windows Sockets](bluetooth-programming-with-windows-sockets.md).



| Section                                                                                | Content                                                           |
|----------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| [Windows Sockets Support for Bluetooth](windows-sockets-support-for-bluetooth.md)     | Describes the relationship between Bluetooth and Windows Sockets. |
| [Managing Bluetooth Devices and Services](managing-bluetooth-devices-and-services.md) | Describes how to manage Bluetooth devices and services.           |



 

 

 




