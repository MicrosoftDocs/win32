---
description: Translates virtual-key messages into character messages.
title: TranslateMessageEx
ms.topic: reference
ms.date: 03/23/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TranslateMessageEx
api_type: 
- DllExport
api_location: 
- user32.dll
---

# TranslateMessageEx function

Translates virtual-key messages into character messages. The character messages are posted to the calling thread's message queue, to be read the next time the thread calls the <a href="/windows/desktop/api/winuser/nf-winuser-getmessage">GetMessage</a> or <a href="/windows/desktop/api/winuser/nf-winuser-peekmessagea">PeekMessage</a> function.

## Syntax

```C++
WINUSERAPI
BOOL
WINAPI
TranslateMessageEx(
    _In_ CONST MSG *lpMsg,
    _In_ UINT flags);
```

## Parameters

### lpMsg [in]

A pointer to a [MSG](/windows/desktop/api/winuser/ns-winuser-msg) structure that contains message information retrieved from the calling thread's message queue by using the [GetMessage](/windows/desktop/api/winuser/nf-winuser-getmessage) or [PeekMessage](/windows/desktop/api/winuser/nf-winuser-peekmessagea) function.


### flags [in]

The behavior of the function.

If bit 0 is set, a menu is active. In this mode Alt+Numeric keypad key combinations are not handled.

If bit 1 is set, **TranslateMessageEx** will return FALSE when it does not post WM_CHAR or WM_SYSCHAR to the message loop.

If bit 2 is set, keyboard state is not changed (Windows 10, version 1607 and newer)

All other bits (through 31) are reserved.


## Return value

Returns a boolean value. If the message is translated (that is, a character message is posted to the thread's message queue), the return value is nonzero.

Unlike [TranslateMessage](/windows/win32/api/winuser/nf-winuser-translatemessage), **TranslateMessageEx** will return FALSE for the case where it doesn't post a WM_CHAR.


If the message is not translated (that is, a character message is not posted to the thread's message queue), the return value is zero.

## -remarks

The **TranslateMessage** function does not modify the message pointed to by the *lpMsg* parameter. 


[WM_KEYDOWN](/windows/desktop/inputdev/wm-keydown) and [WM_KEYUP](/windows/desktop/inputdev/wm-keyup) combinations produce a [WM_CHAR](/windows/desktop/inputdev/wm-char) or [WM_DEADCHAR](/windows/desktop/inputdev/wm-deadchar) message. [WM_SYSKEYDOWN](/windows/desktop/inputdev/wm-syskeydown) and [WM_SYSKEYUP](/windows/desktop/inputdev/wm-syskeyup) combinations produce a [WM_SYSCHAR](/windows/desktop/menurc/wm-syschar) or [WM_SYSDEADCHAR](/windows/desktop/inputdev/wm-sysdeadchar) message. 

**TranslateMessage** produces [WM_CHAR](/windows/desktop/inputdev/wm-char) messages only for keys that are mapped to ASCII characters by the keyboard driver. 

If applications process virtual-key messages for some other purpose, they should not call **TranslateMessage**. For instance, an application should not call **TranslateMessage** if the [TranslateAccelerator](/windows/desktop/api/winuser/nf-winuser-translateacceleratora) function returns a nonzero value. Note that the application is responsible for retrieving and dispatching input messages to the dialog box. Most applications use the main message loop for this. However, to permit the user to move to and to select controls by using the keyboard, the application must call [IsDialogMessage](/windows/desktop/api/winuser/nf-winuser-isdialogmessagea). For more information, see [Dialog Box Keyboard Interface](/windows/desktop/dlgbox/dlgbox-programming-considerations).

This function is not defined in an SDK header and must be declared by the caller. This function is exported from user32.dll.