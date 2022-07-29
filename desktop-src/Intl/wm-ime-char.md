---
description: Sent to an application when the IME gets a character of the conversion result. A window receives this message through its WindowProc function.
ms.assetid: 1e1353c3-5215-4829-a00a-2fee47a430eb
title: WM_IME_CHAR message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_IME\_CHAR message

Sent to an application when the IME gets a character of the conversion result. A window receives this message through its [**WindowProc**](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.


```C++
LRESULT CALLBACK WindowProc(
 HWND  hwnd,
 WM_IME_CHAR,
 WPARAM wParam,
 LPARAM lParam   
);
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

A handle to window.

</dd> <dt>

*wParam* 
</dt> <dd>

**DBCS:** A single-byte or double-byte character value. For a double-byte character, (BYTE)(wParam >> 8) contains the lead byte. Note that the parentheses are necessary because the cast operator has higher precedence than the shift operator.

**Unicode:** A Unicode character value.

</dd> <dt>

*lParam* 
</dt> <dd>

The repeat count, scan code, extended key flag, context code, previous key state flag, and transition state flag, with values as defined below.



| Bit   | Meaning                                                                              |
|-------|--------------------------------------------------------------------------------------|
| 0-15  | Repeat count. Since the first byte and second byte are continuous, this is always 1. |
| 16-23 | Scan code for a complete Asian character.                                            |
| 24    | Extended key.                                                                        |
| 25-28 | Not used.                                                                            |
| 29    | Context code.                                                                        |
| 30    | Previous key state.                                                                  |
| 31    | Transition state.                                                                    |



 

</dd> </dl>

## Remarks

Unlike the [**WM\_CHAR**](../inputdev/wm-char.md) message for a non-Unicode window, this message can include double-byte and single-byte character values. For a Unicode window, this message is the same as WM\_CHAR.

For a non-Unicode window, if the WM\_IME\_CHAR message includes a double-byte character and the application passes this message to [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca), the IME converts this message into two WM\_CHAR messages, each containing one byte of the double-byte character.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also
- [Input Method Manager](input-method-manager.md)
- [Input Method Manager Messages](input-method-manager-messages.md)
- [Keyboard Input (Keyboard and Mouse Input)](../inputdev/keyboard-input.md)
- [About Keyboard Input](../inputdev/about-keyboard-input.md)

 

 
