---
title: TCM_GETITEMCOUNT message (Commctrl.h)
description: Retrieves the number of tabs in the tab control. You can send this message explicitly or by using the TabCtrl\_GetItemCount macro.
ms.assetid: a8ec7d66-fe44-45ca-8f6c-4e75752ebe95
keywords:
- TCM_GETITEMCOUNT message Windows Controls
topic_type:
- apiref
api_name:
- TCM_GETITEMCOUNT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TCM\_GETITEMCOUNT message

Retrieves the number of tabs in the tab control. You can send this message explicitly or by using the [**TabCtrl\_GetItemCount**](/windows/desktop/api/Commctrl/nf-commctrl-tabctrl_getitemcount) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the number of items if successful, or zero otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





