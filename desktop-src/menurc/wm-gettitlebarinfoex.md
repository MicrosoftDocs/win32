---
title: WM_GETTITLEBARINFOEX message (Winuser.h)
description: Sent to request extended title bar information. A window receives this message through its WindowProc function.
ms.assetid: 0760dbf1-5b20-471c-bfd9-b8d28b52074b
keywords:
- WM_GETTITLEBARINFOEX message Menus and Other Resources
topic_type:
- apiref
api_name:
- WM_GETTITLEBARINFOEX
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_GETTITLEBARINFOEX message

Sent to request extended title bar information. A window receives this message through its [**WindowProc**](/windows/win32/api/winuser/nc-winuser-wndproc) function.


```C++
#define WM_GETTITLEBARINFOEX            0x033F
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used and must be 0.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**TITLEBARINFOEX**](/windows/win32/api/winuser/ns-winuser-titlebarinfoex) structure. The message sender is responsible for allocating memory for this structure. Set the **cbSize** member of this structure to `sizeof(TITLEBARINFOEX)` before passing this structure with the message.

</dd> </dl>

## Remarks

The following example shows how the message receiver casts an **LPARAM** value to retrieve the [**TITLEBARINFOEX**](/windows/win32/api/winuser/ns-winuser-titlebarinfoex) structure.

`TITLEBARINFOEX *ptinfo = (TITLEBARINFOEX *)lParam;`

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Menus Overview](menus.md)
</dt> </dl>

 

