---
title: WM_KEYUP message (Winuser.h)
description: Posted to the window with the keyboard focus when a nonsystem key is released. A nonsystem key is a key that is pressed when the ALT key is not pressed, or a keyboard key that is pressed when a window has the keyboard focus.
ms.assetid: 67d9d82d-fab0-4aec-a337-7a9cb2b0b586
keywords:
- WM_KEYUP message Keyboard and Mouse Input
topic_type:
- apiref
api_name:
- WM_KEYUP
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_KEYUP message

Posted to the window with the keyboard focus when a nonsystem key is released. A nonsystem key is a key that is pressed when the ALT key is *not* pressed, or a keyboard key that is pressed when a window has the keyboard focus.


```C++
#define WM_KEYUP                        0x0101
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The virtual-key code of the nonsystem key. See [Virtual-Key Codes](virtual-key-codes.md).

</dd> <dt>

*lParam* 
</dt> <dd>

The repeat count, scan code, extended-key flag, context code, previous key-state flag, and transition-state flag, as shown in the following table.



| Bits  | Meaning                                                                                                                                                                                                          |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0-15  | The repeat count for the current message. The value is the number of times the keystroke is autorepeated as a result of the user holding down the key. The repeat count is always 1 for a **WM\_KEYUP** message. |
| 16-23 | The scan code. The value depends on the OEM.                                                                                                                                                                     |
| 24    | Indicates whether the key is an extended key, such as the right-hand ALT and CTRL keys that appear on an enhanced 101- or 102-key keyboard. The value is 1 if it is an extended key; otherwise, it is 0.         |
| 25-28 | Reserved; do not use.                                                                                                                                                                                            |
| 29    | The context code. The value is always 0 for a **WM\_KEYUP** message.                                                                                                                                             |
| 30    | The previous key state. The value is always 1 for a **WM\_KEYUP** message.                                                                                                                                       |
| 31    | The transition state. The value is always 1 for a **WM\_KEYUP** message.                                                                                                                                         |

For more detail, see [Keystroke Message Flags](about-keyboard-input.md#keystroke-message-flags).
 

</dd> </dl>

## Return value

An application should return zero if it processes this message.

## Remarks

The [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function sends a [**WM\_SYSCOMMAND**](/windows/desktop/menurc/wm-syscommand) message to the top-level window if the F10 key or the ALT key was released. The *wParam* parameter of the message is set to SC\_KEYMENU.

For enhanced 101- and 102-key keyboards, extended keys are the right ALT and CTRL keys on the main section of the keyboard; the INS, DEL, HOME, END, PAGE UP, PAGE DOWN, and arrow keys in the clusters to the left of the numeric keypad; and the divide (/) and ENTER keys in the numeric keypad. Other keyboards may support the extended-key bit in the *lParam* parameter.

Applications must pass *wParam* to [**TranslateMessage**](/windows/desktop/api/winuser/nf-winuser-translatemessage) without altering it at all.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca)
</dt> <dt>

[**TranslateMessage**](/windows/desktop/api/winuser/nf-winuser-translatemessage)
</dt> <dt>

[**WM\_KEYDOWN**](wm-keydown.md)
</dt> <dt>

[**WM\_SYSCOMMAND**](/windows/desktop/menurc/wm-syscommand)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Keyboard Input](keyboard-input.md)
</dt> </dl>

 

