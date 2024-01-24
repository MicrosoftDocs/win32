---
description: The DeviceIoControl function provides a device input and output control (IOCTL) interface through which an application can communicate directly with a device driver.
ms.assetid: 2dffd86a-162c-4e09-bfa1-73b87522741a
title: Device Input and Output Control (IOCTL)
ms.topic: article
ms.date: 05/31/2018
---

# Device Input and Output Control (IOCTL)

The [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) function provides a device input and output control (IOCTL) interface through which an application can communicate directly with a device driver. The **DeviceIoControl** function is a general-purpose interface that can send control codes to a variety of devices. Each control code represents an operation for the driver to perform. For example, a control code can ask a device driver to return information about the corresponding device, or direct the driver to carry out an action on the device, such as formatting a disk.

A number of standard control codes are defined in the SDK header files. In addition, device drivers can define their own device-specific control codes. For a list of standard control codes included in the SDK documentation, see the Remarks section of [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol).

The types of control codes you can specify depend on the device being accessed and the platform on which your application is running. Applications can use the standard control codes or device-specific control codes to perform direct input and output operations on a floppy disk drive, hard disk drive, tape drive, or CD-ROM drive.

## Related topics

<dl> <dt>

[Calling DeviceIoControl](calling-deviceiocontrol.md)
</dt> </dl>

 

 
