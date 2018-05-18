---
Description: 'Broadcast to every window following a theme change event. Examples of theme change events are the activation of a theme, the deactivation of a theme, or a transition from one theme to another.'
ms.assetid: '1a4051ac-cc6e-4520-ab66-d0a41a8a4c73'
title: 'WM\_THEMECHANGED message'
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

A window receives this message through its [**WindowProc**](windowproc.md) function.

> [!Note]  
> This message is posted by the operating system. Applications typically do not send this message.

 

Themes are specifications for the appearance of controls, so that the visual element of a control is treated separately from its functionality.

To release an existing theme handle, call [**CloseThemeData**](inet_CloseThemeData_cpp). To acquire a new theme handle, use [**OpenThemeData**](inet_OpenThemeData_cpp).

Following the **WM\_THEMECHANGED** broadcast, any existing theme handles are invalid. A theme-aware window should release and reopen any of its pre-existing theme handles when it receives the **WM\_THEMECHANGED** message. If the [**OpenThemeData**](inet_OpenThemeData_cpp) function returns **NULL**, the window should paint unthemed.

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

[**CloseThemeData**](inet_CloseThemeData_cpp)
</dt> <dt>

[**IsThemeActive**](inet_IsThemeActive_cpp)
</dt> <dt>

[**OpenThemeData**](inet_OpenThemeData_cpp)
</dt> </dl>

 

 




