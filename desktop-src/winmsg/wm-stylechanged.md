---
Description: Sent to a window after the SetWindowLong function has changed one or more of the windows styles.
ms.assetid: 37bc4e1a-f75d-4851-8dee-97fa2da90254
title: WM\_STYLECHANGED message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WM\_STYLECHANGED message

Sent to a window after the [**SetWindowLong**](setwindowlong.md) function has changed one or more of the window's styles.

A window receives this message through its [**WindowProc**](windowproc.md) function.


```C++
#define WM_STYLECHANGED                 0x007D
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Indicates whether the window's styles or extended window styles have changed. This parameter can be one or more of the following values.



| Value                                                                                                                                                                                                            | Meaning                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <span id="GWL_EXSTYLE"></span><span id="gwl_exstyle"></span><dl> <dt>**GWL\_EXSTYLE**</dt> <dt>-20</dt> </dl> | The extended window styles have changed.<br/> |
| <span id="GWL_STYLE"></span><span id="gwl_style"></span><dl> <dt>**GWL\_STYLE**</dt> <dt>-16</dt> </dl>       | The window styles have changed.<br/>          |



 

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**STYLESTRUCT**](stylestruct.md) structure that contains the new styles for the window. An application can examine the styles, but cannot change them.

</dd> </dl>

## Return value

Type: **LRESULT**

An application should return zero if it processes this message.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**SetWindowLong**](setwindowlong.md)
</dt> <dt>

[**STYLESTRUCT**](stylestruct.md)
</dt> <dt>

[**WM\_STYLECHANGING**](wm-stylechanging.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 




