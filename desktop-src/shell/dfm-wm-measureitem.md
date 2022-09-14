---
description: Sent to the owner window of a control or menu item when the control or menu is created.
ms.assetid: 4584a3da-6c92-4ecd-8cf2-e4afc1b8321d
title: DFM_WM_MEASUREITEM message (Shlobj.h)
ms.topic: reference
ms.date: 05/31/2018
---

# DFM\_WM\_MEASUREITEM message

Sent to the owner window of a control or menu item when the control or menu is created.


```C++
DFM_WM_MEASUREITEM 

    wParam = (WPARAM);

    lParam = (LPARAM)(LPMEASUREITEMSTRUCT) lpMeasureItem;

            
```



## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

The value of the **CtlID** member of the [**MEASUREITEMSTRUCT**](/windows/win32/api/winuser/ns-winuser-measureitemstruct) structure pointed to by the *lpMeasureItem* parameter. This value identifies the control that sent the **DFM\_WM\_MEASUREITEM** message.

</dd> <dt>

*lpMeasureItem* \[out\]
</dt> <dd>

A pointer to a [**MEASUREITEMSTRUCT**](/windows/win32/api/winuser/ns-winuser-measureitemstruct) structure that contains the dimensions of the owner-drawn control or menu item.

</dd> </dl>

## Remarks

When the owner window receives the **DFM\_WM\_MEASUREITEM** message, the owner fills in the [**MEASUREITEMSTRUCT**](/windows/win32/api/winuser/ns-winuser-measureitemstruct) structure pointed to by the *lpMeasureItem* parameter of the message and returns; this informs the system of the dimensions of the control.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 
