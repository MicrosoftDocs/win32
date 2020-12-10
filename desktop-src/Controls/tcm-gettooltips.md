---
title: TCM_GETTOOLTIPS message (Commctrl.h)
description: Retrieves the handle to the tooltip control associated with a tab control. You can send this message explicitly or by using the TabCtrl\_GetToolTips macro.
ms.assetid: d7dcca4f-8629-4eeb-844f-b3171438f528
keywords:
- TCM_GETTOOLTIPS message Windows Controls
topic_type:
- apiref
api_name:
- TCM_GETTOOLTIPS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TCM\_GETTOOLTIPS message

Retrieves the handle to the tooltip control associated with a tab control. You can send this message explicitly or by using the [**TabCtrl\_GetToolTips**](/windows/desktop/api/Commctrl/nf-commctrl-tabctrl_gettooltips) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the handle to the tooltip control if successful, or **NULL** otherwise.

## Remarks

A tab control creates a tooltip control if it has the [**TCS\_TOOLTIPS**](tab-control-styles.md) style. You can also assign a tooltip control to a tab control by using the [**TCM\_SETTOOLTIPS**](tcm-settooltips.md) message.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





