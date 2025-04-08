---
UID: NS:winuser.WM_CLOAKED_STATE_CHANGED
description: Message sent to windows when their cloak state changes, if they have called RegisterCloakedNotification.
tech.root: winmsg
title: WM_CLOAKED_STATE_CHANGED message (Winuser.h)
ms.topic: reference
ms.date: 2/25/2025
f1_keywords:
 - WM_CLOAKED_STATE_CHANGED
 - winuser/WM_CLOAKED_STATE_CHANGED
dev_langs:
 - c++
helpviewer_keywords:
 - WM_CLOAKED_STATE_CHANGED
targetos: Windows
ms.localizationpriority: low
---

# WM_CLOAKED_STATE_CHANGED message

Sent when a window's cloak state has changed.

## Syntax

```C++
#define WM_CLOAKED_STATE_CHANGED 0x0347
```

## Parameters

`wParam` 

The new cloaking state of the window. If the window is cloaked, this value can
have one or more of the flags set:

**DWM_CLOAKED_APP** (value 1). The window was cloaked by its owner application.

**DWM_CLOAKED_SHELL** (value 2). The window was cloaked by the Shell.

If the window is not cloaked, the value will be:

**DWM_NOT_CLOAKED** (value 0). The window is not cloaked.

`lParam` 

This parameter is not used.

## Return value

Type: **LRESULT**

If an application processes this message, it should return zero.

## Remarks

The _wParam_ corresponds to the cloaked state the window has changed to. The
values for the cloak state have the same meaning to those returned when calling
[DwmGetWindowAttribute](/windows/win32/api/dwmapi/nf-dwmapi-dwmgetwindowattribute)
with DWMWA_CLOAKED, with the exception that the window message
WM_CLOAKED_STATE_CHANGED will never have a _wParam_ with the flag
DWM_CLOAKED_INHERITED set.

A window will not receive WM_CLOAKED_STATE_CHANGED message unless it has been
registered for cloak state notifications. See
[RegisterCloakedNotification](nf-winuser-registercloakednotification.md).

## Requirements

| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 11 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |

## See also

[RegisterCloakedNotification](nf-winuser-registercloakednotification.md)
