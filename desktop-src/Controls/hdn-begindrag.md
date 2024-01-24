---
title: HDN_BEGINDRAG notification code (Commctrl.h)
description: Sent by a header control when a drag operation has begun on one of its items. This notification code is sent only by header controls that are set to the HDS\_DRAGDROP style. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 3dfb7a7c-d783-48e0-ba92-8144104f163a
keywords:
- HDN_BEGINDRAG notification code Windows Controls
topic_type:
- apiref
api_name:
- HDN_BEGINDRAG
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# HDN\_BEGINDRAG notification code

Sent by a header control when a drag operation has begun on one of its items. This notification code is sent only by header controls that are set to the [**HDS\_DRAGDROP**](header-control-styles.md) style. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
HDN_BEGINDRAG

   pNMHeader = (LPNMHEADER) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMHEADER**](/windows/win32/api/commctrl/ns-commctrl-nmheadera) structure containing information about the header item that is being dragged.

</dd> </dl>

## Return value

To allow the header control to automatically manage drag-and-drop operations, return **FALSE**. If the owner of the control is manually performing drag-and-drop reordering, return **TRUE**.

## Remarks

A header control defaults to automatically managing drag-and-drop reordering. Returning **TRUE** to indicate external (manual) drag-and-drop management allows the owner of the control to provide custom services as part of the drag-and-drop process.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





