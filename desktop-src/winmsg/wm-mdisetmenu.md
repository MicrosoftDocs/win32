---
description: An application sends the WM\_MDISETMENU message to a multiple-document interface (MDI) client window to replace the entire menu of an MDI frame window, to replace the window menu of the frame window, or both.
ms.assetid: 5cc85032-5378-44a0-abd4-d583deaa3294
title: WM_MDISETMENU message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_MDISETMENU message

An application sends the **WM\_MDISETMENU** message to a multiple-document interface (MDI) client window to replace the entire menu of an MDI frame window, to replace the window menu of the frame window, or both.


```C++
#define WM_MDISETMENU                   0x0230
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the new frame window menu. If this parameter is **NULL**, the frame window menu is not changed.

</dd> <dt>

*lParam* 
</dt> <dd>

A handle to the new window menu. If this parameter is **NULL**, the window menu is not changed.

</dd> </dl>

## Return value

Type: **HMENU**

If the message succeeds, the return value is the handle to the old frame window menu.

If the message fails, the return value is zero.

## Remarks

After sending this message, an application must call the [**DrawMenuBar**](/windows/win32/api/winuser/nf-winuser-drawmenubar) function to update the menu bar.

If this message replaces the window menu, the MDI child window menu items are removed from the previous window menu and added to the new window menu.

If an MDI child window is maximized and this message replaces the MDI frame window menu, the window menu icon and restore icon are removed from the previous frame window menu and added to the new frame window menu.

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

[**DrawMenuBar**](/windows/win32/api/winuser/nf-winuser-drawmenubar)
</dt> <dt>

[**WM\_MDIREFRESHMENU**](wm-mdirefreshmenu.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Multiple Document Interface](multiple-document-interface.md)
</dt> </dl>

 

 
