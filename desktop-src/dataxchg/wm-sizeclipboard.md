---
title: WM_SIZECLIPBOARD message (Winuser.h)
description: Sent to the clipboard owner by a clipboard viewer window when the clipboard contains data in the CF\_OWNERDISPLAY format and the clipboard viewer's client area has changed size.
ms.assetid: 95991d03-8677-4dde-b72a-082dec4834b3
keywords:
- WM_SIZECLIPBOARD message Data Exchange
topic_type:
- apiref
api_name:
- WM_SIZECLIPBOARD
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_SIZECLIPBOARD message

Sent to the clipboard owner by a clipboard viewer window when the clipboard contains data in the [**CF\_OWNERDISPLAY**](standard-clipboard-formats.md) format and the clipboard viewer's client area has changed size.


```C++
#define WM_SIZECLIPBOARD                0x030B
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the clipboard viewer window.

</dd> <dt>

*lParam* 
</dt> <dd>

A handle to a global memory object that contains a [**RECT**](/previous-versions//dd162897(v=vs.85)) structure. The structure specifies the new dimensions of the clipboard viewer's client area.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Remarks

When the clipboard viewer window is about to be destroyed or resized, a **WM\_SIZECLIPBOARD** message is sent with a null rectangle (0, 0, 0, 0) as the new size. This permits the clipboard owner to free its display resources.

The clipboard owner must use the [**GlobalLock**](/windows/desktop/api/winbase/nf-winbase-globallock) function to lock the memory object that contains [**RECT**](/previous-versions//dd162897(v=vs.85)). Before returning, the clipboard owner must unlock the object by using the [**GlobalUnlock**](/windows/desktop/api/winbase/nf-winbase-globalunlock) function.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Conceptual**
</dt> <dt>

[Clipboard](clipboard.md)
</dt> </dl>

 

