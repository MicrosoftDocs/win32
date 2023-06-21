---
description: Sent to an application when a window is activated. A window receives this message through its WindowProc function.
ms.assetid: ba1e7877-1612-4f2f-aced-0dd982352ad6
title: WM_IME_SETCONTEXT message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_IME\_SETCONTEXT message

Sent to an application when a window is activated. A window receives this message through its [*WindowProc*](/windows/win32/api/winuser/nc-winuser-wndproc) function.


```C++
LRESULT CALLBACK WindowProc(
  HWND  hwnd,  
  WM_IME_SETCONTEXT,  
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

**TRUE** if the window is active, and **FALSE** otherwise.

</dd> <dt>

*lParam* 
</dt> <dd>

Display options. This parameter can have one or more of the following values.



| Value                                                                                                                                                                                                   | Meaning                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <span id="ISC_SHOWUICOMPOSITIONWINDOW"></span><span id="isc_showuicompositionwindow"></span><dl> <dt>**ISC\_SHOWUICOMPOSITIONWINDOW**</dt> </dl> | Show the composition window by user interface window.<br/>          |
| <span id="ISC_SHOWUIGUIDWINDOW"></span><span id="isc_showuiguidwindow"></span><dl> <dt>**ISC\_SHOWUIGUIDWINDOW**</dt> </dl>                      | Show the guide window by user interface window.<br/>                |
| <span id="ISC_SHOWUISOFTKBD"></span><span id="isc_showuisoftkbd"></span><dl> <dt>**ISC\_SHOWUISOFTKBD**</dt> </dl>                               | Show the soft keyboard by user interface window.<br/>               |
| <span id="ISC_SHOWUICANDIDATEWINDOW"></span><span id="isc_showuicandidatewindow"></span><dl> <dt>**ISC\_SHOWUICANDIDATEWINDOW**</dt> </dl>       | Show the candidate window of index 0 by user interface window.<br/> |
| <dl> <dt>ISC\_SHOWUICANDIDATEWINDOW << 1</dt> </dl>                                                                                        | Show the candidate window of index 1 by user interface window.<br/> |
| <dl> <dt>ISC\_SHOWUICANDIDATEWINDOW << 2</dt> </dl>                                                                                        | Show the candidate window of index 2 by user interface window.<br/> |
| <dl> <dt>ISC\_SHOWUICANDIDATEWINDOW << 3</dt> </dl>                                                                                        | Show the candidate window of index 3 by user interface window.<br/> |



 

</dd> </dl>

## Return value

Returns the value returned by [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) or [**ImmIsUIMessage**](/windows/desktop/api/Imm/nf-imm-immisuimessagea).

## Remarks

If the application has created an IME window, it should call [**ImmIsUIMessage**](/windows/desktop/api/Imm/nf-imm-immisuimessagea). Otherwise, it should pass this message to [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca).

If the application draws the composition window, the default IME window does not have to show its composition window. In this case, the application must clear the **ISC\_SHOWUICOMPOSITIONWINDOW** value from the *lParam* parameter before passing the message to [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) or [**ImmIsUIMessage**](/windows/desktop/api/Imm/nf-imm-immisuimessagea). To display a certain user interface window, an application should remove the corresponding value so that the IME will not display it.

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

[**ImmIsUIMessage**](/windows/desktop/api/Imm/nf-imm-immisuimessagea)
</dt> </dl>

 

 
