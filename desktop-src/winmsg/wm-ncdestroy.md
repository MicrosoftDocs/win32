---
Description: Notifies a window that its nonclient area is being destroyed. The DestroyWindow function sends the WM\_NCDESTROY message to the window following the WM\_DESTROY message.
ms.assetid: 64ab268d-0e90-4401-81d3-a4da64196001
title: WM_NCDESTROY message
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_NCDESTROY message

Notifies a window that its nonclient area is being destroyed. The [**DestroyWindow**](https://msdn.microsoft.com/en-us/library/ms632682(v=VS.85).aspx) function sends the **WM\_NCDESTROY** message to the window following the [**WM\_DESTROY**](wm-destroy.md) message.[**WM\_DESTROY**](wm-destroy.md) is used to free the allocated memory object associated with the window.

The **WM\_NCDESTROY** message is sent after the child windows have been destroyed. In contrast, [**WM\_DESTROY**](wm-destroy.md) is sent before the child windows are destroyed.

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/en-us/library/ms633573(v=VS.85).aspx) function.


```C++
#define WM_NCDESTROY                    0x0082
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

Type: **LRESULT**

If an application processes this message, it should return zero.

## Remarks

This message frees any memory internally allocated for the window.

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

[**DestroyWindow**](https://msdn.microsoft.com/en-us/library/ms632682(v=VS.85).aspx)
</dt> <dt>

[**WM\_DESTROY**](wm-destroy.md)
</dt> <dt>

[**WM\_NCCREATE**](wm-nccreate.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 




