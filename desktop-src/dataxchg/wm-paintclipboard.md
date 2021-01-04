---
title: WM_PAINTCLIPBOARD message (Winuser.h)
description: Sent to the clipboard owner by a clipboard viewer window when the clipboard contains data in the CF\_OWNERDISPLAY format and the clipboard viewer's client area needs repainting.
ms.assetid: 85aeefa5-e3d9-4689-a068-47b59ec7b571
keywords:
- WM_PAINTCLIPBOARD message Data Exchange
topic_type:
- apiref
api_name:
- WM_PAINTCLIPBOARD
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_PAINTCLIPBOARD message

Sent to the clipboard owner by a clipboard viewer window when the clipboard contains data in the [**CF\_OWNERDISPLAY**](standard-clipboard-formats.md) format and the clipboard viewer's client area needs repainting.


```C++
#define WM_PAINTCLIPBOARD               0x0309
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the clipboard viewer window.

</dd> <dt>

*lParam* 
</dt> <dd>

A handle to a global memory object that contains a [**PAINTSTRUCT**](/windows/win32/api/winuser/ns-winuser-paintstruct) structure. The structure defines the part of the client area to paint.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Remarks

To determine whether the entire client area or just a portion of it needs repainting, the clipboard owner must compare the dimensions of the drawing area given in the **rcPaint** member of [**PAINTSTRUCT**](/windows/win32/api/winuser/ns-winuser-paintstruct) to the dimensions given in the most recent [**WM\_SIZECLIPBOARD**](wm-sizeclipboard.md) message.

The clipboard owner must use the [**GlobalLock**](/windows/desktop/api/winbase/nf-winbase-globallock) function to lock the memory that contains the [**PAINTSTRUCT**](/windows/win32/api/winuser/ns-winuser-paintstruct) structure. Before returning, the clipboard owner must unlock that memory by using the [**GlobalUnlock**](/windows/desktop/api/winbase/nf-winbase-globalunlock) function.

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

[**WM\_SIZECLIPBOARD**](wm-sizeclipboard.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Clipboard](clipboard.md)
</dt> </dl>

 

