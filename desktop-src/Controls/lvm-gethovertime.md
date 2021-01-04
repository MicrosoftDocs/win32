---
title: LVM_GETHOVERTIME message (Commctrl.h)
description: Retrieves the amount of time that the mouse cursor must hover over an item before it is selected. You can send this message explicitly or use the ListView\_GetHoverTime macro.
ms.assetid: e7646024-f868-459f-88be-b232b6b4bb2a
keywords:
- LVM_GETHOVERTIME message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETHOVERTIME
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETHOVERTIME message

Retrieves the amount of time that the mouse cursor must hover over an item before it is selected. You can send this message explicitly or use the [**ListView\_GetHoverTime**](/windows/desktop/api/Commctrl/nf-commctrl-listview_gethovertime) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the amount of time, in milliseconds, that the mouse cursor must hover over an item before it is selected. If the return value is (**DWORD**)-1, then the hover time is the default hover time.

## Remarks

The hover time only affects list-view controls that have the [**LVS\_EX\_TRACKSELECT**](extended-list-view-styles.md), [**LVS\_EX\_ONECLICKACTIVATE**](extended-list-view-styles.md), or [**LVS\_EX\_TWOCLICKACTIVATE**](extended-list-view-styles.md) extended list-view style.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





