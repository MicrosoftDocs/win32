---
title: Raw Input
description: This section describes how the system provides raw input to your application and how an application receives and processes that input.
ms.assetid: '013ed309-f667-47ed-ade0-5e7ca5a0997a'
keywords: ["Windows User Interface,user input", "Windows User Interface,raw input", "user input,raw input", "capturing user input,raw input", "raw input"]
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
| [**DefRawInputProc**](defrawinputproc.md)                           | Calls the default raw input procedure to provide default processing for any raw input messages that an application does not process. This function ensures that every message is processed. [**DefRawInputProc**](defrawinputproc.md) is called with the same parameters received by the window procedure. <br/> |
| [**GetRawInputBuffer**](getrawinputbuffer.md)                       | Performs a buffered read of the raw input data.<br/>                                                                                                                                                                                                                                                              |
| [**GetRawInputData**](getrawinputdata.md)                           | Gets the raw input from the specified device.<br/>                                                                                                                                                                                                                                                                |
| [**GetRawInputDeviceInfo**](getrawinputdeviceinfo.md)               | Gets information about the raw input device.<br/>                                                                                                                                                                                                                                                                 |
| [**GetRawInputDeviceList**](getrawinputdevicelist.md)               | Enumerates the raw input devices attached to the system. <br/>                                                                                                                                                                                                                                                    |
| [**GetRegisteredRawInputDevices**](getregisteredrawinputdevices.md) | Gets the information about the raw input devices for the current application.<br/>                                                                                                                                                                                                                                |
| [**RegisterRawInputDevices**](registerrawinputdevices.md)           | Registers the devices that supply the raw input data.<br/>                                                                                                                                                                                                                                                        |



 

### Macros



| Name                                                            | Description                                                                                                 |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [**GET\_RAWINPUT\_CODE\_WPARAM**](get-rawinput-code-wparam.md) | Gets the input code from *wParam* in [**WM\_INPUT**](wm-input.md).<br/>                              |
| [**NEXTRAWINPUTBLOCK**](nextrawinputblock.md)                  | Gets the location of the next structure in an array of [**RAWINPUT**](rawinput.md) structures. <br/> |



 

### Notifications



| Name                                                        | Description                                                          |
|-------------------------------------------------------------|----------------------------------------------------------------------|
| [**WM\_INPUT**](wm-input.md)                               | Sent to the window that is getting raw input. <br/>            |
| [**WM\_INPUT\_DEVICE\_CHANGE**](wm-input-device-change.md) | Sent to the window that registered to receive raw input. <br/> |



 

### Structures



| Name                                                            | Description                                                                            |
|-----------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**RAWHID**](rawhid.md)                                        | Describes the format of the raw input from a Human Interface Device (HID). <br/> |
| [**RAWINPUT**](rawinput.md)                                    | Contains the raw input from a device. <br/>                                      |
| [**RAWINPUTDEVICE**](rawinputdevice.md)                        | Defines information for the raw input devices. <br/>                             |
| [**RAWINPUTDEVICELIST**](rawinputdevicelist.md)                | Contains information about a raw input device.<br/>                              |
| [**RAWINPUTHEADER**](rawinputheader.md)                        | Contains the header information that is part of the raw input data. <br/>        |
| [**RAWKEYBOARD**](rawkeyboard.md)                              | Contains information about the state of the keyboard. <br/>                      |
| [**RAWMOUSE**](rawmouse.md)                                    | Contains information about the state of the mouse. <br/>                         |
| [**RID\_DEVICE\_INFO**](rid-device-info.md)                    | Defines the raw input data coming from any device. <br/>                         |
| [**RID\_DEVICE\_INFO\_HID**](rid-device-info-hid.md)           | Defines the raw input data coming from the specified HID. <br/>                  |
| [**RID\_DEVICE\_INFO\_KEYBOARD**](rid-device-info-keyboard.md) | Defines the raw input data coming from the specified keyboard. <br/>             |
| [**RID\_DEVICE\_INFO\_MOUSE**](rid-device-info-mouse.md)       | Defines the raw input data coming from the specified mouse.<br/>                 |



 

 

 





