---
title: HDN_ENDDRAG notification code (Commctrl.h)
description: Sent by a header control when a drag operation has ended on one of its items. This notification code is sent as a WM\_NOTIFY message. Only header controls that are set to the HDS\_DRAGDROP style send this notification code.
ms.assetid: a28df985-73f1-4fc7-a1db-81a86a131c06
keywords:
- HDN_ENDDRAG notification code Windows Controls
topic_type:
- apiref
api_name:
- HDN_ENDDRAG
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# HDN\_ENDDRAG notification code

Sent by a header control when a drag operation has ended on one of its items. This notification code is sent as a [**WM\_NOTIFY**](wm-notify.md) message. Only header controls that are set to the [**HDS\_DRAGDROP**](header-control-styles.md) style send this notification code.


```C++
HDN_ENDDRAG

   pNMHeader = (LPNMHEADER) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMHEADER**](/windows/win32/api/commctrl/ns-commctrl-nmheadera) structure containing information about the header item that was being dragged.

</dd> </dl>

## Return value

To allow the control to automatically place and reorder the item, return **FALSE**. To prevent the item from being placed, return **TRUE**.

## Remarks

If the owner is performing external (manual) drag-and-drop management, it must return **FALSE**. The owner then must reorder header items manually by sending [**HDM\_SETITEM**](hdm-setitem.md) or [**HDM\_SETORDERARRAY**](hdm-setorderarray.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





