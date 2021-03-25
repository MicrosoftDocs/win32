---
description: The topics in this section provide the reference specifications for Pointer Device Input Stack functions.
ms.assetid: 44942954-3EA6-4C33-8CF1-E8BF72A914CB
title: Pointer Device Input Stack functions
ms.topic: article
ms.date: 02/05/2020
---

# Pointer Device Input Stack functions

The topics in this section provide the reference specifications for [Pointer Device Input Stack](pointer-device-stack-portal.md) functions.

## In this section

| Topic | Description |
|---|---|
| [**CreateSyntheticPointerDevice**](/windows/win32/api/winuser/nf-winuser-createsyntheticpointerdevice)<br/> | Configures the pointer injection device for the calling application, and initializes the maximum number of simultaneous pointers that the app can inject.<br/> |
| [**DestroySyntheticPointerDevice**](/windows/win32/api/winuser/nf-winuser-destroysyntheticpointerdevice)<br/> | Destroys the specified pointer injection device.<br/> |
| [**GetPointerDevice**](/windows/win32/api/winuser/nf-winuser-getpointerdevice)<br/> | Gets information about the pointer device.<br/> |
| [**GetPointerDeviceCursors**](/windows/win32/api/winuser/nf-winuser-getpointerdevicecursors)<br/> | Gets the cursor IDs that are mapped to the cursors associated with a pointer device.<br/> |
| [**GetPointerDeviceProperties**](/windows/win32/api/winuser/nf-winuser-getpointerdeviceproperties)<br/> | Gets device properties that aren't included in the [**POINTER\_DEVICE\_INFO**](/previous-versions/windows/desktop/api) structure. <br/> |
| [**GetPointerDeviceRects**](/windows/win32/api/winuser/nf-winuser-getpointerdevicerects)<br/> | Gets the x and y range for the pointer device (in himetric) and the x and y range (current resolution) for the display that the pointer device is mapped to. <br/> |
| [**GetPointerDevices**](/windows/win32/api/winuser/nf-winuser-getpointerdevices)<br/> | Gets information about the pointer devices attached to the system.<br/> |
| [**GetRawPointerDeviceData**](/windows/win32/api/winuser/nf-winuser-getrawpointerdevicedata)<br/> | Gets the raw input data from the pointer device. <br/> |
| [**InjectSyntheticPointerInput**](/windows/win32/api/winuser/nf-winuser-injectsyntheticpointerinput)<br/> | Simulates pointer input (pen or touch).<br/> |
| [**RegisterPointerDeviceNotifications**](/windows/win32/api/winuser/nf-winuser-registerpointerdevicenotifications)<br/> | Registers a window to process the [**WM_POINTERDEVICECHANGE**](../inputmsg/wm-pointerdevicechange.md), [**WM_POINTERDEVICEINRANGE**](../inputmsg/wm-pointerdeviceinrange.md), and [**WM_POINTERDEVICEOUTOFRANGE**](../inputmsg/wm-pointerdeviceoutofrange.md) pointer device notifications.<br/> |

## Related topics

[Pointer Device Input Stack Reference](unified-input-stack-reference.md)
