---
description: Retrieves the font with which the control is currently drawing its text.
ms.assetid: a6d05ef5-9933-4d03-a677-a8328bf1cb7d
title: WM_GETFONT message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_GETFONT message

Retrieves the font with which the control is currently drawing its text.


```C++
#define WM_GETFONT                      0x0031
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used and must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used and must be zero.

</dd> </dl>

## Return value

Type: **HFONT**

The return value is a handle to the font used by the control, or **NULL** if the control is using the system font.

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

[**WM\_SETFONT**](wm-setfont.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 




