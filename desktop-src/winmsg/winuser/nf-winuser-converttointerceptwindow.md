---
UID: NF:winuser.ConvertToInterceptWindow
description: Converts a window to an Intercept window, where windowing operations are intercepted (WM_INTERCEPTED_WINDOW_ACTION).
tech.root: winmsg
title: ConvertToInterceptWindow function
ms.topic: reference
ms.date: 3/22/2025
req.lib: 
req.dll: User32.dll
api_type:
 - DllExport
api_location:
 - user32.dll
api_name:
 - ConvertToInterceptWindow
f1_keywords:
 - ConvertToInterceptWindow
 - winuser/ConvertToInterceptWindow
dev_langs:
 - c++
helpviewer_keywords:
 - ConvertToInterceptWindow
targetos: Windows
ms.localizationpriority: low
---

# ConvertToInterceptWindow function

Converts the provided top level window to an Intercept window.

## Syntax

```cpp
BOOL ConvertToInterceptWindow(HWND topLevelWindow);
```

## Parameters

`topLevelWindow`

Type: **HWND**

Handle to the top-level window.

## Return value

Type: **BOOL**

If the function succeeds, the return value is nonzero.

If the function fails, the return value is zero. To get extended error
information, call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror).


> [!IMPORTANT]
> The API ConvertToInterceptWindow is a Limited Access Feature (see
[LimitedAccessFeatures class](/uwp/api/windows.applicationmodel.limitedaccessfeatures))
. For more information or to request an unlock token, please use the
[LAF Access Token Request Form](https://go.microsoft.com/fwlink/?linkid=2271232&clcid=0x409)
and select 'Remote App Windowing APIs' from the drop down.

## Remarks

> [!TIP]
> At this time, this function does not have an associated header file or library file. Your application can call [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) with the DLL name (`User32.dll`) to obtain a module handle. It can then call [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) with the module handle and the name of this function to get the function address.

An Intercept window is one where all windowing operations (calls to APIs like
[SetWindowPos](/windows/win32/api/winuser/nf-winuser-setwindowpos)
) are intercepted. Instead of modifying the window's position,
size, state, activation, etc, the window is notified of the intercepted changes
with a
[WM_INTERCEPTED_WINDOW_ACTION](ns-winuser-wminterceptedwindowaction.md)
message. The message contains a
[WINDOW_ACTION](ns-winuser-windowaction.md)
, which describes the changes. The Intercept window can apply
these changes using
[ApplyWindowAction](nf-winuser-applywindowaction.md).

`ConvertToInterceptWindow` should be called while creating the window or shortly
after. If the call succeeds, all future windowing operations done on the window
are Intercepted, not including ones caused by
[ApplyWindowAction](nf-winuser-applywindowaction.md).

Intercept windows have complete control over their window's position, size,
state, visibility and activation state. This can be used by Remote Desktop
applications to keep windows in sync between multiple machines and third party
apps, whose windowing behavior is not predictable.

There is no way to change an Intercept window back to a non-intercept window.
If an Intercept window chooses to accept default behavior, it can call
[ApplyWindowAction](nf-winuser-applywindowaction.md)
directly from the
[WM_INTERCEPTED_WINDOW_ACTION](ns-winuser-wminterceptedwindowaction.md)
message.

## Requirements

The window must be a top level window owned by the calling thread.


| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 11 [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | None |
| **Library** | None |
| **DLL** | User32.dll |
