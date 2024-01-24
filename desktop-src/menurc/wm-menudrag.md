---
title: WM_MENUDRAG message (Winuser.h)
description: Sent to the owner of a drag-and-drop menu when the user drags a menu item.
ms.assetid: 99e8f490-ef1e-4964-a3a1-47030a88f10c
keywords:
- WM_MENUDRAG message Menus and Other Resources
topic_type:
- apiref
api_name:
- WM_MENUDRAG
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_MENUDRAG message

Sent to the owner of a drag-and-drop menu when the user drags a menu item.


```C++
#define WM_MENUDRAG                     0x0123
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The position of the item where the drag operation began.

</dd> <dt>

*lParam* 
</dt> <dd>

A handle to the menu containing the item.

</dd> </dl>

## Return value

The application should return one of the following values.



| Return code/value                                                                                                                                   | Description                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| <dl> <dt>**MND\_CONTINUE**</dt> <dt>0</dt> </dl> | Menu should remain active. If the mouse is released, it should be ignored.<br/> |
| <dl> <dt>**MND\_ENDMENU**</dt> <dt>1</dt> </dl>  | Menu should be ended.<br/>                                                      |



 

## Remarks

The application can call the [**DoDragDrop**](/windows/win32/api/ole2/nf-ole2-dodragdrop) function in response to this message.

To create a drag-and-drop menu, call [**SetMenuInfo**](/windows/desktop/api/Winuser/nf-winuser-setmenuinfo) with **MNS\_DRAGDROP**.

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

[**SetMenuInfo**](/windows/desktop/api/Winuser/nf-winuser-setmenuinfo)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Menus](menus.md)
</dt> </dl>

 

