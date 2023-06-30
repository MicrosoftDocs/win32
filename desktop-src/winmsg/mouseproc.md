---
UID: 
title: MouseProc callback function
description: The system calls this function when an application calls a message function and there is a mouse message to be processed.
old-location: 
ms.assetid: na
ms.date: 04/05/2019
ms.keywords: 
ms.topic: reference
req.header: 
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
- APIRef
api_type: 
api_location: 
api_name: 
targetos: Windows
req.typenames: 
req.redist: 
---

# MouseProc function

## Description

An application-defined or library-defined callback function used with the [**SetWindowsHookExA**](/windows/win32/api/winuser/nf-winuser-setwindowshookexa)/[**SetWindowsHookExW**](/windows/win32/api/winuser/nf-winuser-setwindowshookexw) function. The system calls this function whenever an application calls the [**GetMessage**](/windows/win32/api/winuser/nf-winuser-getmessage) or [**PeekMessageA**](/windows/win32/api/winuser/nf-winuser-peekmessagea)/[**PeekMessageW**](/windows/win32/api/winuser/nf-winuser-peekmessagew) function and there is a mouse message to be processed.

The **HOOKPROC** type defines a pointer to this callback function. *MouseProc* is a placeholder for the application-defined or library-defined function name.

```cpp
LRESULT CALLBACK MouseProc(
  _In_ int    nCode,
  _In_ WPARAM wParam,
  _In_ LPARAM lParam
);
```

## Parameters

### nCode [in]

Type: **int**

A code that the hook procedure uses to determine how to process the message.

If *nCode* is less than zero, the hook procedure must pass the message to the [**CallNextHookEx**](/windows/desktop/api/winuser/nf-winuser-callnexthookex) function without further processing and should return the value returned by **CallNextHookEx**.

This parameter can be one of the following values.

| Value | Meaning |
|-------|---------|
| **HC_ACTION** 0 | The *wParam* and *lParam* parameters contain information about a mouse message. |
| **HC_NOREMOVE** 3 | The *wParam* and *lParam* parameters contain information about a mouse message, and the mouse message has not been removed from the message queue. (An application called the **PeekMessage** function, specifying the **PM_NOREMOVE** flag.) |

### wParam [in]

Type: **WPARAM**

The identifier of the mouse message.

### lParam [in]

Type: **LPARAM**

A pointer to a [MOUSEHOOKSTRUCT](/windows/desktop/api/winuser/ns-winuser-mousehookstruct) structure.

## Returns

Type: **LRESULT**

If *nCode* is less than zero, the hook procedure must return the value returned by [**CallNextHookEx**](/windows/win32/api/winuser/nf-winuser-callnexthookex).

If *nCode* is greater than or equal to zero, and the hook procedure did not process the message, it is highly recommended that you call **CallNextHookEx** and return the value it returns; otherwise, other applications that have installed [WH_MOUSE](about-hooks.md) hooks will not receive hook notifications and may behave incorrectly as a result.

If the hook procedure processed the message, it may return a nonzero value to prevent the system from passing the message to the target window procedure.

## Remarks

An application installs the hook procedure by specifying the [**WH_MOUSE**](/windows/win32/winmsg/about-hooks) hook type and a pointer to the hook procedure in a call to the [**SetWindowsHookExA**](/windows/win32/api/winuser/nf-winuser-setwindowshookexa)/[**SetWindowsHookExW**](/windows/win32/api/winuser/nf-winuser-setwindowshookexw) function.

The hook procedure must not install a [**WH_JOURNALPLAYBACK**](/windows/win32/winmsg/about-hooks) callback function.

This hook may be called in the context of the thread that installed it. The call is made by sending a message to the thread that installed the hook. Therefore, the thread that installed the hook must have a message loop.

## See also

[CallNextHookEx](/windows/desktop/api/winuser/nf-winuser-callnexthookex)

[GetMessage](/windows/desktop/api/winuser/nf-winuser-getmessage)

[MOUSEHOOKSTRUCT](/windows/desktop/api/winuser/ns-winuser-mousehookstruct)

[PeekMessage](/windows/desktop/api/winuser/nf-winuser-peekmessagew)

[SetWindowsHookEx](/windows/desktop/api/winuser/nf-winuser-setwindowshookexw)

[Hooks](hooks.md)

[About Hooks](about-hooks.md)
