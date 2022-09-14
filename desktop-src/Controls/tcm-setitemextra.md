---
title: TCM_SETITEMEXTRA message (Commctrl.h)
description: Sets the number of bytes per tab reserved for application-defined data in a tab control. You can send this message explicitly or by using the TabCtrl\_SetItemExtra macro.
ms.assetid: 8315f1fd-8eca-48bd-bb4a-71b09e8aa2c4
keywords:
- TCM_SETITEMEXTRA message Windows Controls
topic_type:
- apiref
api_name:
- TCM_SETITEMEXTRA
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TCM\_SETITEMEXTRA message

Sets the number of bytes per tab reserved for application-defined data in a tab control. You can send this message explicitly or by using the [**TabCtrl\_SetItemExtra**](/windows/desktop/api/Commctrl/nf-commctrl-tabctrl_setitemextra) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Number of extra bytes.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

By default, the number of extra bytes is four. An application that changes the number of extra bytes cannot use the [**TCITEM**](/windows/win32/api/commctrl/ns-commctrl-tcitema) structure to retrieve and set the application-defined data for a tab. Instead, you must define a new structure that consists of the [**TCITEMHEADER**](/windows/win32/api/commctrl/ns-commctrl-tcitemheadera) structure followed by application-defined members.

An application should only change the number of extra bytes when a tab control does not contain any tabs.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





