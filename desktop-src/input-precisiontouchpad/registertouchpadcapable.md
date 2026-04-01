---
title: RegisterTouchpadCapableWindow and RegisterTouchpadCapableThread functions (Winuser.h)
description: Registers a window or thread as touchpad-capable, enabling WM_POINTER messages for touchpad two-finger gestures and touchpad-aware behavior for related APIs.
ms.topic: reference
ms.date: 03/28/2026
---

# RegisterTouchpadCapableWindow and RegisterTouchpadCapableThread functions

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Registers the specified window, or current thread, as touchpad-capable to the system.

## Syntax

```cpp
WINUSERAPI
BOOL
WINAPI
RegisterTouchpadCapableWindow(
    _In_ HWND hWnd,
    _In_ BOOL fEnable);

WINUSERAPI
BOOL
WINAPI
RegisterTouchpadCapableThread(
    _In_ BOOL fEnable);
```

## Parameters

**RegisterTouchpadCapableWindow**

<dl>
<dt><em>hWnd</em></dt>
<dd>

A handle to the window to be registered or unregistered as touchpad-capable.

</dd>
<dt><em>fEnable</em></dt>
<dd>

**TRUE** to register the window as touchpad-capable; **FALSE** to unregister it.

</dd>
</dl>

**RegisterTouchpadCapableThread**

<dl>
<dt><em>fEnable</em></dt>
<dd>

**TRUE** to register the current thread as touchpad-capable; **FALSE** to unregister it.

</dd>
</dl>

## Return value

If the function succeeds, the return value is nonzero.

If the function fails, the return value is zero. To get extended error information, call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror). Registration can fail if the system does not support registering as touchpad-capable, or if trying to unregister the thread and the thread is not currently registered as capable.

## Remarks

By registering as touchpad-capable, the following system functionality will change:

- [**GetPointerDevices**](/windows/win32/api/winuser/nf-winuser-getpointerdevices) will now include touchpads in its device list.
- [**GetCurrentInputMessageSource**](/windows/win32/api/winuser/nf-winuser-getcurrentinputmessagesource) for touchpad-originated mouse messages will return **IMDT_TOUCHPAD** as the device type instead of **IMDT_MOUSE**.
- [**RegisterPointerDeviceNotifications**](/windows/win32/api/winuser/nf-winuser-registerpointerdevicenotifications) will produce messages for touchpads (both device arrival/departure as well as contacts in/out of range).
- The window (or all windows on the thread) will receive **WM_POINTER** messages for touchpad two-finger gestures (pans and zooms).
- If these messages are forwarded to [**DefWindowProc**](/windows/win32/api/winuser/nf-winuser-defwindowproca), they will be converted into mouse wheel messages just as the system does today for non-touchpad-capable windows/threads.

**RegisterTouchpadCapableWindow** — Registering a window is "last caller wins" – the window's touchpad capability is enabled or disabled based on the most recent call to the API. The expectation is that the owner of the window will register as capable during initialization – components should not register a window as capable if they cannot control how it handles the **WM_POINTER** messages it will consequently receive.

**RegisterTouchpadCapableThread** — The system keeps track of how many times the thread has been registered as capable, so if the thread is registered as capable, it should be unregistered when no longer needed. A thread can use **RegisterTouchpadCapableThread** to temporarily register as capable to call APIs that have dependent behavior and then unregister so that the thread's original state is preserved.

Since **GetPointerDevices** and **GetCurrentInputMessageSource** do not take a window in their parameters, their behavior will only change when the entire thread is touchpad-capable, to avoid compatibility issues when opting in a single window on an otherwise-unaware thread.

> [!IMPORTANT]
> The behavior for some of the system's touchpad settings is implemented within the Interaction Context APIs for performing gesture recognition on pointer input. These include whether panning and/or zooming have been explicitly disabled, and the direction of content motion for panning. Future system updates may introduce more functionality as well. It is highly recommended, therefore, to use the Interaction Context APIs for gesture recognition when registering as touchpad-capable and receiving the pointer input directly, so that the user experiences uniform behavior across all applications. If not using these APIs, it is important to query the user's touchpad settings and respect the ones related to gesture recognition, if applicable to the application's user experience. The introduction of new system settings would require application updates, however — if using the Interaction Context APIs, these new settings would automatically work as expected.

> Specifically, the new [**ProcessPointerFramesInteractionContext2** or **BufferPointerPacketsInteractionContext2**](processpointerframesinteractioncontext2.md) should be used, as these provide the full pointer payload to the Interaction Context, rather than just the POINTER_INFO. Future enhancements to gesture recognition may take this information into consideration. The WinRT [**PhysicalGestureRecognizer**](physicalgesturerecognizer.md) class uses these APIs internally.

## Requirements

| Requirement | Value |
|-----|-----|
| Minimum supported client | Windows 11 \[desktop apps only\] |
| Minimum supported server | None supported |
| Header | Winuser.h (include Windows.h) |
| Library | User32.lib |
| DLL | User32.dll (ordinal 2689 for RegisterTouchpadCapableWindow, ordinal 2688 for RegisterTouchpadCapableThread) |

## See also

- [**GetPointerTouchpadInfo**](getpointertouchpadinfo.md)
- [**ReportWindowContentInertia**](reportwindowcontentinertia.md)
- [Precision Touchpad Programming Guide](precision-touchpad-guide.md)
- [Precision Touchpad Reference](precision-touchpad-reference.md)
