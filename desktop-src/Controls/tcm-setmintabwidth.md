---
title: TCM_SETMINTABWIDTH message (Commctrl.h)
description: Sets the minimum width of items in a tab control. You can send this message explicitly or by using the TabCtrl\_SetMinTabWidth macro.
ms.assetid: c0be3d4e-774c-4233-820f-01ffbb69ecf0
keywords:
- TCM_SETMINTABWIDTH message Windows Controls
topic_type:
- apiref
api_name:
- TCM_SETMINTABWIDTH
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TCM\_SETMINTABWIDTH message

Sets the minimum width of items in a tab control. You can send this message explicitly or by using the [**TabCtrl\_SetMinTabWidth**](/windows/desktop/api/Commctrl/nf-commctrl-tabctrl_setmintabwidth) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Minimum width to be set for a tab control item. If this parameter is set to -1, the control will use the default tab width.

</dd> </dl>

## Return value

Returns an INT value that represents the previous minimum tab width.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





