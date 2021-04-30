---
title: Devices (Windows 7 Developer Guide)
description: Devices are a fundamental part of the PC experience, and Windows 7 enables new possibilities for developers of applications that interact with devices.
ms.assetid: faed8ec8-2f12-4090-a003-b14b3d26e02a
ms.topic: article
ms.date: 05/31/2018
---

# Devices (Windows 7 Developer Guide)

Devices are a fundamental part of the PC experience, and Windows 7 enables new possibilities for developers of applications that interact with devices. The Device Experience Platform enables the association of applications and services with a particular device, so that users can get the maximum benefit from their peripherals immediately upon connection. The Sensor Platform provides a set of APIs for discovery of and communication with sensor devices that will enable a new generation of applications that are aware of their environments. The Location Platform provides new APIs for using location data from a Global Positioning Systems (GPS) receiver or other services that enable location-specific application behavior for mobile users. (See [Device Fundamentals - Overview](https://www.microsoft.com/whdc/device/default.mspx).)

## Device Experience Platform

Windows 7 combines software and services to create exciting new experiences for mobile phones, portable media players, cameras, and printers. Windows 7 makes it easier to use these devices directly from the Windows desktop. It also provides device makers with prominent placement on the Windows desktop, with branding opportunities and a simple interface for presenting the functionality and services that the device supports.

Through the Device Experience Platform, every Windows session becomes a portal for customers to get more value from their devices. The Device Experience Platform enables users to connect with the device manufacturer, discover and use related services, and learn about accessories. Because the device experience is connected to Microsoft's web services, device companies can update the experience even after devices have been shipped to consumers. The Device Experience Platform can generate an application-like experience for Windows*Logo'd* devices, such as a mobile phones.

The Device Experience Platform gives applications access to devices such as mobile phones and media players that implement services through the *Media Transfer Protocol (MTP)* or the [Windows Portable Devices](https://www.bing.com/search?q=Windows+Portable+Devices) driver model.

To enable the synchronization of personal information between a PC and a device, the Device Experience Platform hosts a new synchronization platform for connected devices, and provides a user interface for selecting target applications for data synchronization such as **Contacts**, **Calendar**, and **Tasks**. (See [Windows Device Experience](https://www.microsoft.com/whdc/device/DeviceExperience/default.mspx).)

## Windows Biometric Framework

The Windows Biometric Framework (WBF) provides an API which enables applications to use fingerprint devices to enroll, identify, and verify user identities without gaining direct access to any biometric fingerprint hardware or samples. You can use WBF with fingerprint devices that have Windows Biometric Device Interface (WBDI) drivers. WBF is extensible through plug-in adapters that manage sensor communications, biometric matching, and template storage. This ensures that WBF can be used with a wide range of fingerprint sensors. In Windows 7, fingerprint readers can use WBF for authentication during *UAC* and Windows logon. (See [Windows Biometric Framework API](../secbiomet/biometric-service-api-portal.md).)

 

 
