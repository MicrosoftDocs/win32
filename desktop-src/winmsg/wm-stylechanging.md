---
description: Sent to a window when the SetWindowLong function is about to change one or more of the window's styles.
ms.assetid: 71034362-3f67-49ae-bbbf-d38853ababb3
title: WM_STYLECHANGING message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_STYLECHANGING message

Sent to a window when the [**SetWindowLong**](/windows/win32/api/winuser/nf-winuser-setwindowlonga) function is about to change one or more of the window's styles.

A window receives this message through its [**WindowProc**](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.


```C++
#define WM_STYLECHANGING                0x007C
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Indicates whether the window's styles or extended window styles are changing. This parameter can be one or more of the following values.



| Value                                                                                                                                                                                                            | Meaning                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <span id="GWL_EXSTYLE"></span><span id="gwl_exstyle"></span><dl> <dt>**GWL\_EXSTYLE**</dt> <dt>-20</dt> </dl> | The extended window styles are changing.<br/> |
| <span id="GWL_STYLE"></span><span id="gwl_style"></span><dl> <dt>**GWL\_STYLE**</dt> <dt>-16</dt> </dl>       | The window styles are changing.<br/>          |



 

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**STYLESTRUCT**](/windows/win32/api/winuser/ns-winuser-stylestruct) structure that contains the proposed new styles for the window. An application can examine the styles and, if necessary, change them.

</dd> </dl>

## Return value

Type: **LRESULT**

An application should return zero if it processes this message.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**STYLESTRUCT**](/windows/win32/api/winuser/ns-winuser-stylestruct)
</dt> <dt>

[**WM\_STYLECHANGED**](wm-stylechanged.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 
