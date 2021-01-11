---
description: Performs no operation. An application sends the WM\_NULL message if it wants to post a message that the recipient window will ignore.
ms.assetid: edbcfba6-7b79-4d53-84e3-2e4227e17369
title: WM_NULL message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_NULL message

Performs no operation. An application sends the **WM\_NULL** message if it wants to post a message that the recipient window will ignore.

A window receives this message through its [**WindowProc**](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.


```C++
#define WM_NULL                         0x0000
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

## Return value

Type: **LRESULT**

An application returns zero if it processes this message.

## Remarks

For example, if an application has installed a **WH\_GETMESSAGE** hook and wants to prevent a message from being processed, the [**GetMsgProc**](/previous-versions/windows/desktop/legacy/ms644981(v=vs.85)) callback function can change the message number to **WM\_NULL** so the recipient will ignore it.

As another example, an application can check if a window is responding to messages by sending the **WM\_NULL** message with the [**SendMessageTimeout**](/windows/win32/api/winuser/nf-winuser-sendmessagetimeouta) function.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Windows Overview](windows.md)
</dt> </dl>

 

 
