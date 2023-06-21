---
description: A message that is sent to all top-level windows when the SystemParametersInfo function changes a system-wide setting or when policy settings have changed.
ms.assetid: 77174e06-a25b-440a-9e9c-4fd5979c433c
title: WM_SETTINGCHANGE message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_SETTINGCHANGE message

A message that is sent to all top-level windows when the [**SystemParametersInfo**](/windows/win32/api/winuser/nf-winuser-systemparametersinfoa) function changes a system-wide setting or when policy settings have changed.

Applications should send **WM\_SETTINGCHANGE** to all top-level windows when they make changes to system parameters. (This message cannot be sent directly to a window.) To send the **WM\_SETTINGCHANGE** message to all top-level windows, use the [**SendMessageTimeout**](/windows/win32/api/winuser/nf-winuser-sendmessagetimeouta) function with the *hwnd* parameter set to **HWND\_BROADCAST**.

A window receives this message through its [**WindowProc**](/windows/win32/api/winuser/nc-winuser-wndproc) function.


```C++
#define WM_WININICHANGE                 0x001A
#define WM_SETTINGCHANGE                WM_WININICHANGE
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

When the system sends this message as a result of a [**SystemParametersInfo**](/windows/win32/api/winuser/nf-winuser-systemparametersinfoa) call, the *wParam* parameter is the value of the *uiAction* parameter passed to the **SystemParametersInfo** function. For a list of values, see **SystemParametersInfo**.

When the system sends this message as a result of a change in policy settings, this parameter indicates the type of policy that was applied. This value is 1 if computer policy was applied or zero if user policy was applied.

When the system sends this message as a result of a change in locale settings, this parameter is zero.

When an application sends this message, this parameter must be **NULL**.

</dd> <dt>

*lParam* 
</dt> <dd>

When the system sends this message as a result of a [**SystemParametersInfo**](/windows/win32/api/winuser/nf-winuser-systemparametersinfoa) call, *lParam* is a pointer to a string that indicates the area containing the system parameter that was changed. This parameter does not usually indicate which specific system parameter changed. (Note that some applications send this message with *lParam* set to **NULL**.) In general, when you receive this message, you should check and reload any system parameter settings that are used by your application.

This string can be the name of a registry key or the name of a section in the Win.ini file. When the string is a registry name, it typically indicates only the leaf node in the registry, not the full path.

When the system sends this message as a result of a change in policy settings, this parameter points to the string "Policy".

When the system sends this message as a result of a change in locale settings, this parameter points to the string "intl".

To effect a change in the environment variables for the system or the user, broadcast this message with *lParam* set to the string "Environment".

</dd> </dl>

## Return value

Type: **LRESULT**

If you process this message, return zero.

## Remarks

The *lParam* parameter indicates which system metric has changed, for example, "ConvertibleSlateMode" if the CONVERTIBLESLATEMODE indicator was toggled or "SystemDockMode" if the DOCKED indicator was toggled.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Policy Events](/previous-versions/windows/desktop/Policy/policy-events)
</dt> <dt>

[**SendMessageTimeout**](/windows/win32/api/winuser/nf-winuser-sendmessagetimeouta)
</dt> <dt>

[**SystemParametersInfo**](/windows/win32/api/winuser/nf-winuser-systemparametersinfoa)
</dt> </dl>

 

 
