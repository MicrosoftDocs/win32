---
title: BCM_SETDROPDOWNSTATE message (Commctrl.h)
description: Sets the drop down state for a button with style TBSTYLE\_DROPDOWN. Send this message explicitly or by using the Button\_SetDropDownState macro.
ms.assetid: 725deff4-0bcb-497d-a6cf-e9c98b05f16e
keywords:
- BCM_SETDROPDOWNSTATE message Windows Controls
topic_type:
- apiref
api_name:
- BCM_SETDROPDOWNSTATE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# BCM\_SETDROPDOWNSTATE message

Sets the drop down state for a button with style [**TBSTYLE\_DROPDOWN**](toolbar-control-and-button-styles.md). Send this message explicitly or by using the [**Button\_SetDropDownState**](/windows/desktop/api/Commctrl/nf-commctrl-button_setdropdownstate) macro.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

A **BOOL** that is **TRUE** for state of BST\_DROPDOWNPUSHED, or **FALSE** otherwise.

</dd> <dt>

*lParam* 
</dt> <dd>

Must be zero.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[Button Styles](button-styles.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Button Types](button-types-and-styles.md)
</dt> </dl>

 

 





