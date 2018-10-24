---
Description: Broadcast to every window following a theme change event. Examples of theme change events are the activation of a theme, the deactivation of a theme, or a transition from one theme to another.
ms.assetid: 1a4051ac-cc6e-4520-ab66-d0a41a8a4c73
title: WM_THEMECHANGED message
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_THEMECHANGED message

Broadcast to every window following a theme change event. Examples of theme change events are the activation of a theme, the deactivation of a theme, or a transition from one theme to another.


```C++
#define WM_THEMECHANGED                 0x031A
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is reserved.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is reserved.

</dd> </dl>

## Return value

Type: **LRESULT**

If an application processes this message, it should return zero.

## Remarks

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/en-us/library/ms633573(v=VS.85).aspx) function.

> [!Note]  
> This message is posted by the operating system. Applications typically do not send this message.

 

Themes are specifications for the appearance of controls, so that the visual element of a control is treated separately from its functionality.

To release an existing theme handle, call [**CloseThemeData**](https://msdn.microsoft.com/library/Bb773287(v=VS.85).aspx). To acquire a new theme handle, use [**OpenThemeData**](https://msdn.microsoft.com/library/Bb759821(v=VS.85).aspx).

Following the **WM\_THEMECHANGED** broadcast, any existing theme handles are invalid. A theme-aware window should release and reopen any of its pre-existing theme handles when it receives the **WM\_THEMECHANGED** message. If the [**OpenThemeData**](https://msdn.microsoft.com/library/Bb759821(v=VS.85).aspx) function returns **NULL**, the window should paint unthemed.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Other Resources**
</dt> <dt>

[**CloseThemeData**](https://msdn.microsoft.com/library/Bb773287(v=VS.85).aspx)
</dt> <dt>

[**IsThemeActive**](https://msdn.microsoft.com/library/Bb759813(v=VS.85).aspx)
</dt> <dt>

[**OpenThemeData**](https://msdn.microsoft.com/library/Bb759821(v=VS.85).aspx)
</dt> </dl>

 

 




