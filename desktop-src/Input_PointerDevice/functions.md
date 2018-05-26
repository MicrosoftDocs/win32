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
| [**GetPointerDevice**](getpointerdevice.md)<br/>                                     | Gets information about the pointer device.<br/>                                                                                                                                                                                                                                   |
| [**GetPointerDeviceCursors**](getpointerdevicecursors.md)<br/>                       | Gets the cursor IDs that are mapped to the cursors associated with a pointer device.<br/>                                                                                                                                                                                         |
| [**GetPointerDeviceProperties**](getpointerdeviceproperties.md)<br/>                 | Gets device properties that aren't included in the [**POINTER\_DEVICE\_INFO**](pointer-device-info.md) structure. <br/>                                                                                                                                                          |
| [**GetPointerDeviceRects**](getpointerdevicerects.md)<br/>                           | Gets the x and y range for the pointer device (in himetric) and the x and y range (current resolution) for the display that the pointer device is mapped to. <br/>                                                                                                                |
| [**GetPointerDevices**](getpointerdevices.md)<br/>                                   | Gets information about the pointer devices attached to the system.<br/>                                                                                                                                                                                                           |
| [**GetRawPointerDeviceData**](getrawpointerdevicedata.md)<br/>                       | Gets the raw input data from the pointer device. <br/>                                                                                                                                                                                                                            |
| [**RegisterPointerDeviceNotifications**](registerpointerdevicenotifications.md)<br/> | Registers a window to process the [**WM\_POINTERDEVICECHANGE**](inputmsg.wm_pointerdevicechange), [**WM\_POINTERDEVICEINRANGE**](inputmsg.wm_pointerdeviceinrange), and [**WM\_POINTERDEVICEOUTOFRANGE**](inputmsg.wm_pointerdeviceoutofrange) pointer device notifications.<br/> |



 

## Related topics

<dl> <dt>

[Pointer Device Input Stack Reference](unified-input-stack-reference.md)
</dt> </dl>

 

 




