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

 

Passing a **WM\_SETREDRAW** message to the **DefWindowProc** function will remove the **WS\_VISIBLE** style from the window when *wParam* is set to **FALSE**. Although the window content will remain visible on screen, the [**IsWindowVisible**](/windows/desktop/api/winuser/nf-winuser-iswindowvisible) function will return **FALSE** when called on a window in this state. 

Passing a **WM\_SETREDRAW** message to the **DefWindowProc** function will add the **WS\_VISIBLE** style to the window, if not set, when *wParam* is set to **TRUE**. If the application sends the **WM\_SETREDRAW** message with *wParam* set to **TRUE** to a hidden window, the window becomes visible. 

**Windows 10 and later, Windows Server 2016 and later**: The system will set a property named *SysSetRedraw* on a window whose window procedure passes **WM\_SETREDRAW** messages to **DefWindowProc**. Applications can use the [**GetProp**](/windows/desktop/api/Winuser/nf-winuser-getpropa) function to get the property value when available. **GetProp** will return a non-zero value when redraw is disabled. **GetProp** will return zero when redraw is enabled, or when the window property does not exist. 


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

 

 
