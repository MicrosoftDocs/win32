---
Description: 'An application sends the WM\_FONTCHANGE message to all top-level windows in the system after changing the pool of font resources.'
ms.assetid: '4774308e-2f18-4a35-a769-56871f3c29a2'
title: 'WM\_FONTCHANGE message'
---

# WM\_FONTCHANGE message

An application sends the **WM\_FONTCHANGE** message to all top-level windows in the system after changing the pool of font resources.

To send this message, call the [**SendMessage**](_win32_sendmessage_cpp) function with the following parameters.


```C++
SendMessage( 
  (HWND)  hWnd,              
  WM_FONTCHANGE,            
  (WPARAM)  wParam,          
  (LPARAM)  lParam            
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

An application that adds or removes fonts from the system (for example, by using the [**AddFontResource**](addfontresource.md) or [**RemoveFontResource**](removefontresource.md) function) should send this message to all top-level windows.

To send the **WM\_FONTCHANGE** message to all top-level windows, an application can call the **SendMessage** function with the *hwnd* parameter set to HWND\_BROADCAST.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Fonts and Text Overview](fonts-and-text.md)
</dt> <dt>

[Font and Text Messages](font-and-text-messages.md)
</dt> <dt>

[**AddFontResource**](addfontresource.md)
</dt> <dt>

[**RemoveFontResource**](removefontresource.md)
</dt> </dl>

 

 




