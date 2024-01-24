---
title: WM_SYSKEYUP message (Winuser.h)
description: Posted to the window with the keyboard focus when the user releases a key that was pressed while the ALT key was held down.
ms.assetid: a4f62575-fb84-4390-a1d1-1a62629de55f
keywords:
- WM_SYSKEYUP message Keyboard and Mouse Input
topic_type:
- apiref
api_name:
- WM_SYSKEYUP
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_SYSKEYUP message

Posted to the window with the keyboard focus when the user releases a key that was pressed while the ALT key was held down. It also occurs when no window currently has the keyboard focus; in this case, the **WM\_SYSKEYUP** message is sent to the active window. The window that receives the message can distinguish between these two contexts by checking the context code in the *lParam* parameter.

A window receives this message through its [**WindowProc**](/windows/win32/api/winuser/nc-winuser-wndproc) function.


```C++
#define WM_SYSKEYUP                     0x0105
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The virtual-key code of the key being released. See [**Virtual-Key Codes**](virtual-key-codes.md).

</dd> <dt>

*lParam* 
</dt> <dd>

The repeat count, scan code, extended-key flag, context code, previous key-state flag, and transition-state flag, as shown in the following table.



| Bits  | Meaning                                                                                                                                                                                                                       |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0-15  | The repeat count for the current message. The value is the number of times the keystroke is autorepeated as a result of the user holding down the key. The repeat count is always one for a **WM\_SYSKEYUP** message.         |
| 16-23 | The scan code. The value depends on the OEM.                                                                                                                                                                                  |
| 24    | Indicates whether the key is an extended key, such as the right-hand ALT and CTRL keys that appear on an enhanced 101- or 102-key keyboard. The value is 1 if it is an extended key; otherwise, it is zero.                   |
| 25-28 | Reserved; do not use.                                                                                                                                                                                                         |
| 29    | The context code. The value is 1 if the ALT key is down while the key is released; it is zero if the **WM\_SYSKEYUP** message is posted to the active window because no window has the keyboard focus. |
| 30    | The previous key state. The value is always 1 for a **WM\_SYSKEYUP** message.                                                                                                                                                 |
| 31    | The transition state. The value is always 1 for a **WM\_SYSKEYUP** message.                                                                                                                                                   |

For more details, see [Keystroke Message Flags](about-keyboard-input.md#keystroke-message-flags).

</dd> </dl>

## Return value

An application should return zero if it processes this message.

## Remarks

The [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function sends a [**WM\_SYSCOMMAND**](/windows/desktop/menurc/wm-syscommand) message to the top-level window if the F10 key or the ALT key was released. The *wParam* parameter of the message is set to **SC\_KEYMENU**.

When the context code is zero, the message can be passed to the [**TranslateAccelerator**](/windows/desktop/api/winuser/nf-winuser-translateacceleratora) function, which will handle it as though it were a normal key message instead of a character-key message. This allows accelerator keys to be used with the active window even if the active window does not have the keyboard focus.

For enhanced 101- and 102-key keyboards, extended keys are the right ALT and CTRL keys on the main section of the keyboard; the INS, DEL, HOME, END, PAGE UP, PAGE DOWN, and arrow keys in the clusters to the left of the numeric keypad; and the divide (/) and ENTER keys in the numeric keypad. Other keyboards may support the extended-key bit in the *lParam* parameter.

For non-U.S. enhanced 102-key keyboards, the right ALT key is handled as a CTRL+ALT key. The following table shows the sequence of messages that result when the user presses and releases this key.



| Message                           | Virtual-key code |
|-----------------------------------|------------------|
| [**WM\_KEYDOWN**](wm-keydown.md) | **VK\_CONTROL**  |
| [**WM\_KEYDOWN**](wm-keydown.md) | **VK\_MENU**     |
| [**WM\_KEYUP**](wm-keyup.md)     | **VK\_CONTROL**  |
| **WM\_SYSKEYUP**                  | **VK\_MENU**     |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also
- [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca)
- [**TranslateAccelerator**](/windows/desktop/api/winuser/nf-winuser-translateacceleratora)
- [**WM\_SYSCOMMAND**](/windows/desktop/menurc/wm-syscommand)
- [**WM\_SYSKEYDOWN**](wm-syskeydown.md)
- [Keyboard Input](keyboard-input.md)
- [About Keyboard Input](about-keyboard-input.md)

 

