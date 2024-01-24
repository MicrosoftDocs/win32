---
description: Sent to an application by the IME to notify the application of a key press and to keep message order. A window receives this message through its WindowProc function.
ms.assetid: db7075fb-b3d4-4d32-a0db-096d17d67c72
title: WM_IME_KEYDOWN message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_IME\_KEYDOWN message

Sent to an application by the IME to notify the application of a key press and to keep message order. A window receives this message through its [**WindowProc**](/windows/win32/api/winuser/nc-winuser-wndproc) function.


```C++
LRESULT CALLBACK WindowProc(
  HWND  hwnd,        
  WM_IME_KEYDOWN,  
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

Virtual key code of the key.

</dd> <dt>

*lParam* 
</dt> <dd>

Repeat count, scan code, extended key flag, context code, previous key state flag, and transition state flag, as shown in the following table.



| Bit   | Meaning                                                                     |
|-------|-----------------------------------------------------------------------------|
| 0-15  | Repeat count.                                                               |
| 16-23 | Scan code.                                                                  |
| 24    | Extended key. This value is 1 if it is an extended key. Otherwise, it is 0. |
| 25-28 | Not used.                                                                   |
| 29    | Context code. This value is always 0.                                       |
| 30    | Previous key state. This value is 1 if the key is down or 0 if it is up.    |
| 31    | Transition state. This value is always 0.                                   |



 

</dd> </dl>

## Return value

An application should return 0 if it processes this message.

## Remarks

An application can process this message or pass it to the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca)  function to generate a matching [**WM\_KEYDOWN**](../inputdev/wm-keydown.md) message.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

- [Input Method Manager](input-method-manager.md)
- [Input Method Manager Messages](input-method-manager-messages.md)
- [Keyboard Input (Keyboard and Mouse Input)](../inputdev/keyboard-input.md)
- [About Keyboard Input](../inputdev/about-keyboard-input.md)
