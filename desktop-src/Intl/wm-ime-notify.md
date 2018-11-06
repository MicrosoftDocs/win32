---
Description: Sent to an application to notify it of changes to the IME window. A window receives this message through its WindowProc function.
ms.assetid: 20e064b8-2baf-4b4c-8341-36c3e4643eff
title: WM_IME_NOTIFY message
ms.topic: article
ms.date: 05/31/2018
---

# WM_IME_NOTIFY message

Sent to an application to notify it of changes to the IME window. A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/library/ms633573(v=VS.85).aspx) function.


```C++
LRESULT CALLBACK WindowProc(
  HWND  hwnd,       
  WM_IME_NOTIFY,   
  WPARAM wParam,   
  LPARAM lParam     
);
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

A handle to window.

</dd> <dt>

*wParam* 
</dt> <dd>

The command. This parameter can have one of the following values.

<dl>
<dd><a href="imn-changecandidate">IMN_CHANGECANDIDATE</a></dd> 
<dd><a href="imn-closecandidate">IMN_CLOSECANDIDATE</a></dd> 
<dd><a href="imn-closestatuswindow">IMN_CLOSESTATUSWINDOW</a></dd> 
<dd><a href="imn-guideline">IMN_GUIDELINE</a></dd> 
<dd><a href="imn-opencandidate">IMN_OPENCANDIDATE</a></dd> 
<dd><a href="imn-openstatuswindow">IMN_OPENSTATUSWINDOW</a></dd> 
<dd><a href="imn-setcandidatepos">IMN_SETCANDIDATEPOS</a></dd> 
<dd><a href="imn-setcompositionfont">IMN_SETCOMPOSITIONFONT</a></dd> 
<dd><a href="imn-setcompositionwindow">IMN_SETCOMPOSITIONWINDOW</a></dd> 
<dd><a href="imn-setconversionmode">IMN_SETCONVERSIONMODE</a></dd> 
<dd><a href="imn-setopenstatus">IMN_SETOPENSTATUS</a></dd> 
<dd><a href="imn-setsentencemode">IMN_SETSENTENCEMODE</a></dd> 
<dd><a href="imn-setstatuswindowpos">IMN_SETSTATUSWINDOWPOS</a></dd> 
</dl> 
</dd> 
<dt>

*lParam* 
</dt> <dd>

Command-specific data, with format dependent on the value of the *wParam* parameter. For more information, refer to the documentation for each command.

</dd> </dl>

## Return value

The return value depends on the command sent.

## Remarks

An application processes this message if it is responsible for managing the IME window.

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

[IMN_CHANGECANDIDATE](imn-changecandidate.md)
</dt> <dt>

[IMN_CLOSECANDIDATE](imn-closecandidate.md)
</dt> <dt>

[IMN_CLOSESTATUSWINDOW](imn-closestatuswindow.md)
</dt> <dt>

[IMN_GUIDELINE](imn-guideline.md)
</dt> <dt>

[IMN_OPENCANDIDATE](imn-opencandidate.md)
</dt> <dt>

[IMN_OPENSTATUSWINDOW](imn-openstatuswindow.md)
</dt> <dt>

[IMN_SETCANDIDATEPOS](imn-setcandidatepos.md)
</dt> <dt>

[IMN_SETCOMPOSITIONFONT](imn-setcompositionfont.md)
</dt> <dt>

[IMN_SETCOMPOSITIONWINDOW](imn-setcompositionwindow.md)
</dt> <dt>

[IMN_SETCONVERSIONMODE](imn-setconversionmode.md)
</dt> <dt>

[IMN_SETOPENSTATUS](imn-setopenstatus.md)
</dt> <dt>

[IMN_SETSENTENCEMODE](imn-setsentencemode.md)
</dt> <dt>

[IMN_SETSTATUSWINDOWPOS](imn-setstatuswindowpos.md)
</dt> </dl>

 

 




