---
description: Removal of WPDUSB.SYS Driver for Windows Portable Devices
ms.assetid: 3ad0c892-8b19-465d-af2f-9207f98e27b7
title: Removal of WPDUSB.SYS Driver for Windows Portable Devices
ms.topic: article
ms.date: 05/31/2018
---

# Removal of WPDUSB.SYS Driver for Windows Portable Devices

## Affected Platforms

**Clients** - Windows 7  
**Servers** - Windows Server 2008 R2  









## Feature Impact

 **Severity** - Low  
**Frequency** - Low  





## Description

Microsoft has replaced the kernel mode component of the Windows Vista USB driver stack (WPDUSB.SYS) for Windows Portable Devices (WPD) with the generic WINUSB.SYS driver. Communication with the original WPDUSB.SYS driver was via private I/O Control (IOCTL) codes; support of these has also been removed.

Any consumer of these IOCTL codes would have been responsible for proper interpretation and implementation of the Media Transfer Protocol (MTP). Windows Vista did not support use of these IOCTL codes by third-party applications.

## Manifestation of Impact

Any application that depended on the availability of these private IOCTL codes would no longer have access to USB-connected MTP devices.

## Mitigation

Users of an application that depends on the private IOCTL codes must use a different application (or an updated version of the application) to access the USB-connected MTP device.

## Solution

Applications should use the Windows Portable Devices (WPD) API to find and interact with any WPD Device. Although a significant percentage of WPD devices implement MTP for communication with the PC, WPD is not limited to just MTP devices. In addition, where direct access to the device via the private IOCTLs would have limited the application to communication with only USB-connected devices, use of the WPD API expands the list of connectivity options to other communication protocols (for example, Wi-Fi). In the rare cases when the application must be MTP-aware, the WPD API provides a pass-through mechanism for raw MTP commands.

## Leveraging Feature Capabilities

The WPD API is supported in Windows XP (via the Windows Format SDK), Windows Vista and Windows 7. The Windows 7 implementation of WPD adds support for MTP over Bluetooth.

## Links to Other Resources

[Windows Portable Devices](../windows-portable-devices.md)

 

 
