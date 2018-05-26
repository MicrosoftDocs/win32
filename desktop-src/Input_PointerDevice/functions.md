---
Description: The topics in this section provide the reference specifications for Pointer Device Input Stack functions.
ms.assetid: 44942954-3EA6-4C33-8CF1-E8BF72A914CB
title: Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Functions

The topics in this section provide the reference specifications for [Pointer Device Input Stack](pointer-device-stack-portal.md) functions.

## In this section



| Topic                                                                                       | Description                                                                                                                                                                                                                                                                             |
|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetPointerDevice**](/windows/win32/winuser/nf-winuser-getpointerdevice?branch=master)<br/>                                     | Gets information about the pointer device.<br/>                                                                                                                                                                                                                                   |
| [**GetPointerDeviceCursors**](/windows/win32/winuser/nf-winuser-getpointerdevicecursors?branch=master)<br/>                       | Gets the cursor IDs that are mapped to the cursors associated with a pointer device.<br/>                                                                                                                                                                                         |
| [**GetPointerDeviceProperties**](/windows/win32/winuser/nf-winuser-getpointerdeviceproperties?branch=master)<br/>                 | Gets device properties that aren't included in the [**POINTER\_DEVICE\_INFO**](/windows/win32/Winuser/ns-winuser-tagpointer_device_info?branch=master) structure. <br/>                                                                                                                                                          |
| [**GetPointerDeviceRects**](/windows/win32/winuser/nf-winuser-getpointerdevicerects?branch=master)<br/>                           | Gets the x and y range for the pointer device (in himetric) and the x and y range (current resolution) for the display that the pointer device is mapped to. <br/>                                                                                                                |
| [**GetPointerDevices**](/windows/win32/winuser/nf-winuser-getpointerdevices?branch=master)<br/>                                   | Gets information about the pointer devices attached to the system.<br/>                                                                                                                                                                                                           |
| [**GetRawPointerDeviceData**](/windows/win32/winuser/nf-winuser-getrawpointerdevicedata?branch=master)<br/>                       | Gets the raw input data from the pointer device. <br/>                                                                                                                                                                                                                            |
| [**RegisterPointerDeviceNotifications**](/windows/win32/winuser/nf-winuser-registerpointerdevicenotifications?branch=master)<br/> | Registers a window to process the [**WM\_POINTERDEVICECHANGE**](inputmsg.wm_pointerdevicechange), [**WM\_POINTERDEVICEINRANGE**](inputmsg.wm_pointerdeviceinrange), and [**WM\_POINTERDEVICEOUTOFRANGE**](inputmsg.wm_pointerdeviceoutofrange) pointer device notifications.<br/> |



 

## Related topics

<dl> <dt>

[Pointer Device Input Stack Reference](unified-input-stack-reference.md)
</dt> </dl>

 

 




