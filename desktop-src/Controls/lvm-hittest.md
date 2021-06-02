---
title: LVM_HITTEST message (Commctrl.h)
description: Determines which list-view item, if any, is at a specified position. You can send this message explicitly or by using the ListView\_HitTest macro.
ms.assetid: 81df4ed1-30bd-4b63-9cb9-5163cb7cf52c
keywords:
- LVM_HITTEST message Windows Controls
topic_type:
- apiref
api_name:
- LVM_HITTEST
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_HITTEST message

Determines which list-view item, if any, is at a specified position. You can send this message explicitly or by using the [**ListView\_HitTest**](/windows/desktop/api/Commctrl/nf-commctrl-listview_hittest) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be 0. **Windows Vista.** Should be -1 if the **iGroup** and **iSubItem** members of the *lParam* structure are to be retrieved.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**LVHITTESTINFO**](/windows/win32/api/commctrl/ns-commctrl-lvhittestinfo) structure that contains the position to hit test and receives information about the results of the hit test.

</dd> </dl>

## Return value

Returns the index of the item at the specified position, if any, or -1 otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





