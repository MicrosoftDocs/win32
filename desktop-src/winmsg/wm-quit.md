---
Description: Indicates a request to terminate an application, and is generated when the application calls the PostQuitMessage function. This message causes the GetMessage function to return zero.
ms.assetid: a9bff5dc-cab8-4e08-838e-d92c87c265d6
title: WM\_QUIT message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WM\_QUIT message

Indicates a request to terminate an application, and is generated when the application calls the [**PostQuitMessage**](/windows/win32/Winuser/nf-winuser-postquitmessage?branch=master) function. This message causes the [**GetMessage**](/windows/win32/Winuser/nf-engextcpp-extexception-getmessage?branch=master) function to return zero.


```C++
#define WM_QUIT                         0x0012
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The exit code given in the [**PostQuitMessage**](/windows/win32/Winuser/nf-winuser-postquitmessage?branch=master) function.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

Type: **LRESULT**

This message does not have a return value because it causes the message loop to terminate before the message is sent to the application's window procedure.

## Remarks

The **WM\_QUIT** message is not associated with a window and therefore will never be received through a window's window procedure. It is retrieved only by the [**GetMessage**](/windows/win32/Winuser/nf-engextcpp-extexception-getmessage?branch=master) or [**PeekMessage**](/windows/win32/Winuser/nf-winuser-peekmessagea?branch=master) functions.

Do not post the **WM\_QUIT** message using the [**PostMessage**](/windows/win32/Winuser/nf-winuser-postmessagea?branch=master) function; use [**PostQuitMessage**](/windows/win32/Winuser/nf-winuser-postquitmessage?branch=master).

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**GetMessage**](/windows/win32/Winuser/nf-engextcpp-extexception-getmessage?branch=master)
</dt> <dt>

[**PeekMessage**](/windows/win32/Winuser/nf-winuser-peekmessagea?branch=master)
</dt> <dt>

[**PostQuitMessage**](/windows/win32/Winuser/nf-winuser-postquitmessage?branch=master)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 




