---
title: CallWndProc callback function (Windows)
description: The system calls this function before calling the window procedure to process a message sent to the thread.
ms.date: 06/30/2023
ms.topic: reference
f1_keywords:
- CallWndProc
- winuser/CallWndProc
dev_langs:
- C++
- C
api_location:
- Winuser.h
api_name:
- CallWndProc
api_type:
- UserDefined
product:
- Windows
topic_type:
- apiref
- kbSyntax
product_family_name: VS
ROBOTS: INDEX,FOLLOW
---

# CallWndProc callback function

An application-defined or library-defined callback function used with the [**SetWindowsHookExA**](/windows/win32/api/winuser/nf-winuser-setwindowshookexa)/[**SetWindowsHookExW**](/windows/win32/api/winuser/nf-winuser-setwindowshookexw) function. The system calls this function before calling the window procedure to process a message sent to the thread.

The **HOOKPROC** type defines a pointer to this callback function. *CallWndProc* is a placeholder for the application-defined or library-defined function name.

## Syntax

``` c++
LRESULT CALLBACK CallWndProc(
  _In_ int    nCode,
  _In_ WPARAM wParam,
  _In_ LPARAM lParam
);
```

## Parameters

  - *nCode* \[in\]  
    Type: **int**
    
    Specifies whether the hook procedure must process the message. If *nCode* is **HC_ACTION**, the hook procedure must process the message. If *nCode* is less than zero, the hook procedure must pass the message to the [**CallNextHookEx**](/windows/win32/api/winuser/nf-winuser-callnexthookex) function without further processing and must return the value returned by **CallNextHookEx**.

  - *wParam* \[in\]  
    Type: **WPARAM**
    
    Specifies whether the message was sent by the current thread. If the message was sent by the current thread, it is nonzero; otherwise, it is zero.

  - *lParam* \[in\]  
    Type: **LPARAM**
    
    A pointer to a [**CWPSTRUCT**](/windows/win32/api/winuser/ns-winuser-cwpstruct) structure that contains details about the message.

## Return value

Type: ****

Type: LRESULT

If *nCode* is less than zero, the hook procedure must return the value returned by [**CallNextHookEx**](/windows/win32/api/winuser/nf-winuser-callnexthookex).

If *nCode* is greater than or equal to zero, it is highly recommended that you call [**CallNextHookEx**](/windows/win32/api/winuser/nf-winuser-callnexthookex) and return the value it returns; otherwise, other applications that have installed [**WH_CALLWNDPROC**](/windows/win32/winmsg/about-hooks) hooks will not receive hook notifications and may behave incorrectly as a result. If the hook procedure does not call **CallNextHookEx**, the return value should be zero.

## Remarks

The *CallWndProc* hook procedure can examine the message, but it cannot modify it. After the hook procedure returns control to the system, the message is passed to the window procedure.

An application installs the hook procedure by specifying the [**WH_CALLWNDPROC**](/windows/win32/winmsg/about-hooks) hook type and a pointer to the hook procedure in a call to the [**SetWindowsHookExA**](/windows/win32/api/winuser/nf-winuser-setwindowshookexa)/[**SetWindowsHookExW**](/windows/win32/api/winuser/nf-winuser-setwindowshookexw) function.

## Requirements

<table>
<colgroup>
<col />
<col />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 2000 Professional [desktop apps only]</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows 2000 Server [desktop apps only]</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Winuser.h (include Windows.h)</td>
</tr>
</tbody>
</table>

## See also

[**CallNextHookEx**](/windows/win32/api/winuser/nf-winuser-callnexthookex)

[**CWPSTRUCT**](/windows/win32/api/winuser/ns-winuser-cwpstruct)

[**SendMessage**](/windows/win32/api/winuser/nf-winuser-sendmessage)

[**SetWindowsHookExA**](/windows/win32/api/winuser/nf-winuser-setwindowshookexa)/[**SetWindowsHookExW**](/windows/win32/api/winuser/nf-winuser-setwindowshookexw)

[Hooks](hooks.md)
