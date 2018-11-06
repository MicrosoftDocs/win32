---
title: Raw Input
description: This section describes how the system provides raw input to your application and how an application receives and processes that input.
ms.assetid: 'vs|winui|~\winui\windowsuserinterface\userinput\rawinput.htm'
keywords:
- Windows User Interface,user input
- Windows User Interface,raw input
- user input,raw input
- capturing user input,raw input
- raw input
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
| [**DefRawInputProc**](https://msdn.microsoft.com/en-us/library/ms645594(v=VS.85).aspx)                           | Calls the default raw input procedure to provide default processing for any raw input messages that an application does not process. This function ensures that every message is processed. [**DefRawInputProc**](https://msdn.microsoft.com/en-us/library/ms645594(v=VS.85).aspx) is called with the same parameters received by the window procedure. <br/> |
| [**GetRawInputBuffer**](https://msdn.microsoft.com/en-us/library/ms645595(v=VS.85).aspx)                       | Performs a buffered read of the raw input data.<br/>                                                                                                                                                                                                                                                              |
| [**GetRawInputData**](https://msdn.microsoft.com/en-us/library/ms645596(v=VS.85).aspx)                           | Gets the raw input from the specified device.<br/>                                                                                                                                                                                                                                                                |
| [**GetRawInputDeviceInfo**](https://msdn.microsoft.com/en-us/library/ms645597(v=VS.85).aspx)               | Gets information about the raw input device.<br/>                                                                                                                                                                                                                                                                 |
| [**GetRawInputDeviceList**](https://msdn.microsoft.com/en-us/library/ms645598(v=VS.85).aspx)               | Enumerates the raw input devices attached to the system. <br/>                                                                                                                                                                                                                                                    |
| [**GetRegisteredRawInputDevices**](https://msdn.microsoft.com/en-us/library/ms645599(v=VS.85).aspx) | Gets the information about the raw input devices for the current application.<br/>                                                                                                                                                                                                                                |
| [**RegisterRawInputDevices**](https://msdn.microsoft.com/en-us/library/ms645600(v=VS.85).aspx)           | Registers the devices that supply the raw input data.<br/>                                                                                                                                                                                                                                                        |



 

### Macros



| Name                                                            | Description                                                                                                 |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [**GET\_RAWINPUT\_CODE\_WPARAM**](https://msdn.microsoft.com/en-us/library/ms645592(v=VS.85).aspx) | Gets the input code from *wParam* in [**WM\_INPUT**](wm-input.md).<br/>                              |
| [**NEXTRAWINPUTBLOCK**](https://msdn.microsoft.com/en-us/library/ms645593(v=VS.85).aspx)                  | Gets the location of the next structure in an array of [**RAWINPUT**](https://msdn.microsoft.com/en-us/library/ms645562(v=VS.85).aspx) structures. <br/> |



 

### Notifications



| Name                                                        | Description                                                          |
|-------------------------------------------------------------|----------------------------------------------------------------------|
| [**WM\_INPUT**](wm-input.md)                               | Sent to the window that is getting raw input. <br/>            |
| [**WM\_INPUT\_DEVICE\_CHANGE**](wm-input-device-change.md) | Sent to the window that registered to receive raw input. <br/> |



 

### Structures



| Name                                                            | Description                                                                            |
|-----------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**RAWHID**](https://msdn.microsoft.com/en-us/library/ms645549(v=VS.85).aspx)                                        | Describes the format of the raw input from a Human Interface Device (HID). <br/> |
| [**RAWINPUT**](https://msdn.microsoft.com/en-us/library/ms645562(v=VS.85).aspx)                                    | Contains the raw input from a device. <br/>                                      |
| [**RAWINPUTDEVICE**](https://msdn.microsoft.com/en-us/library/ms645565(v=VS.85).aspx)                        | Defines information for the raw input devices. <br/>                             |
| [**RAWINPUTDEVICELIST**](https://msdn.microsoft.com/en-us/library/ms645568(v=VS.85).aspx)                | Contains information about a raw input device.<br/>                              |
| [**RAWINPUTHEADER**](https://msdn.microsoft.com/en-us/library/ms645571(v=VS.85).aspx)                        | Contains the header information that is part of the raw input data. <br/>        |
| [**RAWKEYBOARD**](https://msdn.microsoft.com/en-us/library/ms645575(v=VS.85).aspx)                              | Contains information about the state of the keyboard. <br/>                      |
| [**RAWMOUSE**](https://msdn.microsoft.com/en-us/library/ms645578(v=VS.85).aspx)                                    | Contains information about the state of the mouse. <br/>                         |
| [**RID\_DEVICE\_INFO**](https://msdn.microsoft.com/en-us/library/ms645581(v=VS.85).aspx)                    | Defines the raw input data coming from any device. <br/>                         |
| [**RID\_DEVICE\_INFO\_HID**](https://msdn.microsoft.com/en-us/library/ms645584(v=VS.85).aspx)           | Defines the raw input data coming from the specified HID. <br/>                  |
| [**RID\_DEVICE\_INFO\_KEYBOARD**](https://msdn.microsoft.com/en-us/library/ms645587(v=VS.85).aspx) | Defines the raw input data coming from the specified keyboard. <br/>             |
| [**RID\_DEVICE\_INFO\_MOUSE**](https://msdn.microsoft.com/en-us/library/ms645589(v=VS.85).aspx)       | Defines the raw input data coming from the specified mouse.<br/>                 |



 

 

 





