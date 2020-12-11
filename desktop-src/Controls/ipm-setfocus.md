---
title: IPM_SETFOCUS message (Commctrl.h)
description: Sets the keyboard focus to the specified field in the IP address control. All of the text in that field will be selected.
ms.assetid: 4b975eb2-85e1-4e33-a803-99b48d2ff5e8
keywords:
- IPM_SETFOCUS message Windows Controls
topic_type:
- apiref
api_name:
- IPM_SETFOCUS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# IPM\_SETFOCUS message

Sets the keyboard focus to the specified field in the IP address control. All of the text in that field will be selected.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A zero-based field index to which the focus should be set. If this value is greater than the number of fields, focus is set to the first blank field. If all fields are nonblank, focus is set to the first field.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

The return value is not used.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





