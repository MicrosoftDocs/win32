---
title: WM_INPUT_DEVICE_CHANGE message (Winuser.h)
description: Sent to the window that registered to receive raw input. A window receives this message through its WindowProc function.
ms.assetid: 2f98d8ea-b47b-4dea-9c38-f9697b18053a
keywords:
- WM_INPUT_DEVICE_CHANGE message Keyboard and Mouse Input
topic_type:
- apiref
api_name:
- WM_INPUT_DEVICE_CHANGE
api_location:
- Winuser.h
api_type:
- HeaderDef
req.header: winuser.h
req.include-header: Windows.h
req.target-type: Windows
req.target-min-winverclnt: Windows Vista [desktop apps only]
req.target-min-winversvr: Windows Server 2008 [desktop apps only]
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_INPUT\_DEVICE\_CHANGE message

## -description

Sent to the window that registered to receive raw input. 

Raw input notifications is available only after the application calls [RegisterRawInputDevices](https://docs.microsoft.com/windows/win32/api/winuser/nf-winuser-registerrawinputdevices) with [RIDEV_DEVNOTIFY](https://docs.microsoft.com/windows/win32/api/winuser/ns-winuser-rawinputdevice) flag.

A window receives this message through its [**WindowProc**](https://docs.microsoft.com/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.

```C++
#define WM_INPUT_DEVICE_CHANGE          0x00FE
```

## -parameters

### -param wParam

Type: <b>WPARAM</b>

This parameter can be one of the following values.

| Value                    | Meaning                                    |
|--------------------------|--------------------------------------------|
| **GIDC\_ARRIVAL** </br>1 | A new device has been added to the system. </br> You can call [GetRawInputDeviceInfo](https://docs.microsoft.com/windows/win32/api/winuser/nf-winuser-getrawinputdeviceinfoa) to get more information regarding the device. |
| **GIDC\_REMOVAL** </br>2 | A device has been removed from the system. |

### -param lParam

Type: <b>LPARAM</b>

The **HANDLE** to the raw input device. 

## -returns

If an application processes this message, it should return zero.


## -see-also

<b>Conceptual</b>

[Raw Input](https://docs.microsoft.com/windows/desktop/inputdev/raw-input)

<b>Reference</b>

[RegisterRawInputDevices](https://docs.microsoft.com/windows/win32/api/winuser/nf-winuser-registerrawinputdevices)

[RAWINPUTDEVICE structure](https://docs.microsoft.com/windows/win32/api/winuser/ns-winuser-rawinputdevice)
 

 





