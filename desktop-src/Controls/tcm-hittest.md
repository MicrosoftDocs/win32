---
title: TCM_HITTEST message (Commctrl.h)
description: Determines which tab, if any, is at a specified screen position. You can send this message explicitly or by using the TabCtrl\_HitTest macro.
ms.assetid: 0334f616-8d39-4460-a7f8-692a9ffab012
keywords:
- TCM_HITTEST message Windows Controls
topic_type:
- apiref
api_name:
- TCM_HITTEST
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TCM\_HITTEST message

Determines which tab, if any, is at a specified screen position. You can send this message explicitly or by using the [**TabCtrl\_HitTest**](/windows/desktop/api/Commctrl/nf-commctrl-tabctrl_hittest) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TCHITTESTINFO**](/windows/win32/api/commctrl/ns-commctrl-tchittestinfo) structure that specifies the screen position to test.

</dd> </dl>

## Return value

Returns the index of the tab, or -1 if no tab is at the specified position.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





