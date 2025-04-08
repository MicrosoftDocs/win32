---
UID: NF:winuser.RegisterCloakedNotification
description: Allows applications to register or unregister a window for cloak state change notification.
tech.root: winmsg
title: RegisterCloakedNotification function
ms.topic: reference
ms.date: 2/25/2025
req.lib: 
req.dll: User32.dll
api_type:
 - DllExport
api_location:
 - user32.dll
api_name:
 - RegisterCloakedNotification
f1_keywords:
 - RegisterCloakedNotification
 - winuser/RegisterCloakedNotification
dev_langs:
 - c++
helpviewer_keywords:
 - RegisterCloakedNotification
targetos: Windows
ms.localizationpriority: low
---

# RegisterCloakedNotification function

Registers a window for cloak state change notifications.

## Syntax

```cpp
BOOL RegisterCloakedNotification(
    HWND hwnd,
    BOOL register);
```

## Parameters

`[in] hwnd`

Type: <b>HWND</b>

Handle to the window whose registration is changing.

`[in] register`

Type: <b>BOOL</b>

Indicates if the call is registering the window for cloak state change
notifications.

## Return value

Type: **BOOL**

If the function succeeds, the return value is nonzero.

If the function fails, the return value is zero. To get extended error
information, call <a href="/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror">GetLastError</a>.

## Remarks

When a window is registered for cloak change notifications the
[WM_CLOAKED_STATE_CHANGED](ns-winuser-wmcloakedstatechanged.md)
message will be sent to its window procedure when the window's cloak state
changes. A window that is registered for cloak change notifications will receive
the RegisterCloakedNotification can only be called from the thread that owns the
window being registered or unregistered for notifications.

> [!TIP]
> At this time, this function does not have an associated header file or library file. Your application can call [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) with the DLL name (`User32.dll`) to obtain a module handle. It can then call [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) with the module handle and the name of this function to get the function address.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 11 [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | None |
| **Library** | None |
| **DLL** | User32.dll |

## See also

[WM_CLOAKED_STATE_CHANGED](ns-winuser-wmcloakedstatechanged.md)

[DwmSetWindowAttribute](/windows/desktop/api/dwmapi/nf-dwmapi-dwmsetwindowattribute)