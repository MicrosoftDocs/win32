---
UID: 
title: GetMsgProc callback function
description: The system calls this function when a message function gets a message from an application message queue.
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

# GetMsgProc function

## -description

An application-defined or library-defined callback function used with the [SetWindowsHookEx](/windows/desktop/api/winuser/nf-winuser-setwindowshookexw) function. The system calls this function whenever the [GetMessage](/windows/desktop/api/winuser/nf-winuser-getmessage) or [PeekMessage](/windows/desktop/api/winuser/nf-winuser-peekmessagew) function has retrieved a message from an application message queue.
Before returning the retrieved message to the caller, the system passes the message to the hook procedure.

The **HOOKPROC** type defines a pointer to this callback function.
**GetMsgProc** is a placeholder for the application-defined or library-defined function name.

```cpp
LRESULT CALLBACK GetMsgProc(
  _In_ int    code,
  _In_ WPARAM wParam,
  _In_ LPARAM lParam
);
```

## -parameters

### code [in]

Type: **int**

Specifies whether the hook procedure must process the message.
If *code* is **HC_ACTION**, the hook procedure must process the message.
If *code* is less than zero, the hook procedure must pass the message to the [CallNextHookEx](/windows/desktop/api/winuser/nf-winuser-callnexthookex) function without further processing and should return the value returned by **CallNextHookEx**.

### wParam [in]

Type: **WPARAM**

Specifies whether the message has been removed from the queue.
This parameter can be one of the following values.

| Value | Meaning |
|-------|---------|
| **PM_NOREMOVE** 0x0000 | The message has not been removed from the queue. (An application called the **PeekMessage** function, specifying the **PM_NOREMOVE** flag.) |
| **PM_REMOVE** 0x0001 | The message has been removed from the queue. (An application called **GetMessage**, or it called the  **PeekMessage** function, specifying the **PM_REMOVE** flag.)|

### lParam [in]

Type: **LPARAM**

A pointer to an [MSG](/windows/desktop/api/winuser/ns-winuser-msg) structure that contains details about the message.

## -returns

If *code* is less than zero, the hook procedure must return the value returned by [CallNextHookEx](/windows/desktop/api/winuser/nf-winuser-callnexthookex).

If *code* is greater than or equal to zero, it is highly recommended that you call **CallNextHookEx** and return the value it returns; otherwise, other applications that have installed [WH_GETMESSAGE](about-hooks.md) hooks will not receive hook notifications and may behave incorrectly as a result.
If the hook procedure does not call **CallNextHookEx**, the return value should be zero.

## -remarks

The **GetMsgProc** hook procedure can examine or modify the message.
After the hook procedure returns control to the system, the **GetMessage** or **PeekMessage** function returns the message, along with any modifications, to the application that originally called it.

An application installs this hook procedure by specifying the **WH_GETMESSAGE** hook type and a pointer to the hook procedure in a call to the **SetWindowsHookEx** function.

## See also

[CallNextHookEx](/windows/desktop/api/winuser/nf-winuser-callnexthookex)

[GetMessage](/windows/desktop/api/winuser/nf-winuser-getmessage)

[MSG](/windows/desktop/api/winuser/ns-winuser-msg)

[PeekMessage](/windows/desktop/api/winuser/nf-winuser-peekmessagew)

[SetWindowsHookEx](/windows/desktop/api/winuser/nf-winuser-setwindowshookexw)

[Hooks](hooks.md)
