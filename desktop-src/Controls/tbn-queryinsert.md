---
title: TBN_QUERYINSERT notification code (Commctrl.h)
description: Notifies the toolbar's parent window whether a button may be inserted to the left of the specified button while the user is customizing a toolbar. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: d389fabb-16f6-43aa-a4b6-abb80723345b
keywords:
- TBN_QUERYINSERT notification code Windows Controls
topic_type:
- apiref
api_name:
- TBN_QUERYINSERT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBN\_QUERYINSERT notification code

Notifies the toolbar's parent window whether a button may be inserted to the left of the specified button while the user is customizing a toolbar. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TBN_QUERYINSERT 

    lpnmtb = (LPNMTOOLBAR) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTOOLBAR**](/windows/win32/api/commctrl/ns-commctrl-nmtoolbara) structure. The **iItem** member contains the zero-based index of the button to be inserted.

</dd> </dl>

## Return value

Return **TRUE** to allow a button to be inserted in front of the given button, or **FALSE** to prevent the button from being inserted.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





