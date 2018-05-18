---
Description: 'Sent to an application when the operating system is about to change the current IME. A window receives this message through its WindowProc function.'
ms.assetid: '5559b3ab-8d81-4f33-b0af-d05489371328'
title: 'WM\_IME\_SELECT message'
---

# WM\_IME\_SELECT message

Sent to an application when the operating system is about to change the current IME. A window receives this message through its [*WindowProc*](_win32_windowproc_cpp) function.


```C++
LRESULT CALLBACK WindowProc(
 HWND  hwnd,       
 WM_IME_SELECT,   
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

Selection indicator. This parameter specifies **TRUE** if the indicated IME is selected. The parameter is set to **FALSE** if the specified IME is no longer selected.

</dd> <dt>

*lParam* 
</dt> <dd>

Input locale identifier associated with the IME.

</dd> </dl>

## Return value

This message has no return value.

## Remarks

An application that has created an IME window should pass this message to that window so that it can retrieve the keyboard layout handle to the newly selected IME.

The [**DefWindowProc**](_win32_defwindowproc_cpp) function processes this message by passing the information to the default IME window.

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
</dt> </dl>

 

 




