---
description: Sent to an application when the IME window finds no space to extend the area for the composition window. A window receives this message through its WindowProc function.
ms.assetid: d81d6438-c470-4ae5-8016-8d816bcba9b8
title: WM_IME_COMPOSITIONFULL message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_IME\_COMPOSITIONFULL message

Sent to an application when the IME window finds no space to extend the area for the composition window. A window receives this message through its [**WindowProc**](/windows/win32/api/winuser/nc-winuser-wndproc) function.


```C++
LRESULT CALLBACK WindowProc(
  HWND  hwnd,
  WM_IME_COMPOSITIONFULL, 
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

The application should use the [IMC\_SETCOMPOSITIONWINDOW](imc-setcompositionwindow.md) command to specify how the window should be displayed.

The IME window, instead of the IME, sends this notification message by the [**SendMessage**](/windows/win32/api/winuser/nf-winuser-sendmessage) function.

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
</dt> <dt>

[IMC\_SETCOMPOSITIONWINDOW](imc-setcompositionwindow.md)
</dt> </dl>

 

 
