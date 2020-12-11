---
title: WM_UNICHAR message (Winuser.h)
description: The WM\_UNICHAR message can be used by an application to post input to other windows.
ms.assetid: edbfcf14-0371-43ce-9676-eb10d964d0b7
keywords:
- WM_UNICHAR message Keyboard and Mouse Input
topic_type:
- apiref
api_name:
- WM_UNICHAR
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_UNICHAR message

The **WM\_UNICHAR** message can be used by an application to post input to other windows. This message contains the character code of the key that was pressed. (Test whether a target app can process **WM\_UNICHAR** messages by sending the message with *wParam* set to **UNICODE\_NOCHAR**.)


```C++
#define WM_UNICHAR                      0x0109
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The character code of the key.

If *wParam* is **UNICODE\_NOCHAR** and the application processes this message, then return **TRUE**. The [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function will return **FALSE** (the default).

If *wParam* is not **UNICODE\_NOCHAR**, return **FALSE**. The Unicode  [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) posts a [**WM\_CHAR**](wm-char.md) message with the same parameters and the ANSI **DefWindowProc** function posts either one or two **WM\_CHAR** messages with the corresponding ANSI character(s).

</dd> <dt>

*lParam* 
</dt> <dd>

The repeat count, scan code, extended-key flag, context code, previous key-state flag, and transition-state flag, as shown in the following table.



| Bits  | Meaning                                                                                                                                                                                                                                                               |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0-15  | The repeat count for the current message. The value is the number of times the keystroke is autorepeated as a result of the user holding down the key. If the keystroke is held long enough, multiple messages are sent. However, the repeat count is not cumulative. |
| 16-23 | The scan code. The value depends on the OEM.                                                                                                                                                                                                                          |
| 24    | Indicates whether the key is an extended key, such as the right-hand ALT and CTRL keys that appear on an enhanced 101- or 102-key keyboard. The value is 1 if it is an extended key; otherwise, it is 0.                                                              |
| 25-28 | Reserved; do not use.                                                                                                                                                                                                                                                 |
| 29    | The context code. The value is 1 if the ALT key is held down while the key is pressed; otherwise, the value is 0.                                                                                                                                                     |
| 30    | The previous key state. The value is 1 if the key is down before the message is sent, or it is 0 if the key is up.                                                                                                                                                    |
| 31    | The transition state. The value is 1 if the key is being released, or it is 0 if the key is being pressed.                                                                                                                                                            |

For more detail, see [Keystroke Message Flags](about-keyboard-input.md#keystroke-message-flags).

</dd> </dl>

## Return value

An application should return zero if it processes this message.

## Remarks

The **WM\_UNICHAR** message is similar to [**WM\_CHAR**](wm-char.md), but it uses Unicode Transformation Format (UTF)-32, whereas **WM\_CHAR** uses UTF-16.

This message is designed to send or post Unicode characters to ANSI windows and can handle Unicode Supplementary Plane characters.

Because there is not necessarily a one-to-one correspondence between keys pressed and character messages generated, the information in the high-order word of the *lParam* parameter is generally not useful to applications. The information in the high-order word applies only to the most recent [**WM\_KEYDOWN**](wm-keydown.md) message that precedes the posting of the **WM\_UNICHAR** message.

For enhanced 101- and 102-key keyboards, extended keys are the right ALT and the right CTRL keys on the main section of the keyboard; the INS, DEL, HOME, END, PAGE UP, PAGE DOWN and arrow keys in the clusters to the left of the numeric keypad; and the divide (/) and ENTER keys in the numeric keypad. Some other keyboards may support the extended-key bit in the *lParam* parameter.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**TranslateMessage**](/windows/desktop/api/winuser/nf-winuser-translatemessage)
</dt> <dt>

[**WM\_CHAR**](wm-char.md)
</dt> <dt>

[**WM\_KEYDOWN**](wm-keydown.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Keyboard Input](keyboard-input.md)
</dt> </dl>

 

