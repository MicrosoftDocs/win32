---
Description: Indicates a request to terminate an application, and is generated when the application calls the PostQuitMessage function. This message causes the GetMessage function to return zero.
ms.assetid: a9bff5dc-cab8-4e08-838e-d92c87c265d6
title: WM_QUIT message
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_QUIT message

Indicates a request to terminate an application, and is generated when the application calls the [**PostQuitMessage**](https://msdn.microsoft.com/en-us/library/ms644945(v=VS.85).aspx) function. This message causes the [**GetMessage**](https://msdn.microsoft.com/en-us/library/ms644936(v=VS.85).aspx) function to return zero.


```C++
#define WM_QUIT                         0x0012
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The exit code given in the [**PostQuitMessage**](https://msdn.microsoft.com/en-us/library/ms644945(v=VS.85).aspx) function.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

Type: **LRESULT**

This message does not have a return value because it causes the message loop to terminate before the message is sent to the application's window procedure.

## Remarks

The **WM\_QUIT** message is not associated with a window and therefore will never be received through a window's window procedure. It is retrieved only by the [**GetMessage**](https://msdn.microsoft.com/en-us/library/ms644936(v=VS.85).aspx) or [**PeekMessage**](https://msdn.microsoft.com/en-us/library/ms644943(v=VS.85).aspx) functions.

Do not post the **WM\_QUIT** message using the [**PostMessage**](https://msdn.microsoft.com/en-us/library/ms644944(v=VS.85).aspx) function; use [**PostQuitMessage**](https://msdn.microsoft.com/en-us/library/ms644945(v=VS.85).aspx).

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

[**GetMessage**](https://msdn.microsoft.com/en-us/library/ms644936(v=VS.85).aspx)
</dt> <dt>

[**PeekMessage**](https://msdn.microsoft.com/en-us/library/ms644943(v=VS.85).aspx)
</dt> <dt>

[**PostQuitMessage**](https://msdn.microsoft.com/en-us/library/ms644945(v=VS.85).aspx)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 




