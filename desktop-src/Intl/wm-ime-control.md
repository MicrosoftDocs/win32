---
description: Sent by an application to direct the IME window to carry out the requested command.
ms.assetid: 5d3b7f8a-57c9-41e3-8022-9a3f515fc32e
title: WM_IME_CONTROL message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM_IME_CONTROL message

Sent by an application to direct the IME window to carry out the requested command. The application uses this message to control the IME window that it has created. To send this message, the application calls the [**SendMessage**](/windows/win32/api/winuser/nf-winuser-sendmessage) function with the following parameters.


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

<dl>
<dd><a href="imc-closestatuswindow.md">IMC_CLOSESTATUSWINDOW</a></dd> 
<dd><a href="imc-getcandidatepos.md">IMC_GETCANDIDATEPOS</a></dd> 
<dd><a href="imc-getcompositionfont.md">IMC_GETCOMPOSITIONFONT</a></dd> 
<dd><a href="imc-getcompositionwindow.md">IMC_GETCOMPOSITIONWINDOW</a></dd> 
<dd><a href="imc-getstatuswindowpos.md">IMC_GETSTATUSWINDOWPOS</a></dd> 
<dd><a href="imc-openstatuswindow.md">IMC_OPENSTATUSWINDOW</a></dd> 
<dd><a href="imc-setcandidatepos.md">IMC_SETCANDIDATEPOS</a></dd> 
<dd><a href="imc-setcompositionfont.md">IMC_SETCOMPOSITIONFONT</a>></dd> 
<dd><a href="imc-setcompositionwindow.md">IMC_SETCOMPOSITIONWINDOW</a></dd> 
<dd><a href="imc-setstatuswindowpos.md">IMC_SETSTATUSWINDOWPOS</a></dd> 
</dl>
</dd>

<dt>

*lParam* 
</dt> <dd>

Command-specific data, with format dependent on the value of the *wParam* parameter. For more information, refer to the documentation for each command.

</dd> </dl>

## Return value

The message returns a command-specific value.

## Requirements



| Requirement | Value |
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

[IMC_CLOSESTATUSWINDOW](imc-closestatuswindow.md)
</dt> <dt>

[IMC_GETCANDIDATEPOS](imc-getcandidatepos.md)
</dt> <dt>

[IMC_GETCOMPOSITIONFONT](imc-getcompositionfont.md)
</dt> <dt>

[IMC_GETCOMPOSITIONWINDOW](imc-getcompositionwindow.md)
</dt> <dt>

[IMC_GETSTATUSWINDOWPOS](imc-getstatuswindowpos.md)
</dt> <dt>

[IMC_OPENSTATUSWINDOW](imc-openstatuswindow.md)
</dt> <dt>

[IMC_SETCANDIDATEPOS](imc-setcandidatepos.md)
</dt> <dt>

[IMC_SETCOMPOSITIONFONT](imc-setcompositionfont.md)
</dt> <dt>

[IMC_SETCOMPOSITIONWINDOW](imc-setcompositionwindow.md)
</dt> <dt>

[IMC_SETSTATUSWINDOWPOS](imc-setstatuswindowpos.md)
</dt> </dl>

 

 
