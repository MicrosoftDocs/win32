---
description: An application sends the WM\_WININICHANGE message to all top-level windows after making a change to the WIN.INI file. The SystemParametersInfo function sends this message after an application uses the function to change a setting in WIN.INI.
ms.assetid: 402f8d71-ad52-486d-be26-8b41a3f22045
title: WM_WININICHANGE message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_WININICHANGE message

An application sends the **WM\_WININICHANGE** message to all top-level windows after making a change to the WIN.INI file. The [**SystemParametersInfo**](/windows/win32/api/winuser/nf-winuser-systemparametersinfoa) function sends this message after an application uses the function to change a setting in WIN.INI.

> [!Note]  
> The **WM\_WININICHANGE** message is provided only for compatibility with earlier versions of the system. Applications should use the [**WM\_SETTINGCHANGE**](wm-settingchange.md) message.

 

A window receives this message through its [**WindowProc**](/windows/win32/api/winuser/nc-winuser-wndproc) function.


```C++
#define WM_WININICHANGE                 0x001A
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a string containing the name of the system parameter that was changed. For example, this string can be the name of a registry key or the name of a section in the Win.ini file. This parameter is not particularly useful in determining which system parameter changed. For example, when the string is a registry name, it typically indicates only the leaf node in the registry, not the whole path. In addition, some applications send this message with *lParam* set to **NULL**. In general, when you receive this message, you should check and reload any system parameter settings that are used by your application.

</dd> </dl>

## Return value

Type: **LRESULT**

If you process this message, return zero.

## Remarks

To send the **WM\_WININICHANGE** message to all top-level windows, use the [**SendMessage**](/windows/win32/api/winuser/nf-winuser-sendmessage) function with the *hWnd* parameter set to **HWND\_BROADCAST**.

Calls to functions that change WIN.INI may be mapped to the registry instead. This mapping occurs when WIN.INI and the section being changed are specified in the registry under the following key:

**HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\IniFileMapping**

The change in the storage location has no effect on the behavior of this message.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**SystemParametersInfo**](/windows/win32/api/winuser/nf-winuser-systemparametersinfoa)
</dt> </dl>

 

 
