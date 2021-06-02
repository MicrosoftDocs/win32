---
title: WM_SETFOCUS message (Winuser.h)
description: Sent to a window after it has gained the keyboard focus.
ms.assetid: 77180e4c-95a6-41a4-93d9-033381ae7543
keywords:
- WM_SETFOCUS message Keyboard and Mouse Input
topic_type:
- apiref
api_name:
- WM_SETFOCUS
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_SETFOCUS message

Sent to a window after it has gained the keyboard focus.


```C++
#define WM_SETFOCUS                     0x0007
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the window that has lost the keyboard focus. This parameter can be **NULL**.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

An application should return zero if it processes this message.

## Remarks

To display a caret, an application should call the appropriate caret functions when it receives the **WM\_SETFOCUS** message.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**SetFocus**](/windows/win32/api/winuser/nf-winuser-setfocus)
</dt> <dt>

[**WM\_KILLFOCUS**](wm-killfocus.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Keyboard Input](keyboard-input.md)
</dt> </dl>

 

