---
description: The WM\_DEVMODECHANGE message is sent to all top-level windows whenever the user changes device-mode settings.
ms.assetid: 06b625a8-7584-4a98-b8e7-f1de668c274e
title: WM_DEVMODECHANGE message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_DEVMODECHANGE message

The **WM\_DEVMODECHANGE** message is sent to all top-level windows whenever the user changes device-mode settings.

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

*hwnd* 
</dt> <dd>

A handle to a window.

</dd> <dt>

*uMsg* 
</dt> <dd>

WM\_DEVMODECHANGE

</dd> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a string that specifies the device name.

</dd> </dl>

## Return value

An application should return zero if it processes this message.

## Remarks

This message cannot be sent directly to a window. To send the **WM\_DEVMODECHANGE** message to all top-level windows, use the [**SendMessageTimeout**](/windows/win32/api/winuser/nf-winuser-sendmessagetimeouta) function with the *hWnd* parameter set to HWND\_BROADCAST.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Device Contexts Overview](device-contexts.md)
</dt> <dt>

[Device Context Messages](device-context-messages.md)
</dt> </dl>

 

 
