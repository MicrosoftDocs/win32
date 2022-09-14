---
description: Sent to an application when the IME ends composition. A window receives this message through its WindowProc function.
ms.assetid: d0f05524-4dfc-45b2-9476-6f1244190de5
title: WM_IME_ENDCOMPOSITION message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_IME\_ENDCOMPOSITION message

Sent to an application when the IME ends composition. A window receives this message through its [**WindowProc**](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.


```C++
LRESULT CALLBACK WindowProc(
  HWND  hwnd,      
  WM_IME_ENDCOMPOSITION,  
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

An application should process this message if it displays composition characters itself.

If the application has created an IME window, it should pass this message to that window. The [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca)  function processes this message by passing it to the default IME window.

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

 

 
