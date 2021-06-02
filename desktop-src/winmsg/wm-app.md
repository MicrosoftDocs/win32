---
description: Used to define private messages, usually of the form WM\_APP+x, where x is an integer value.
ms.assetid: fdb549df-426f-4af5-9c17-6e8730e4abc0
title: WM_APP (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_APP

Used to define private messages, usually of the form **WM\_APP**+*x*, where *x* is an integer value.

``` syntax
#define WM_APP                          0x8000
```

## Remarks

The **WM\_APP** constant is used to distinguish between message values that are reserved for use by the system and values that can be used by an application to send messages within a private window class. The following are the ranges of message numbers available.



| Range                                                 | Meaning                                                        |
|-------------------------------------------------------|----------------------------------------------------------------|
| 0 through [**WM\_USER**](wm-user.md) –1<br/>   | Messages reserved for use by the system.<br/>            |
| [**WM\_USER**](wm-user.md) through 0x7FFF<br/> | Integer messages for use by private window classes.<br/> |
| **WM\_APP** through 0xBFFF<br/>                 | Messages available for use by applications.<br/>         |
| 0xC000 through 0xFFFF<br/>                      | String messages for use by applications.<br/>            |
| Greater than 0xFFFF<br/>                        | Reserved by the system.<br/>                             |



 

Message numbers in the first range (0 through [**WM\_USER**](wm-user.md) –1) are defined by the system. Values in this range that are not explicitly defined are reserved by the system.

Message numbers in the second range ([**WM\_USER**](wm-user.md) through 0x7FFF) can be defined and used by an application to send messages within a private window class. These values cannot be used to define messages that are meaningful throughout an application because some predefined window classes already define values in this range. For example, predefined control classes such as **BUTTON**, **EDIT**, **LISTBOX**, and **COMBOBOX** may use these values. Messages in this range should not be sent to other applications unless the applications have been designed to exchange messages and to attach the same meaning to the message numbers.

Message numbers in the third range (0x8000 through 0xBFFF) are available for applications to use as private messages. Messages in this range do not conflict with system messages.

Message numbers in the fourth range (0xC000 through 0xFFFF) are defined at run time when an application calls the [**RegisterWindowMessage**](/windows/win32/api/winuser/nf-winuser-registerwindowmessagea) function to retrieve a message number for a string. All applications that register the same string can use the associated message number for exchanging messages. The actual message number, however, is not a constant and cannot be assumed to be the same between different sessions.

Message numbers in the fifth range (greater than 0xFFFF) are reserved by the system.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**RegisterWindowMessage**](/windows/win32/api/winuser/nf-winuser-registerwindowmessagea)
</dt> <dt>

[**WM\_USER**](wm-user.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Messages and Message Queues](messages-and-message-queues.md)
</dt> </dl>

 

 
