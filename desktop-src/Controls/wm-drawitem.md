---
title: WM\_DRAWITEM message
description: Sent to the parent window of an owner-drawn button, combo box, list box, or menu when a visual aspect of the button, combo box, list box, or menu has changed.
ms.assetid: e54bae5e-10d6-43b0-a766-1b270c8873a9
keywords:
- WM_DRAWITEM message Windows Controls
topic_type:
- apiref
api_name:
- WM_DRAWITEM
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_DRAWITEM message

Sent to the parent window of an owner-drawn button, combo box, list box, or menu when a visual aspect of the button, combo box, list box, or menu has changed.

A window receives this message through its [*WindowProc*](https://msdn.microsoft.com/library/windows/desktop/ms633573) function.


```C++
WM_DRAWITEM

    WPARAM wParam;
    LPARAM lParam; 
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the identifier of the control that sent the **WM\_DRAWITEM** message. If the message was sent by a menu, this parameter is zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**DRAWITEMSTRUCT**](/windows/desktop/api/Winuser/ns-winuser-tagdrawitemstruct) structure containing information about the item to be drawn and the type of drawing required.

</dd> </dl>

## Return value

If an application processes this message, it should return **TRUE**.

## Remarks

By default, the [**DefWindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633572) function draws the focus rectangle for an owner-drawn list box item.

The *itemAction* member of the [**DRAWITEMSTRUCT**](/windows/desktop/api/Winuser/ns-winuser-tagdrawitemstruct) structure specifies the drawing operation that an application should perform.

Before returning from processing this message, an application should ensure that the device context identified by the *hDC* member of the [**DRAWITEMSTRUCT**](/windows/desktop/api/Winuser/ns-winuser-tagdrawitemstruct) structure is in the default state.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**DRAWITEMSTRUCT**](/windows/desktop/api/Winuser/ns-winuser-tagdrawitemstruct)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**DefWindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633572)
</dt> </dl>

 

 





