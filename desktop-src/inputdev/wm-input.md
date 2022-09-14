---
title: WM_INPUT message (Winuser.h)
description: Sent to the window that is getting raw input. A window receives this message through its WindowProc function.
ms.assetid: a014d68c-841c-4120-b752-4b3fac60e12d
keywords:
- WM_INPUT message Keyboard and Mouse Input
topic_type:
- apiref
api_name:
- WM_INPUT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 04/17/2020
---

# WM\_INPUT message

Sent to the window that is getting raw input.

A window receives this message through its [**WindowProc**](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.


```cpp
#define WM_INPUT 0x00FF
```

## Parameters

<dl> <dt>

*wParam*

</dt> <dd>

The input code. Use [**GET\_RAWINPUT\_CODE\_WPARAM**](/windows/win32/api/winuser/nf-winuser-get_rawinput_code_wparam) macro to get the value.

Can be one of the following values:

| Value | Meaning |
|---|---|
| <span id="RIM_INPUT"></span><span id="rim_input"></span><dl> <dt>**RIM\_INPUT**</dt> <dt>0</dt> </dl> | Input occurred while the application was in the foreground. </br> The application must call [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) so the system can perform cleanup. |
| <span id="RIM_INPUTSINK"></span><span id="rim_inputsink"></span><dl> <dt>**RIM\_INPUTSINK**</dt> <dt>1</dt> </dl> | Input occurred while the application was not in the foreground. |

</dd> <dt>

*lParam* 

</dt> <dd>

A **HRAWINPUT** handle to the [**RAWINPUT**](/windows/win32/api/winuser/ns-winuser-rawinput) structure that contains the raw input from the device. To get the raw data, use this handle in the call to [**GetRawInputData**](/windows/win32/api/winuser/nf-winuser-getrawinputdata).

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Remarks

Raw input is available only when the application calls [**RegisterRawInputDevices**](/windows/win32/api/winuser/nf-winuser-registerrawinputdevices) with valid device specifications.

## Requirements

| Requirement | Value |
|--------------------------|-------------------------------------------|
| Minimum supported client | Windows XP \[desktop apps only\] |
| Minimum supported server | Windows Server 2003 \[desktop apps only\] |
| Header | <dl> <dt>**Winuser.h (include Windows.h)** </dt> </dl> |

## See also

**Reference**

[**GetRawInputData**](/windows/win32/api/winuser/nf-winuser-getrawinputdata)

[**RegisterRawInputDevices**](/windows/win32/api/winuser/nf-winuser-registerrawinputdevices)

[**RAWINPUT**](/windows/win32/api/winuser/ns-winuser-rawinput)

[**GET\_RAWINPUT\_CODE\_WPARAM**](/windows/win32/api/winuser/nf-winuser-get_rawinput_code_wparam)

**Conceptual**

[Raw Input](raw-input.md)
