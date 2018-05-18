---
Description: 'Sent to an application when the IME window finds no space to extend the area for the composition window. A window receives this message through its WindowProc function.'
ms.assetid: 'd81d6438-c470-4ae5-8016-8d816bcba9b8'
title: 'WM\_IME\_COMPOSITIONFULL message'
---

# WM\_IME\_COMPOSITIONFULL message

Sent to an application when the IME window finds no space to extend the area for the composition window. A window receives this message through its [**WindowProc**](_win32_windowproc_cpp) function.


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

The IME window, instead of the IME, sends this notification message by the [**SendMessage**](_win32_sendmessage_cpp) function.

## Requirements



|                                     |                                                                                                          |
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

 

 




