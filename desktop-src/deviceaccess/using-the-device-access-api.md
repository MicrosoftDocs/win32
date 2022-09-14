---
title: How to Use the Device Access API
description: This topic contains tasks and design considerations for using the Device Access API.
ms.assetid: 8D951EB5-4AFB-4051-8F1F-30F847F1A757
ms.topic: article
ms.date: 02/11/2020
---

# How to Use the Device Access API

This topic contains tasks and design considerations for using the Device Access API.

## Steps

| Topic | Description |
|---|---|
| [Design Considerations for Custom Devices](design.md)<br/> | This topic describes design considerations that can help you determine whether your device needs a custom driver.<br/> |
| [Implement the Device Access Object](create-the-device-access-object.md)<br/> | This topic explains how to instantiate the device access object and use it to access a device. <br/>  |
| [Declaring the Device Capability](declaring-the-device-capability.md)<br/> | This topic explains how to declare the device capability GUID.<br/> |
| [Register the device interface as restricted to privileged apps](register-the-device-interface-class-as-privileged.md)<br/> | This topic shows how to add the **Restricted** property that indicates that only privileged apps can access a device interface class.<br/> |
| [Create a Windows Runtime Extension](create-a-windows-runtime-extension.md)<br/> | You can create a Windows Runtime component to wrap the component that accesses your driver. You can then write a Windows Store device app for your device in C# or JavaScript.<br/> |

## Additional resources

- The [Custom Driver Access Sample](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/411c271e537727d737a53fa2cbe99eaecac00cc0/Official%20Windows%20Platform%20Sample/Custom%20driver%20access%20sample) demonstrates how to use the Device Access APIs to access a custom driver from a Windows Store device app.
- [UWP device apps for internal devices](/windows-hardware/drivers/devapps/uwp-device-apps-for-specialized-devices) provides resources for learning more about how to design and develop Windows Store device apps for specialized devices.
- The [Hardware Dev Center](/windows-hardware/drivers/) provides general resources for Windows Store device app development tasks that are common to all types of devices.
