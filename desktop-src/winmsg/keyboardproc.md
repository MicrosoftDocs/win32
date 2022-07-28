---
UID: 
title: KeyboardProc callback function
description: The system calls this function gets a message function and there is a keyboard message to process.
old-location: 
ms.assetid: na
ms.date: 04/05/2019
ms.keywords: 
ms.topic: reference
req.header: 
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
- APIRef
api_type: 
api_location: 
api_name: 
targetos: Windows
req.typenames: 
req.redist: 
---

# KeyboardProc function

## Description

An application-defined or library-defined callback function used with the [SetWindowsHookEx](/windows/desktop/api/winuser/nf-winuser-setwindowshookexw) function.
The system calls this function whenever an application calls the [GetMessage](/windows/desktop/api/winuser/nf-winuser-getmessage) or [PeekMessage](/windows/desktop/api/winuser/nf-winuser-peekmessagew) function and there is a keyboard message ([WM_KEYUP](/windows/desktop/inputdev/wm-keyup) or [WM_KEYDOWN](/windows/desktop/inputdev/wm-keydown)) to be processed.

The **HOOKPROC** type defines a pointer to this callback function.
**KeyboardProc** is a placeholder for the application-defined or library-defined function name.

```cpp
LRESULT CALLBACK KeyboardProc(
  _In_ int    code,
  _In_ WPARAM wParam,
  _In_ LPARAM lParam
);
```

## Parameters

### code [in]

Type: **int**

A code the hook procedure uses to determine how to process the message.
If *code* is less than zero, the hook procedure must pass the message to the [CallNextHookEx](/windows/desktop/api/winuser/nf-winuser-callnexthookex) function without further processing and should return the value returned by **CallNextHookEx**.
This parameter can be one of the following values.

| Value | Meaning |
|-------|---------|
| **HC_ACTION** 0 | The *wParam* and *lParam* parameters contain information about a keystroke message. |
| **HC_NOREMOVE** 3 | The *wParam* and *lParam* parameters contain information about a keystroke message, and the keystroke message has not been removed from the message queue. (An application called the **PeekMessage** function, specifying the **PM_NOREMOVE** flag.) |

### wParam [in]

Type: **WPARAM**

The [virtual-key code](/windows/desktop/inputdev/virtual-key-codes) of the key that generated the keystroke message.

### lParam [in]

Type: **LPARAM**

The repeat count, scan code, extended-key flag, context code, previous key-state flag, and transition-state flag.
For more information about The *lParam* parameter, see [Keystroke Message Flags](/windows/desktop/inputdev/about-keyboard-input).
The following table describes the bits of this value.

| Bits | Description |
|-------|---------|
| 0-15 | The repeat count. The value is the number of times the keystroke is repeated as a result of the user's holding down the key. |
| 16-23 | The scan code. The value depends on the OEM. |
| 24 | Indicates whether the key is an extended key, such as a function key or a key on the numeric keypad. The value is 1 if the key is an extended key; otherwise, it is 0. |
| 25-28 | Reserved. |
| 29 | The context code. The value is 1 if the ALT key is down; otherwise, it is 0. |
| 30 | The previous key state. The value is 1 if the key is down before the message is sent; it is 0 if the key is up. |
| 31 | The transition state. The value is 0 if the key is being pressed and 1 if it is being released. |

## Returns

Type: **LRESULT**

If *code* is less than zero, the hook procedure must return the value returned by **CallNextHookEx**.

If *code* is greater than or equal to zero, and the hook procedure did not process the message, it is highly recommended that you call **CallNextHookEx** and return the value it returns; otherwise, other applications that have installed [WH_KEYBOARD](about-hooks.md) hooks will not receive hook notifications and may behave incorrectly as a result.
If the hook procedure processed the message, it may return a nonzero value to prevent the system from passing the message to the rest of the hook chain or the target window procedure.

## Remarks

An application installs the hook procedure by specifying the **WH_KEYBOARD** hook type and a pointer to the hook procedure in a call to the **SetWindowsHookEx** function.

This hook may be called in the context of the thread that installed it.
The call is made by sending a message to the thread that installed the hook.
Therefore, the thread that installed the hook must have a message loop.

## See also

- [CallNextHookEx](/windows/desktop/api/winuser/nf-winuser-callnexthookex)
- [GetMessage](/windows/desktop/api/winuser/nf-winuser-getmessage)
- [PeekMessage](/windows/desktop/api/winuser/nf-winuser-peekmessagew)
- [SetWindowsHookEx](/windows/desktop/api/winuser/nf-winuser-setwindowshookexw)
- [WM_KEYUP](/windows/desktop/inputdev/wm-keyup)
- [WM_KEYDOWN](/windows/desktop/inputdev/wm-keydown)
- [Hooks](hooks.md)
- [Keyboard Input](keyboard-input.md)
- [About Keyboard Input](about-keyboard-input.md)
