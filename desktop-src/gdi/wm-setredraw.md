---
description: An application sends the WM\_SETREDRAW message to a window to allow changes in that window to be redrawn or to prevent changes in that window from being redrawn.
ms.assetid: 0085a55e-7bf6-4eb6-a649-832b685db1cc
title: WM_SETREDRAW message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_SETREDRAW message

An application sends the **WM\_SETREDRAW** message to a window to allow changes in that window to be redrawn or to prevent changes in that window from being redrawn.

To send this message, call the [**SendMessage**](/windows/win32/api/winuser/nf-winuser-sendmessage) function with the following parameters.


```C++
SendMessage( 
  (HWND) hWnd,              
  WM_SETREDRAW,             
  (WPARAM) wParam,          
  (LPARAM) lParam            
);
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The redraw state. If this parameter is **TRUE**, the content can be redrawn after a change. If this parameter is **FALSE**, the content cannot be redrawn after a change.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

An application returns zero if it processes this message.

## Remarks

This message can be useful if an application must add several items to a list box. The application can call this message with *wParam* set to **FALSE**, add the items, and then call the message again with *wParam* set to **TRUE**. Finally, the application can call [**RedrawWindow**](/windows/desktop/api/Winuser/nf-winuser-redrawwindow)(*hWnd*, **NULL**, **NULL**, RDW\_ERASE \| RDW\_FRAME \| RDW\_INVALIDATE \| RDW\_ALLCHILDREN) to cause the list box to be repainted.

> [!Note]  
> [**RedrawWindow**](/windows/desktop/api/Winuser/nf-winuser-redrawwindow) with the specified flags is used instead of [**InvalidateRect**](/windows/desktop/api/Winuser/nf-winuser-invalidaterect) because the former is necessary for some controls that have nonclient area on their own, or have window styles that cause them to be given a nonclient area (such as **WS\_THICKFRAME**, **WS\_BORDER**, or **WS\_EX\_CLIENTEDGE**). If the control does not have a nonclient area, **RedrawWindow** with these flags will do only as much invalidation as **InvalidateRect** would.

 

If the application sends the **WM\_SETREDRAW** message to a hidden window, the window becomes visible (that is, the operating system adds the **WS\_VISIBLE** style to the window).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Painting and Drawing Overview](painting-and-drawing.md)
</dt> <dt>

[Painting and Drawing Messages](painting-and-drawing-messages.md)
</dt> <dt>

[**RedrawWindow**](/windows/desktop/api/Winuser/nf-winuser-redrawwindow)
</dt> </dl>

 

 
