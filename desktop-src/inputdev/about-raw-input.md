---
title: Raw Input Overview
description: This topic discusses user-input from devices such as joysticks, touch screens, and microphones.
ms.assetid: 013ed309-f667-47ed-ade0-5e7ca5a0997a
keywords:
- user input,raw input
- capturing user input,raw input
- raw input
- registering raw input
- reading raw input
- joystick raw input
- touch screen raw input
- microphone raw input
- Human Interface Device (HID)
- HID (Human Interface Device)
ms.topic: article
ms.date: 05/31/2018
---

# Raw Input Overview

There are many user-input devices beside the traditional keyboard and mouse. For example, user input can come from a joystick, a touch screen, a microphone, or other devices that allow great flexibility in user input. These devices are collectively known as Human Interface Devices (HIDs). The raw input API provides a stable and robust way for applications to accept raw input from any HID, including the keyboard and mouse.

This section covers the following topics:

-   [Raw Input Model](#raw-input-model)
-   [Registration for Raw Input](#registration-for-raw-input)
-   [Reading Raw Input](#reading-raw-input)

## Raw Input Model

Previously, the keyboard and mouse typically generated input data. The system interpreted the data coming from these devices in a way that eliminated the device-specific details of the raw information. For example, the keyboard generates the device-specific scan code but the system provides an application with the virtual key code. Besides hiding the details of the raw input, the window manager did not support all the new HIDs. To get input from the unsupported HIDs, an application had to do many things: open the device, manage the shared mode, periodically read the device or set up the I/O completion port, and so forth. The raw input model and the associated APIs were developed to allow simple access to raw input from all input devices, including the keyboard and mouse.

The raw input model is different from the original Windows input model for the keyboard and mouse. In the original input model, an application receives device-independent input in the form of messages that are sent or posted to its windows, such as [**WM\_CHAR**](wm-char.md), [**WM\_MOUSEMOVE**](wm-mousemove.md), and [**WM\_APPCOMMAND**](wm-appcommand.md). In contrast, for raw input an application must register the devices it wants to get data from. Also, the application gets the raw input through the [**WM\_INPUT**](wm-input.md) message.

There are several advantages to the raw input model:

-   An application does not have to detect or open the input device.
-   An application gets the data directly from the device, and processes the data for its needs.
-   An application can distinguish the source of the input even if it is from the same type of device. For example, two mouse devices.
-   An application manages the data traffic by specifying data from a collection of devices or only specific device types.
-   HID devices can be used as they become available in the marketplace, without waiting for new message types or an updated OS to have new commands in [**WM\_APPCOMMAND**](wm-appcommand.md).

Note that [**WM\_APPCOMMAND**](wm-appcommand.md) does provide for some HID devices. However, **WM\_APPCOMMAND** is a higher level device-independent input event, while [**WM\_INPUT**](wm-input.md) sends raw, low level data that is specific to a device.

## Registration for Raw Input

By default, no application receives raw input. To receive raw input from a device, an application must register the device.

To register devices, an application first creates an array of [**RAWINPUTDEVICE**](/windows/win32/api/winuser/ns-winuser-rawinputdevice) structures that specify the [top level collection](/windows-hardware/drivers/hid/top-level-collections) (TLC) for the devices it wants. The TLC is defined by a [Usage Page](/windows-hardware/drivers/hid/hid-usages#usage-page) (the class of the device) and a [Usage ID](/windows-hardware/drivers/hid/hid-usages#usage-id) (the device within the class). For example, to get the keyboard TLC, set UsagePage = 0x01 and UsageID = 0x06. The application calls [**RegisterRawInputDevices**](/windows/win32/api/winuser/nf-winuser-registerrawinputdevices) to register the devices.

Note that an application can register a device that is not currently attached to the system. When this device is attached, the Windows Manager will automatically send the raw input to the application. To get the list of raw input devices on the system, an application calls [**GetRawInputDeviceList**](/windows/win32/api/winuser/nf-winuser-getrawinputdevicelist). Using the *hDevice* from this call, an application calls [**GetRawInputDeviceInfo**](/windows/win32/api/winuser/nf-winuser-getrawinputdeviceinfoa) to get the device information.

Through the **dwFlags** member of [**RAWINPUTDEVICE**](/windows/win32/api/winuser/ns-winuser-rawinputdevice), an application can select the devices to listen to and also those it wants to ignore. For example, an application can ask for input from all telephony devices except for answering machines. For sample code, see [Registering for Raw Input](using-raw-input.md).

Note that the mouse and the keyboard are also HIDs, so data from them can come through both the HID message [**WM\_INPUT**](wm-input.md) and from traditional messages. An application can select either method by the proper selection of flags in [**RAWINPUTDEVICE**](/windows/win32/api/winuser/ns-winuser-rawinputdevice).

To get an application's registration status, call [**GetRegisteredRawInputDevices**](/windows/win32/api/winuser/nf-winuser-getregisteredrawinputdevices) at any time.

## Reading Raw Input

An application receives raw input from any HID whose [top level collection](/windows-hardware/drivers/hid/top-level-collections) (TLC) matches a TLC from the registration. When an application receives raw input, its message queue gets a [**WM\_INPUT**](wm-input.md) message and the queue status flag **QS\_RAWINPUT** is set (**QS\_INPUT** also includes this flag). An application can receive data when it is in the foreground and when it is in the background.

There are two ways to read the raw data: the unbuffered (or standard) method and the buffered method. The unbuffered method gets the raw data one [**RAWINPUT**](/windows/win32/api/winuser/ns-winuser-rawinput) structure at a time and is adequate for many HIDs. Here, the application calls [**GetMessage**](/windows/desktop/api/winuser/nf-winuser-getmessage) to get the [**WM\_INPUT**](wm-input.md) message. Then the application calls [**GetRawInputData**](/windows/win32/api/winuser/nf-winuser-getrawinputdata) using the **RAWINPUT** handle contained in **WM\_INPUT**. For an example, see [Doing a Standard Read of Raw Input](using-raw-input.md).

In contrast, the buffered method gets an array of [**RAWINPUT**](/windows/win32/api/winuser/ns-winuser-rawinput) structures at a time. This is provided for devices that can produce large amounts of raw input. In this method, the application calls [**GetRawInputBuffer**](/windows/win32/api/winuser/nf-winuser-getrawinputbuffer) to get an array of **RAWINPUT** structures. Note that the [**NEXTRAWINPUTBLOCK**](/windows/win32/api/winuser/nf-winuser-nextrawinputblock) macro is used to traverse an array of **RAWINPUT** structures. For an example, see [Doing a Buffered Read of Raw Input](using-raw-input.md).

To interpret the raw input, detailed information about the HIDs is required. An application gets the device information by calling [**GetRawInputDeviceInfo**](/windows/win32/api/winuser/nf-winuser-getrawinputdeviceinfoa) with the device handle. This handle can come either from [**WM\_INPUT**](wm-input.md) or from the **hDevice** member of [**RAWINPUTHEADER**](/windows/win32/api/winuser/ns-winuser-rawinputheader).


## See also
- [Keyboard Input](keyboard-input.md)
- [About Keyboard Input](about-keyboard-input.md)

 

