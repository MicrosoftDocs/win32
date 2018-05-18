---
Description: 'Sent by an application to direct the IME window to carry out the requested command.'
ms.assetid: '5d3b7f8a-57c9-41e3-8022-9a3f515fc32e'
title: 'WM\_IME\_CONTROL message'
---

# WM\_IME\_CONTROL message

Sent by an application to direct the IME window to carry out the requested command. The application uses this message to control the IME window that it has created. To send this message, the application calls the [**SendMessage**](_win32_sendmessage_cpp) function with the following parameters.


```C++
SendMessage(
  HWND   hwnd,
  WM_IME_CONTROL, 
  WPARAM wParam,
  LPARAM lParam             
);
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

Handle to the window.

</dd> <dt>

*wParam* 
</dt> <dd>

The command. This parameter can have one of the following values:

<dl> <dd>[IMC\_CLOSESTATUSWINDOW](imc-closestatuswindow.md)</dd> <dd>[IMC\_GETCANDIDATEPOS](imc-getcandidatepos.md)</dd> <dd>[IMC\_GETCOMPOSITIONFONT](imc-getcompositionfont.md)</dd> <dd>[IMC\_GETCOMPOSITIONWINDOW](imc-getcompositionwindow.md)</dd> <dd>[IMC\_GETSTATUSWINDOWPOS](imc-getstatuswindowpos.md)</dd> <dd>[IMC\_OPENSTATUSWINDOW](imc-openstatuswindow.md)</dd> <dd>[IMC\_SETCANDIDATEPOS](imc-setcandidatepos.md)</dd> <dd>[IMC\_SETCOMPOSITIONFONT](imc-setcompositionfont.md)</dd> <dd>[IMC\_SETCOMPOSITIONWINDOW](imc-setcompositionwindow.md)</dd> <dd>[IMC\_SETSTATUSWINDOWPOS](imc-setstatuswindowpos.md)</dd> </dl> </dd> <dt>

*lParam* 
</dt> <dd>

Command-specific data, with format dependent on the value of the *wParam* parameter. For more information, refer to the documentation for each command.

</dd> </dl>

## Return value

The message returns a command-specific value.

## Requirements



|                                     |                                                                                                                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                                                      |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h); </dt> <dt>Imm.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Input Method Manager](input-method-manager.md)
</dt> <dt>

[Input Method Manager Messages](input-method-manager-messages.md)
</dt> <dt>

[IMC\_CLOSESTATUSWINDOW](imc-closestatuswindow.md)
</dt> <dt>

[IMC\_GETCANDIDATEPOS](imc-getcandidatepos.md)
</dt> <dt>

[IMC\_GETCOMPOSITIONFONT](imc-getcompositionfont.md)
</dt> <dt>

[IMC\_GETCOMPOSITIONWINDOW](imc-getcompositionwindow.md)
</dt> <dt>

[IMC\_GETSTATUSWINDOWPOS](imc-getstatuswindowpos.md)
</dt> <dt>

[IMC\_OPENSTATUSWINDOW](imc-openstatuswindow.md)
</dt> <dt>

[IMC\_SETCANDIDATEPOS](imc-setcandidatepos.md)
</dt> <dt>

[IMC\_SETCOMPOSITIONFONT](imc-setcompositionfont.md)
</dt> <dt>

[IMC\_SETCOMPOSITIONWINDOW](imc-setcompositionwindow.md)
</dt> <dt>

[IMC\_SETSTATUSWINDOWPOS](imc-setstatuswindowpos.md)
</dt> </dl>

 

 




