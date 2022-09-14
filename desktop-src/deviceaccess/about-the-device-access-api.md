---
title: About the Device Access API
description: The Device Access API is for C++ developers who are creating a Windows Store app to interact with specialized devices in Windows 8.
ms.assetid: DDF115A2-A811-450A-80F7-AAFB0EEA4037
ms.topic: article
ms.date: 02/11/2020
---

# About the Device Access API

The Device Access API is for C++ developers who are creating a Windows Store app to interact with specialized devices in Windows 8. This topic describes the scenarios that the Device Access API applies to. It also explains how the Device Access API applies security rules for Windows Store apps in Windows 8.

- [Enabling custom device functionality in Windows Store device apps](#enabling-custom-device-functionality-in-windows-store-device-apps)

## Enabling custom device functionality in Windows Store device apps

Developers for independent hardware vendors (IHVs) and OEMs can build a Windows Store app that's paired with their device and automatically acquired when the device is installed. This app, known as a Windows Store device app, can provide unique device functionality.

Devices that don't have built-in class drivers or Windows Runtime APIs for communicating with the device in Windows 8 are known as *specialized devices*. These devices might require a custom driver. For more information about the types of devices that require custom drivers, see the Windows Store device app design guide for specialized devices .

The Windows Store device app for a specialized device that must communicate with a device's custom driver can't use Microsoft Win32 APIs like [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) and [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) to send IOCTLs to the device. The restricted security environment where Windows Store device apps run require that you use the Device Access API to communicate with your custom driver from a Windows Store app.

The developer of a custom device restricts access to approved, privileged applications. For instance, the manufacturer of a media-player device might want users to play music only through the IHV-provided music app and restrict any competitor's app from syncing media from the device. When you're building the device driver, you set a property in the information (INF) fileto specify that only privileged apps can access the device. Metadata on the device itself specifies the package IDs for the set of approved apps. See [UWP device apps for internal devices](/windows-hardware/drivers/devapps/uwp-device-apps-for-specialized-devices) for more detail on the process of setting this metadata on your device.

## Related topics

[Custom Driver Access Sample](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/411c271e537727d737a53fa2cbe99eaecac00cc0/Official%20Windows%20Platform%20Sample/Custom%20driver%20access%20sample), [UWP device apps for internal devices](/windows-hardware/drivers/devapps/uwp-device-apps-for-specialized-devices), [Hardware Dev Center](/windows-hardware/drivers/)