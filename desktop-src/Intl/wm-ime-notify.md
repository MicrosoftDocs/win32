---
Description: Sent to an application to notify it of changes to the IME window. A window receives this message through its WindowProc function.
ms.assetid: 20e064b8-2baf-4b4c-8341-36c3e4643eff
title: WM\_IME\_NOTIFY message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WM\_IME\_NOTIFY message

Sent to an application to notify it of changes to the IME window. A window receives this message through its [**WindowProc**](_win32_windowproc_cpp) function.


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

<dl> <dd>[IMN\_CHANGECANDIDATE](imn-changecandidate.md)</dd> <dd>[IMN\_CLOSECANDIDATE](imn-closecandidate.md)</dd> <dd>[IMN\_CLOSESTATUSWINDOW](imn-closestatuswindow.md)</dd> <dd>[IMN\_GUIDELINE](imn-guideline.md)</dd> <dd>[IMN\_OPENCANDIDATE](imn-opencandidate.md)</dd> <dd>[IMN\_OPENSTATUSWINDOW](imn-openstatuswindow.md)</dd> <dd>[IMN\_SETCANDIDATEPOS](imn-setcandidatepos.md)</dd> <dd>[IMN\_SETCOMPOSITIONFONT](imn-setcompositionfont.md)</dd> <dd>[IMN\_SETCOMPOSITIONWINDOW](imn-setcompositionwindow.md)</dd> <dd>[IMN\_SETCONVERSIONMODE](imn-setconversionmode.md)</dd> <dd>[IMN\_SETOPENSTATUS](imn-setopenstatus.md)</dd> <dd>[IMN\_SETSENTENCEMODE](imn-setsentencemode.md)</dd> <dd>[IMN\_SETSTATUSWINDOWPOS](imn-setstatuswindowpos.md)</dd> </dl> </dd> <dt>

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

[IMN\_CHANGECANDIDATE](imn-changecandidate.md)
</dt> <dt>

[IMN\_CLOSECANDIDATE](imn-closecandidate.md)
</dt> <dt>

[IMN\_CLOSESTATUSWINDOW](imn-closestatuswindow.md)
</dt> <dt>

[IMN\_GUIDELINE](imn-guideline.md)
</dt> <dt>

[IMN\_OPENCANDIDATE](imn-opencandidate.md)
</dt> <dt>

[IMN\_OPENSTATUSWINDOW](imn-openstatuswindow.md)
</dt> <dt>

[IMN\_SETCANDIDATEPOS](imn-setcandidatepos.md)
</dt> <dt>

[IMN\_SETCOMPOSITIONFONT](imn-setcompositionfont.md)
</dt> <dt>

[IMN\_SETCOMPOSITIONWINDOW](imn-setcompositionwindow.md)
</dt> <dt>

[IMN\_SETCONVERSIONMODE](imn-setconversionmode.md)
</dt> <dt>

[IMN\_SETOPENSTATUS](imn-setopenstatus.md)
</dt> <dt>

[IMN\_SETSENTENCEMODE](imn-setsentencemode.md)
</dt> <dt>

[IMN\_SETSTATUSWINDOWPOS](imn-setstatuswindowpos.md)
</dt> </dl>

 

 




