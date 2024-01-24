---
title: TCM_DELETEITEM message (Commctrl.h)
description: Removes an item from a tab control. You can send this message explicitly or by using the TabCtrl\_DeleteItem macro.
ms.assetid: 54bfa446-580a-4ea7-b5e9-9429f4ee1c2b
keywords:
- TCM_DELETEITEM message Windows Controls
topic_type:
- apiref
api_name:
- TCM_DELETEITEM
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TCM\_DELETEITEM message

Removes an item from a tab control. You can send this message explicitly or by using the [**TabCtrl\_DeleteItem**](/windows/desktop/api/Commctrl/nf-commctrl-tabctrl_deleteitem) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Index of the item to delete.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





