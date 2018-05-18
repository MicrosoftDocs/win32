---
Description: 'Indicates a request to terminate an application, and is generated when the application calls the PostQuitMessage function. This message causes the GetMessage function to return zero.'
ms.assetid: 'a9bff5dc-cab8-4e08-838e-d92c87c265d6'
title: 'WM\_QUIT message'
---

# WM\_QUIT message

Indicates a request to terminate an application, and is generated when the application calls the [**PostQuitMessage**](postquitmessage.md) function. This message causes the [**GetMessage**](getmessage.md) function to return zero.


```C++
#define WM_QUIT                         0x0012
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The exit code given in the [**PostQuitMessage**](postquitmessage.md) function.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

Type: **LRESULT**

This message does not have a return value because it causes the message loop to terminate before the message is sent to the application's window procedure.

## Remarks

The **WM\_QUIT** message is not associated with a window and therefore will never be received through a window's window procedure. It is retrieved only by the [**GetMessage**](getmessage.md) or [**PeekMessage**](peekmessage.md) functions.

Do not post the **WM\_QUIT** message using the [**PostMessage**](postmessage.md) function; use [**PostQuitMessage**](postquitmessage.md).

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

[**GetMessage**](getmessage.md)
</dt> <dt>

[**PeekMessage**](peekmessage.md)
</dt> <dt>

[**PostQuitMessage**](postquitmessage.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 




