---
title: Raw Input
description: This section describes how the system provides raw input to your application and how an application receives and processes that input.
ms.assetid: 013ed309-f667-47ed-ade0-5e7ca5a0997a
keywords:
- Windows User Interface,user input
- Windows User Interface,raw input
- user input,raw input
- capturing user input,raw input
- raw input
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Raw Input

This section describes how the system provides raw input to your application and how an application receives and processes that input. Raw input is sometimes referred to as generic input.

### In This Section



| Name                                           | Description                                                                                     |
|------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [About Raw Input](about-raw-input.md)         | Discusses user-input from devices such as joysticks, touch screens, and microphones.<br/> |
| [Using Raw Input](using-raw-input.md)         | Provides sample code for tasks relating to raw input.<br/>                                |
| [Raw Input Reference](raw-input-reference.md) | Contains the API reference.<br/>                                                          |



 

### Functions



| Name                                                                 | Description                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DefRawInputProc**](/windows/desktop/api/Winuser/nf-winuser-defrawinputproc)                           | Calls the default raw input procedure to provide default processing for any raw input messages that an application does not process. This function ensures that every message is processed. [**DefRawInputProc**](/windows/desktop/api/Winuser/nf-winuser-defrawinputproc) is called with the same parameters received by the window procedure. <br/> |
| [**GetRawInputBuffer**](/windows/desktop/api/Winuser/nf-winuser-getrawinputbuffer)                       | Performs a buffered read of the raw input data.<br/>                                                                                                                                                                                                                                                              |
| [**GetRawInputData**](/windows/desktop/api/Winuser/nf-winuser-getrawinputdata)                           | Gets the raw input from the specified device.<br/>                                                                                                                                                                                                                                                                |
| [**GetRawInputDeviceInfo**](/windows/desktop/api/Winuser/nf-winuser-getrawinputdeviceinfoa)               | Gets information about the raw input device.<br/>                                                                                                                                                                                                                                                                 |
| [**GetRawInputDeviceList**](/windows/desktop/api/Winuser/nf-winuser-getrawinputdevicelist)               | Enumerates the raw input devices attached to the system. <br/>                                                                                                                                                                                                                                                    |
| [**GetRegisteredRawInputDevices**](/windows/desktop/api/Winuser/nf-winuser-getregisteredrawinputdevices) | Gets the information about the raw input devices for the current application.<br/>                                                                                                                                                                                                                                |
| [**RegisterRawInputDevices**](/windows/desktop/api/Winuser/nf-winuser-registerrawinputdevices)           | Registers the devices that supply the raw input data.<br/>                                                                                                                                                                                                                                                        |



 

### Macros



| Name                                                            | Description                                                                                                 |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [**GET\_RAWINPUT\_CODE\_WPARAM**](/windows/desktop/api/Winuser/nf-winuser-get_rawinput_code_wparam) | Gets the input code from *wParam* in [**WM\_INPUT**](wm-input.md).<br/>                              |
| [**NEXTRAWINPUTBLOCK**](/windows/desktop/api/Winuser/nf-winuser-nextrawinputblock)                  | Gets the location of the next structure in an array of [**RAWINPUT**](/windows/desktop/api/Winuser/nf-winuser-defrawinputproc) structures. <br/> |



 

### Notifications



| Name                                                        | Description                                                          |
|-------------------------------------------------------------|----------------------------------------------------------------------|
| [**WM\_INPUT**](wm-input.md)                               | Sent to the window that is getting raw input. <br/>            |
| [**WM\_INPUT\_DEVICE\_CHANGE**](wm-input-device-change.md) | Sent to the window that registered to receive raw input. <br/> |



 

### Structures



| Name                                                            | Description                                                                            |
|-----------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**RAWHID**](/windows/desktop/api/Winuser/ns-winuser-tagrawhid)                                        | Describes the format of the raw input from a Human Interface Device (HID). <br/> |
| [**RAWINPUT**](/windows/desktop/api/Winuser/nf-winuser-defrawinputproc)                                    | Contains the raw input from a device. <br/>                                      |
| [**RAWINPUTDEVICE**](/windows/desktop/api/Winuser/nf-winuser-getrawinputdeviceinfoa)                        | Defines information for the raw input devices. <br/>                             |
| [**RAWINPUTDEVICELIST**](/windows/desktop/api/Winuser/nf-winuser-getrawinputdevicelist)                | Contains information about a raw input device.<br/>                              |
| [**RAWINPUTHEADER**](/windows/desktop/api/Winuser/ns-winuser-tagrawinputheader)                        | Contains the header information that is part of the raw input data. <br/>        |
| [**RAWKEYBOARD**](/windows/desktop/api/Winuser/ns-winuser-tagrawkeyboard)                              | Contains information about the state of the keyboard. <br/>                      |
| [**RAWMOUSE**](/windows/desktop/api/Winuser/ns-winuser-tagrawmouse)                                    | Contains information about the state of the mouse. <br/>                         |
| [**RID\_DEVICE\_INFO**](/windows/desktop/api/Winuser/ns-winuser-tagrid_device_info)                    | Defines the raw input data coming from any device. <br/>                         |
| [**RID\_DEVICE\_INFO\_HID**](/windows/desktop/api/Winuser/ns-winuser-tagrid_device_info_hid)           | Defines the raw input data coming from the specified HID. <br/>                  |
| [**RID\_DEVICE\_INFO\_KEYBOARD**](/windows/desktop/api/Winuser/ns-winuser-tagrid_device_info_keyboard) | Defines the raw input data coming from the specified keyboard. <br/>             |
| [**RID\_DEVICE\_INFO\_MOUSE**](/windows/desktop/api/Winuser/ns-winuser-tagrid_device_info_mouse)       | Defines the raw input data coming from the specified mouse.<br/>                 |



 

 

 





