---
description: The WM\_SYSCOLORCHANGE message is sent to all top-level windows when a change is made to a system color setting.
ms.assetid: ffe61768-86d6-4ea8-ae2d-1095a9afa925
title: WM_SYSCOLORCHANGE message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_SYSCOLORCHANGE message

The **WM\_SYSCOLORCHANGE** message is sent to all top-level windows when a change is made to a system color setting.

A window receives this message through its [**WindowProc**](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.


```C++
LRESULT CALLBACK WindowProc(
  HWND hwnd, 
  UINT  uMsg, 
  WPARAM wParam, 
  LPARAM lParam     
);
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Remarks

The system sends a [**WM\_PAINT**](wm-paint.md) message to any window that is affected by a system color change.

Applications that have brushes using the existing system colors should delete those brushes and re-create them using the new system colors.

Top level windows that use common controls must forward the **WM\_SYSCOLORCHANGE** message to the controls; otherwise, the controls will not be notified of the color change. This ensures that the colors used by your common controls are consistent with those used by other user interface objects. For example, a toolbar control uses the "3D Objects" color to draw its buttons. If the user changes the 3D Objects color but the **WM\_SYSCOLORCHANGE** message is not forwarded to the toolbar, the toolbar buttons will remain in their original color while the color of other buttons in the system changes.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Colors Overview](colors.md)
</dt> <dt>

[Color Messages](color-messages.md)
</dt> <dt>

[**WM\_PAINT**](wm-paint.md)
</dt> </dl>

 

 
