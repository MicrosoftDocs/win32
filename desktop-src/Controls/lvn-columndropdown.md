---
title: LVN_COLUMNDROPDOWN notification code (Commctrl.h)
description: Sent by a list-view control when the list-view's drop-down button is pressed. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 752d745e-4482-425c-af3c-f9707cbb03d7
keywords:
- LVN_COLUMNDROPDOWN notification code Windows Controls
topic_type:
- apiref
api_name:
- LVN_COLUMNDROPDOWN
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVN\_COLUMNDROPDOWN notification code

Sent by a list-view control when the list-view's drop-down button is pressed. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
LVN_COLUMNDROPDOWN
        
    pnmv = (LPNMLISTVIEW) lParam;
```



## Parameters

<dl> <dt>

*lParam* \[in\]
</dt> <dd>

Pointer to a [**NMLISTVIEW**](/windows/win32/api/commctrl/ns-commctrl-nmlistview) structure that describes the notification code. The caller is responsible for allocating this structure, including the contained [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-nmhdr) structure. Set the members of the **NMHDR** structure. The **code** member must be set to LVN\_COLUMNDROPDOWN.

Set the **iItem** member of the [**NMLISTVIEW**](/windows/win32/api/commctrl/ns-commctrl-nmlistview) structure to -1. Set the **iSubItem** member to the index of the subitem. Set the **uNewState**, **uOldState**, and **lParam** members to zero. The remaining members of the **NMLISTVIEW** structure are not used.

</dd> </dl>

## Return value

No return value.

## Remarks

The notification receiver casts *lParam* to retrieve the [**NMLISTVIEW**](/windows/win32/api/commctrl/ns-commctrl-nmlistview) structure. The *wParam* parameter contains the ID of the control that sends the notification code.

If a header control is a child of the list-view, the header control should send this notidication code to the list-view control when the header control receives the [HDN\_DROPDOWN](hdn-dropdown.md) notification code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





