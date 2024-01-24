---
title: TBM_SETTIPSIDE message (Commctrl.h)
description: Positions a tooltip control used by a trackbar control. Trackbar controls that use the TBS\_TOOLTIPS style display tooltips.
ms.assetid: 40a0eeb0-7bb4-4102-98ea-ee664799b934
keywords:
- TBM_SETTIPSIDE message Windows Controls
topic_type:
- apiref
api_name:
- TBM_SETTIPSIDE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBM\_SETTIPSIDE message

Positions a tooltip control used by a trackbar control. Trackbar controls that use the [**TBS\_TOOLTIPS**](trackbar-control-styles.md) style display tooltips.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Value representing the location at which to display the tooltip control. This value can be one of the following:



| Value                                                                                                                                                   | Meaning                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| <span id="TBTS_TOP"></span><span id="tbts_top"></span><dl> <dt>**TBTS\_TOP**</dt> </dl>          | The tooltip control will be positioned above the trackbar. This flag is for use with horizontal trackbars.<br/>         |
| <span id="TBTS_LEFT"></span><span id="tbts_left"></span><dl> <dt>**TBTS\_LEFT**</dt> </dl>       | The tooltip control will be positioned to the left of the trackbar. This flag is for use with vertical trackbars.<br/>  |
| <span id="TBTS_BOTTOM"></span><span id="tbts_bottom"></span><dl> <dt>**TBTS\_BOTTOM**</dt> </dl> | The tooltip control will be positioned below the trackbar. This flag is for use with horizontal trackbars.<br/>         |
| <span id="TBTS_RIGHT"></span><span id="tbts_right"></span><dl> <dt>**TBTS\_RIGHT**</dt> </dl>    | The tooltip control will be positioned to the right of the trackbar. This flag is for use with vertical trackbars.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns a value that represents the tooltip control's previous location. The return value equals one of the possible values for *wParam*.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





