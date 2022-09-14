---
title: RBN_CHEVRONPUSHED notification code (Commctrl.h)
description: Sent by a rebar control when a chevron is pushed. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 58aa2c9d-8ab6-46ee-b32f-5c04fb7afa84
keywords:
- RBN_CHEVRONPUSHED notification code Windows Controls
topic_type:
- apiref
api_name:
- RBN_CHEVRONPUSHED
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RBN\_CHEVRONPUSHED notification code

Sent by a rebar control when a chevron is pushed. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
RBN_CHEVRONPUSHED

    lpnm = (NMREBARCHEVRON) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to the band's [**NMREBARCHEVRON**](/windows/win32/api/commctrl/ns-commctrl-nmrebarchevron) structure.

</dd> </dl>

## Return value

The return value for this notification is not used.

## Remarks

When an application receives this notification code, it is responsible for displaying a popup menu with items for each hidden tool. Use the **rc** member of the [**NMREBARCHEVRON**](/windows/win32/api/commctrl/ns-commctrl-nmrebarchevron) structure to find the correct position for the popup menu.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





