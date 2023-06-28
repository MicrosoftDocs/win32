---
description: A message that is sent whenever there is a change in the system time.
ms.assetid: 94b5b6f7-04bb-4e0a-848b-e2b31ffc2938
title: WM_TIMECHANGE message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_TIMECHANGE message

A message that is sent whenever there is a change in the system time.

A window receives this message through its [**WindowProc**](/windows/win32/api/winuser/nc-winuser-wndproc) function.


```C++
LRESULT CALLBACK WindowProc(
  HWND hwnd,       // handle to window
  UINT uMsg,       // message identifier
  WPARAM wParam,   // not used; must be zero
  LPARAM lParam    // not used; must be zero
);
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

A handle to window.

</dd> <dt>

*uMsg* 
</dt> <dd>

**WM\_TIMECHANGE** identifier.

</dd> <dt>

*wParam* 
</dt> <dd>

Not used; must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

An application should return zero if it processes this message.

## Remarks

An application should not broadcast this message, because the system will broadcast this message when the application changes the system time.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**SendMessage**](/windows/win32/api/winuser/nf-winuser-sendmessage)
</dt> </dl>

 

