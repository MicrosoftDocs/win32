---
title: Design Considerations for Custom Devices
description: This topic describes design considerations that can help you determine whether your device needs a custom driver.
ms.assetid: 8AADE304-4841-41E2-968B-DFCB5B954FF1
ms.topic: article
ms.date: 02/11/2020
---

# Design Considerations for Custom Devices

This topic describes design considerations that can help you determine whether your device needs a custom driver.

- [Determining the type of driver to implement](#determining-the-type-of-driver-to-implement)
- [Security considerations](#security-considerations)
- [Related topics](#related-topics)

## Determining the type of driver to implement

This table describes when you should develop a custom driver for your device and communicate with it by using the Device Access API, and when you should use Windows-provided device stacks instead.

| To support | Implementation |
|:---|:---|
| Well-known devices, including: <ul><li>Sensor</li><li>Location</li><li>Webcam</li><li>Proximity</li><li>Short message service (SMS)</li><li>Mobile broadband</li></ul><br/> | For many types of well-known devices, you don't need a custom driver, because Windows includes APIs and class-extension device driver interfaces (DDIs) that manage the communication between the driver and Windows. Sensor, location, and Windows Portable Device (WPD) devices are some examples of device classes that have this support. If you build a driver that uses one of these Windows-provided DDIs to send and receive data and commands, there's no need for your Windows Store app to use the Device Access API to broker access or send input/output (I/O) control codes directly to the driver. <br/> When a Windows Store app requests access to a well-known device by using the Windows Runtime API for its device class, Windows 8 will handle device access based on the type of device. Apps will always get access to some well-known types of devices (such as accelerometers) that don't reveal any personally identifiable information. Other types of well-known devices must be declared in the application manifest before an app can access them. The user must grant permission for an app to access devices that reveal sensitive information, like location, webcam, and microphone devices, or can cost the user money, like mobile broadband devices. <br/> |
| A WPD device that implements MTP services.<br/> | You can use the MTP class driver, or you can build a driver by using the WPD DDI.<br/> Windows 8 provides support for MTP device services.And an app can use the [Windows.Devices.Portable](/uwp/api/Windows.Devices.Portable) Windows Runtime API, the Portable Device Component Object Model (COM) API, or WPD Automation to access the device. Your app doesn't need to use the Device Access API.<br/> |
| A device that doesn't have a Windows-provided class extension or class driver.<br/>  | In this case, consult the [UWP device apps for internal devices](/windows-hardware/drivers/devapps/uwp-device-apps-for-specialized-devices) for specialized devices to determine whether you must implement custom driver access by using the Device Access API.<br/> |

## Security considerations

The following articles provide guidance for writing secure C++ code:

- [Security Best Practices for C++](/cpp/security/security-best-practices-for-cpp)
- [Patterns & Practices Security Guidance for Applications]/previous-versions/msp-n-p/ff650760(v=pandp.10))

## Related topics

[Custom Driver Access Sample](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/411c271e537727d737a53fa2cbe99eaecac00cc0/Official%20Windows%20Platform%20Sample/Custom%20driver%20access%20sample), [UWP device apps for internal devices](/windows-hardware/drivers/devapps/uwp-device-apps-for-specialized-devices), [Hardware Dev Center](/windows-hardware/drivers/)
