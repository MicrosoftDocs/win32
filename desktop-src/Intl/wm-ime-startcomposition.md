---
description: Sent immediately before the IME generates the composition string as a result of a keystroke. A window receives this message through its WindowProc function.
ms.assetid: 2740d009-8685-4f70-9b01-67b71f4ddcbd
title: WM_IME_STARTCOMPOSITION message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_IME\_STARTCOMPOSITION message

Sent immediately before the IME generates the composition string as a result of a keystroke. A window receives this message through its [*WindowProc*](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.


```C++
LRESULT CALLBACK WindowProc(
  HWND  hwnd,                
  WM_IME_STARTCOMPOSITION,  
  WPARAM wParam,            
  LPARAM lParam             
);
```



## Parameters

This message has no parameters.

<dl></dl>

## Return value

This message has no return value.

## Remarks

This message is a notification to an IME window to open its composition window. An application should process this message if it displays composition characters itself.

If an application has created an IME window, it should pass this message to that window. The [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function processes the message by passing it to the default IME window.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Input Method Manager](input-method-manager.md)
</dt> <dt>

[Input Method Manager Messages](input-method-manager-messages.md)
</dt> </dl>

 

 
