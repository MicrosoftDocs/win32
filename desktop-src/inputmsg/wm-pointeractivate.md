---
title: WM_POINTERACTIVATE message
description: Sent to an inactive window when a primary pointer generates a WM_POINTERDOWN over the window.
ms.assetid: 4eec37da-227c-4be1-bf0b-99704caa1322
keywords:
- WM_POINTERACTIVATE message Input Messages and Notifications
topic_type:
- apiref
api_name:
- WM_POINTERACTIVATE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: article
ms.date: 02/03/2020
---

# WM_POINTERACTIVATE message

Sent to an inactive window when a primary pointer generates a [**WM_POINTERDOWN**](wm-pointerdown.md) over the window. As long as the message remains unhandled, it travels up the parent window chain until it is reaches the top-level window. Applications can respond to this message to specify whether they wish to be activated.

A window receives this message through its [**WindowProc**](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.


```C++
#define WM_POINTERACTIVATE             0x024B
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Contains the pointer identifier and additional information. Use the following macros to retrieve this information.

[**GET_POINTERID_WPARAM**](/previous-versions/windows/desktop/api)(wParam): pointer identifier

[**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85))(wParam): hit-test value returned from processing the [**WM_NCHITTEST**](../inputdev/wm-nchittest.md) message.

</dd> <dt>

*lParam* 
</dt> <dd>

Contains the handle to the top-level window of the window being activated.

</dd> </dl>

## Return value

If an application processes this message, it should return one of the values described in the Remarks section.

If the application does not process this message, it should call [**DefWindowProc**](/windows/win32/api/winuser/nf-winuser-defwindowproca).

## Remarks

An application can handle this message and return one of the following values to determine how the system processes the activation and the activating input:

-   PA_ACTIVATE
-   PA_NOACTIVATE

It is important to note that, when the user is interacting with the system with multiple simultaneous pointers, the activation opportunity that the **WM_POINTERACTIVATE** message represents is available to applications only for the first of those pointers. Applications should, therefore, be aware that they may still receive input from pointers while they are inactive.

If the application does not handle this message, [**DefWindowProc**](/windows/win32/api/winuser/nf-winuser-defwindowproca) passes the message to the parent window.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Messages](messages.md)
</dt> </dl>

 

