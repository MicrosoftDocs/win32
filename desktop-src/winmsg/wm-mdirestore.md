---
description: An application sends the WM\_MDIRESTORE message to a multiple-document interface (MDI) client window to restore an MDI child window from maximized or minimized size.
ms.assetid: bb99fda1-9eb5-4307-9326-9a417a046c22
title: WM_MDIRESTORE message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_MDIRESTORE message

An application sends the **WM\_MDIRESTORE** message to a multiple-document interface (MDI) client window to restore an MDI child window from maximized or minimized size.


```C++
#define WM_MDIRESTORE                   0x0223
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the MDI child window to be restored.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

Type: **zero**

The return value is always zero.

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

[**WM\_MDIMAXIMIZE**](wm-mdimaximize.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Multiple Document Interface](multiple-document-interface.md)
</dt> </dl>

 

 




