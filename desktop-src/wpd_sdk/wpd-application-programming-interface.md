---
description: WPD Application Programming Interface
ms.assetid: 3e2be15f-7af7-4e76-89b1-f9bc591c4f1b
title: WPD Application Programming Interface
ms.topic: article
ms.date: 05/31/2018
---

# WPD Application Programming Interface

Applications built on Windows Portable Devices can explore a device, send and receive content, and even control the device, for example, take a picture or send a text message. The system is designed to be flexible so that many types of devices can be explored, and extensible so that driver developers can define custom properties and commands for custom devices.

The following table describes the main topics of this documentation.



| Topic                                                                                                                  | Description                                                                                                |
|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [General Requirements for Application Development](general-requirements-for-application-development.md)               | Hardware and software requirements to develop drivers and applications using Windows Portable Devices.     |
| [Requirements for Windows Media DRM-Enabled Applications](requirements-for-windows-media-drm-enabled-applications.md) | Properties that are required to enable Windows Media DRM-protected content transfers.                      |
| [Samples](sample.md)                                                                                                  | Description of two command-line desktop applications that are supplied with this software development kit. |
| [Application Overview](application-overview.md)                                                                       | Key concepts used in Windows Portable Devices.                                                             |
| [Programming Guide](programming-guide.md)                                                                             | Key tasks that an application will perform, with step-by-step instructions and code snippets.              |
| [Programming Reference](programming-reference.md)                                                                     | Reference guide to the interfaces and data types defined by Windows Portable Devices.                      |



 

Applications built on Windows Media Device Manager or Windows Image Acquisition can access Windows Portable Devices through a compatibility layer.

Microsoft provides several drivers for standard protocols and devices, including Media Transport Protocol (MTP) devices and Mass Storage Class (MSC) devices. If you are familiar with the User-Mode Driver Framework, you can develop your own drivers for custom devices.

 

 



