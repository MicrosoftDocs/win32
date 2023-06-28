---
title: ForegroundIdleProc callback function (Windows)
description: The system calls this function whenever the foreground thread is about to become idle.
ms.date: 06/28/2023
f1_keywords:
- ForegroundIdleProc
- winuser/ForegroundIdleProc
dev_langs:
- C++
- C
api_location:
- Winuser.h
api_name:
- ForegroundIdleProc
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

# ForegroundIdleProc callback function

An application-defined or library-defined callback function used with the [**SetWindowsHookExA**](/windows/win32/api/winuser/nf-winuser-setwindowshookexa)/[**SetWindowsHookExW**](/windows/win32/api/winuser/nf-winuser-setwindowshookexw) function. The system calls this function whenever the foreground thread is about to become idle.

## Syntax

``` c++
DWORD CALLBACK ForegroundIdleProc(
  _In_ int   code,
       DWORD wParam,
       LONG  lParam
);
```

## Parameters

  - *code* \[in\]  
    Type: **int**
    
    If *code* is **HC\_ACTION**, the hook procedure must process the message. If *code* is less than zero, the hook procedure must pass the message to the [**CallNextHookEx**](/windows/win32/api/winuser/nf-winuser-callnexthookex) function without further processing and should return the value returned by **CallNextHookEx**.

  - *wParam*  
    Type: **DWORD**
    
    This parameter is not used.

  - *lParam*  
    Type: **LONG**
    
    This parameter is not used.

## Return value

Type: ****

Type: DWORD

If *code* is less than zero, the hook procedure must return the value returned by [**CallNextHookEx**](/windows/win32/api/winuser/nf-winuser-callnexthookex).

If *code* is greater than or equal to zero, it is highly recommended that you call [**CallNextHookEx**](/windows/win32/api/winuser/nf-winuser-callnexthookex) and return the value it returns; otherwise, other applications that have installed [**WH\_FOREGROUNDIDLE**](https://msdn.microsoft.com/en-us/library/ms644959\(v=vs.85\)) hooks will not receive hook notifications and may behave incorrectly as a result. If the hook procedure does not call **CallNextHookEx**, the return value should be zero.

## Remarks

The **HOOKPROC** type defines a pointer to this callback function. *ForegroundIdleProc* is a placeholder for the application-defined or library-defined function name.

An application installs this hook procedure by specifying the [**WH\_FOREGROUNDIDLE**](https://msdn.microsoft.com/en-us/library/ms644959\(v=vs.85\)) hook type and the pointer to the hook procedure in a call to the [**SetWindowsHookExA**](/windows/win32/api/winuser/nf-winuser-setwindowshookexa)/[**SetWindowsHookExW**](/windows/win32/api/winuser/nf-winuser-setwindowshookexw) function.

While processing this callback function, avoid calling any functions that retrieve window messages from the calling thread's message queue. This includes [**GetMessage**](https://msdn.microsoft.com/en-us/library/ms644936\(v=vs.85\)), [**PeekMessageA**](/windows/win32/api/winuser/nf-winuser-peekmessagea)/[**PeekMessageW**](/windows/win32/api/winuser/nf-winuser-peekmessagew), modal dialog box, and COM functions. Calling such functions may result in the thread not returning from **GetMessage** or [**WaitMessage**](https://msdn.microsoft.com/en-us/library/ms644956\(v=vs.85\)) when there are messages in the calling thread's message queue.

## Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
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

**Reference**

[**CallNextHookEx**](/windows/win32/api/winuser/nf-winuser-callnexthookex)

[**SetWindowsHookExA**](/windows/win32/api/winuser/nf-winuser-setwindowshookexa)/[**SetWindowsHookExW**](/windows/win32/api/winuser/nf-winuser-setwindowshookexw)

**Conceptual**

[Hooks](https://msdn.microsoft.com/en-us/library/ms632589\(v=vs.85\))

