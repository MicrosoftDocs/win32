---
description: Associates a new large or small icon with a window. The system displays the large icon in the ALT+TAB dialog box, and the small icon in the window caption.
ms.assetid: c86620f2-893b-46f8-8254-1d7c4c142f37
title: WM_SETICON message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_SETICON message

Associates a new large or small icon with a window. The system displays the large icon in the ALT+TAB dialog box, and the small icon in the window caption.


```C++
#define WM_SETICON                      0x0080
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The type of icon to be set. This parameter can be one of the following values.



| Value                                                                                                                                                                                                       | Meaning                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| <span id="ICON_BIG"></span><span id="icon_big"></span><dl> <dt>**ICON\_BIG**</dt> <dt>1</dt> </dl>       | Set the large icon for the window.<br/> |
| <span id="ICON_SMALL"></span><span id="icon_small"></span><dl> <dt>**ICON\_SMALL**</dt> <dt>0</dt> </dl> | Set the small icon for the window.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

A handle to the new large or small icon. If this parameter is **NULL**, the icon indicated by *wParam* is removed.

</dd> </dl>

## Return value

Type: **LRESULT**

The return value is a handle to the previous large or small icon, depending on the value of *wParam*. It is **NULL** if the window previously had no icon of the type indicated by *wParam*.

## Remarks

The [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function returns a handle to the previous large or small icon associated with the window, depending on the value of *wParam*.

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

[**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca)
</dt> <dt>

[**WM\_GETICON**](wm-geticon.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 
