---
title: LVN_INCREMENTALSEARCH notification code (Commctrl.h)
description: Notifies a list-view control's parent window that an incremental search has started. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 34517250-a6ba-490b-b87e-b09048543339
keywords:
- LVN_INCREMENTALSEARCH notification code Windows Controls
topic_type:
- apiref
api_name:
- LVN_INCREMENTALSEARCH
- LVN_INCREMENTALSEARCHA
- LVN_INCREMENTALSEARCHW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVN\_INCREMENTALSEARCH notification code

Notifies a list-view control's parent window that an incremental search has started. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
LVN_INCREMENTALSEARCH
          
    pnmv = (LPNMLVFINDITEM) lParam;
```



## Parameters

<dl> <dt>

*lParam* \[in\]
</dt> <dd>

Pointer to a [**NMLVFINDITEM**](/windows/win32/api/commctrl/ns-commctrl-nmlvfinditema) structure that describes the notification code. The caller is responsible for allocating this structure, including the contained [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-nmhdr) and [**LVFINDINFO**](/windows/win32/api/commctrl/ns-commctrl-lvfindinfoa) structures. Set the members of the **NMHDR** structure. The **code** member must be set to LVN\_INCREMENTALSEARCH.

</dd> </dl>

## Return value

No return value.

## Remarks

The notification receiver casts *lParam* to retrieve the [**NMLVFINDITEM**](/windows/win32/api/commctrl/ns-commctrl-nmlvfinditema) structure. The *wParam* parameter contains the ID of the control that sends this notification code.

This notification code gives an application (or the notification receiver) the opportunity to customize an incremental search. For example, if the search items are numeric, the application can perform a numerical search instead of a string search.

The application sets the **lParam** member of the [**LVFINDINFO**](/windows/win32/api/commctrl/ns-commctrl-lvfindinfoa) structure contained in [**NMLVFINDITEM**](/windows/win32/api/commctrl/ns-commctrl-nmlvfinditema) structure  to the result of the search, or to another application defined value to fail the search and indicate to the control how to proceed.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl>   |
| Unicode and ANSI names<br/>   | **LVN\_INCREMENTALSEARCHW** (Unicode) and **LVN\_INCREMENTALSEARCHA** (ANSI)<br/> |



 

 





