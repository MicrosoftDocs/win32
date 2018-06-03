---
Description: The topics in this section provide the reference specifications for Pointer Device Input Stack functions.
ms.assetid: 44942954-3EA6-4C33-8CF1-E8BF72A914CB
title: Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Functions

The topics in this section provide the reference specifications for [Pointer Device Input Stack](pointer-device-stack-portal.md) functions.

## In this section



| Topic                                                                                       | Description                                                                                                                                                                                                                                                                             |
|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetPointerDevice**](/windows/desktop/api/winuser/nf-winuser-getpointerdevice)<br/>                                     | Gets information about the pointer device.<br/>                                                                                                                                                                                                                                   |
| [**GetPointerDeviceCursors**](/windows/desktop/api/winuser/nf-winuser-getpointerdevicecursors)<br/>                       | Gets the cursor IDs that are mapped to the cursors associated with a pointer device.<br/>                                                                                                                                                                                         |
| [**GetPointerDeviceProperties**](/windows/desktop/api/winuser/nf-winuser-getpointerdeviceproperties)<br/>                 | Gets device properties that aren't included in the [**POINTER\_DEVICE\_INFO**](/windows/desktop/api/Winuser/ns-winuser-tagpointer_device_info) structure. <br/>                                                                                                                                                          |
| [**GetPointerDeviceRects**](/windows/desktop/api/winuser/nf-winuser-getpointerdevicerects)<br/>                           | Gets the x and y range for the pointer device (in himetric) and the x and y range (current resolution) for the display that the pointer device is mapped to. <br/>                                                                                                                |
| [**GetPointerDevices**](/windows/desktop/api/winuser/nf-winuser-getpointerdevices)<br/>                                   | Gets information about the pointer devices attached to the system.<br/>                                                                                                                                                                                                           |
| [**GetRawPointerDeviceData**](/windows/desktop/api/winuser/nf-winuser-getrawpointerdevicedata)<br/>                       | Gets the raw input data from the pointer device. <br/>                                                                                                                                                                                                                            |
| [**RegisterPointerDeviceNotifications**](/windows/desktop/api/winuser/nf-winuser-registerpointerdevicenotifications)<br/> | Registers a window to process the [**WM\_POINTERDEVICECHANGE**](https://msdn.microsoft.com/windows/desktop/9ED01D4C-58B4-4A21-B510-784281F9A909), [**WM\_POINTERDEVICEINRANGE**](https://msdn.microsoft.com/windows/desktop/04244758-E662-4FB2-850E-20B4B3D1294A), and [**WM\_POINTERDEVICEOUTOFRANGE**](https://msdn.microsoft.com/windows/desktop/6BC667C1-6D9A-4E69-BAC6-761A1859F09E) pointer device notifications.<br/> |



 

## Related topics

<dl> <dt>

[Pointer Device Input Stack Reference](unified-input-stack-reference.md)
</dt> </dl>

 

 




