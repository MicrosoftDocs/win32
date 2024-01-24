---
description: Sent to the parent window of an owner-drawn control or menu when a visual aspect of the control or menu has changed.
ms.assetid: 2515bbab-025f-4f00-8564-a732d68edea3
title: DFM_WM_DRAWITEM message (Shlobj.h)
ms.topic: reference
ms.date: 05/31/2018
---

# DFM\_WM\_DRAWITEM message

Sent to the parent window of an owner-drawn control or menu when a visual aspect of the control or menu has changed.


```C++
DFM_WM_DRAWITEM 

    wParam = (WPARAM);

    lParam = (LPARAM)(LPDRAWITEMSTRUCT) lpDrawItem;

            
```



## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

The identifier of the control that sent the **DFM\_WM\_DRAWITEM** message. If the message was sent by a menu, this parameter is zero.

</dd> <dt>

*lpDrawItem* \[out\]
</dt> <dd>

A pointer to a [**DRAWITEMSTRUCT**](/windows/win32/api/winuser/ns-winuser-drawitemstruct) structure containing information about the item to be drawn and the type of drawing required.

</dd> </dl>

## Return value

If an application processes this message, it should return **TRUE**.

## Remarks

The **itemAction** member of the [**DRAWITEMSTRUCT**](/windows/win32/api/winuser/ns-winuser-drawitemstruct) structure specifies the drawing operation that an application should perform.

Before returning from processing this message, an application should ensure that the device context identified by the **hDC** member of the [**DRAWITEMSTRUCT**](/windows/win32/api/winuser/ns-winuser-drawitemstruct) structure is in the default state.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 
