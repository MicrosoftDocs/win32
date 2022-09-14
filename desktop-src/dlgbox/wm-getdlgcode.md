---
title: WM_GETDLGCODE message (Winuser.h)
description: Sent to the window procedure associated with a control.
ms.assetid: 96d2caee-be6e-46e9-98b3-bffc3af1c003
keywords:
- WM_GETDLGCODE message Dialog Boxes
topic_type:
- apiref
api_name:
- WM_GETDLGCODE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_GETDLGCODE message

Sent to the window procedure associated with a control. By default, the system handles all keyboard input to the control; the system interprets certain types of keyboard input as dialog box navigation keys. To override this default behavior, the control can respond to the **WM\_GETDLGCODE** message to indicate the types of input it wants to process itself.


```C++
#define WM_GETDLGCODE                   0x0087
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The virtual key, pressed by the user, that prompted Windows to issue this notification. The handler must selectively handle these keys. For instance, the handler might accept and process **VK\_RETURN** but delegate **VK\_TAB** to the owner window. For a list of values, see [**Virtual-Key Codes**](/windows/desktop/inputdev/virtual-key-codes).

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**MSG**](/windows/win32/api/winuser/ns-winuser-msg) structure (or **NULL** if the system is performing a query).

</dd> </dl>

## Return value

The return value is one or more of the following values, indicating which type of input the application processes.



| Return code/value                                                                                                                                                | Description                                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**DLGC\_BUTTON**</dt> <dt>0x2000</dt> </dl>          | Button.<br/>                                                                                                         |
| <dl> <dt>**DLGC\_DEFPUSHBUTTON**</dt> <dt>0x0010</dt> </dl>   | Default push button.<br/>                                                                                            |
| <dl> <dt>**DLGC\_HASSETSEL**</dt> <dt>0x0008</dt> </dl>       | [**EM\_SETSEL**](/windows/desktop/Controls/em-setsel) messages.<br/>                                                           |
| <dl> <dt>**DLGC\_RADIOBUTTON**</dt> <dt>0x0040</dt> </dl>     | Radio button.<br/>                                                                                                   |
| <dl> <dt>**DLGC\_STATIC**</dt> <dt>0x0100</dt> </dl>          | Static control.<br/>                                                                                                 |
| <dl> <dt>**DLGC\_UNDEFPUSHBUTTON**</dt> <dt>0x0020</dt> </dl> | Non-default push button.<br/>                                                                                        |
| <dl> <dt>**DLGC\_WANTALLKEYS**</dt> <dt>0x0004</dt> </dl>     | All keyboard input.<br/>                                                                                             |
| <dl> <dt>**DLGC\_WANTARROWS**</dt> <dt>0x0001</dt> </dl>      | Direction keys.<br/>                                                                                                 |
| <dl> <dt>**DLGC\_WANTCHARS**</dt> <dt>0x0080</dt> </dl>       | [**WM\_CHAR**](/windows/desktop/inputdev/wm-char) messages.<br/>                                                                      |
| <dl> <dt>**DLGC\_WANTMESSAGE**</dt> <dt>0x0004</dt> </dl>     | All keyboard input (the application passes this message in the [**MSG**](/windows/win32/api/winuser/ns-winuser-msg) structure to the control).<br/> |
| <dl> <dt>**DLGC\_WANTTAB**</dt> <dt>0x0002</dt> </dl>         | TAB key.<br/>                                                                                                        |



 

## Remarks

Although the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function always returns zero in response to the **WM\_GETDLGCODE** message, the window procedure for the predefined control classes return a code appropriate for each class.

The **WM\_GETDLGCODE** message and the returned values are useful only with user-defined dialog box controls or standard controls modified by subclassing.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca)
</dt> <dt>

[**EM\_SETSEL**](/windows/desktop/Controls/em-setsel)
</dt> <dt>

[**MSG**](/windows/win32/api/winuser/ns-winuser-msg)
</dt> <dt>

[**WM\_CHAR**](/windows/desktop/inputdev/wm-char)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Dialog Boxes](dialog-boxes.md)
</dt> </dl>

 

