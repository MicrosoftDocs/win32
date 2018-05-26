---
title: WM\_KEYDOWN message
description: Posted to the window with the keyboard focus when a nonsystem key is pressed. A nonsystem key is a key that is pressed when the ALT key is not pressed.
ms.assetid: 0e37149f-445c-4b20-ad68-fdf39428ac91
keywords:
- WM_KEYDOWN message Keyboard and Mouse Input
topic_type:
- apiref
api_name:
- WM_KEYDOWN
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WM\_KEYDOWN message

Posted to the window with the keyboard focus when a nonsystem key is pressed. A nonsystem key is a key that is pressed when the ALT key is not pressed.


```C++
#define WM_KEYDOWN                      0x0100
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The virtual-key code of the nonsystem key. See [Virtual-Key Codes](virtual-key-codes.md).

</dd> <dt>

*lParam* 
</dt> <dd>

The repeat count, scan code, extended-key flag, context code, previous key-state flag, and transition-state flag, as shown following.



| Bits  | Meaning                                                                                                                                                                                                                                                               |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0-15  | The repeat count for the current message. The value is the number of times the keystroke is autorepeated as a result of the user holding down the key. If the keystroke is held long enough, multiple messages are sent. However, the repeat count is not cumulative. |
| 16-23 | The scan code. The value depends on the OEM.                                                                                                                                                                                                                          |
| 24    | Indicates whether the key is an extended key, such as the right-hand ALT and CTRL keys that appear on an enhanced 101- or 102-key keyboard. The value is 1 if it is an extended key; otherwise, it is 0.                                                              |
| 25-28 | Reserved; do not use.                                                                                                                                                                                                                                                 |
| 29    | The context code. The value is always 0 for a **WM\_KEYDOWN** message.                                                                                                                                                                                                |
| 30    | The previous key state. The value is 1 if the key is down before the message is sent, or it is zero if the key is up.                                                                                                                                                 |
| 31    | The transition state. The value is always 0 for a **WM\_KEYDOWN** message.                                                                                                                                                                                            |



 

</dd> </dl>

## Return value

An application should return zero if it processes this message.

## Remarks

If the F10 key is pressed, the [**DefWindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633572) function sets an internal flag. When **DefWindowProc** receives the [**WM\_KEYUP**](wm-keyup.md) message, the function checks whether the internal flag is set and, if so, sends a [**WM\_SYSCOMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms646360) message to the top-level window. The **WM\_SYSCOMMAND** parameter of the message is set to SC\_KEYMENU.

Because of the autorepeat feature, more than one **WM\_KEYDOWN** message may be posted before a [**WM\_KEYUP**](wm-keyup.md) message is posted. The previous key state (bit 30) can be used to determine whether the **WM\_KEYDOWN** message indicates the first down transition or a repeated down transition.

For enhanced 101- and 102-key keyboards, extended keys are the right ALT and CTRL keys on the main section of the keyboard; the INS, DEL, HOME, END, PAGE UP, PAGE DOWN, and arrow keys in the clusters to the left of the numeric keypad; and the divide (/) and ENTER keys in the numeric keypad. Other keyboards may support the extended-key bit in the *lParam* parameter.

Applications must pass *wParam* to [**TranslateMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644955) without altering it at all.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**DefWindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633572)
</dt> <dt>

[**TranslateMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644955)
</dt> <dt>

[**WM\_CHAR**](wm-char.md)
</dt> <dt>

[**WM\_KEYUP**](wm-keyup.md)
</dt> <dt>

[**WM\_SYSCOMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms646360)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Keyboard Input](keyboard-input.md)
</dt> </dl>

 

 





