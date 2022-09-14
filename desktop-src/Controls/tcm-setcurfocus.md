---
title: TCM_SETCURFOCUS message (Commctrl.h)
description: Sets the focus to a specified tab in a tab control. You can send this message explicitly or by using the TabCtrl\_SetCurFocus macro.
ms.assetid: bcbd5f26-b54e-492b-aff3-357b8ae23969
keywords:
- TCM_SETCURFOCUS message Windows Controls
topic_type:
- apiref
api_name:
- TCM_SETCURFOCUS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TCM\_SETCURFOCUS message

Sets the focus to a specified tab in a tab control. You can send this message explicitly or by using the [**TabCtrl\_SetCurFocus**](/windows/desktop/api/Commctrl/nf-commctrl-tabctrl_setcurfocus) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Index of the tab that gets the focus.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

No return value.

## Remarks

If the tab control has the [**TCS\_BUTTONS**](tab-control-styles.md) style (button mode), the tab with the focus may be different from the selected tab. For example, when a tab is selected, the user can press the arrow keys to set the focus to a different tab without changing the selected tab. In button mode, **TCM\_SETCURFOCUS** sets the input focus to the button associated with the specified tab, but it does not change the selected tab.

If the tab control does not have the [**TCS\_BUTTONS**](tab-control-styles.md) style, changing the focus also changes the selected tab. In this case, the tab control sends the [TCN\_SELCHANGING](tcn-selchanging.md) and [TCN\_SELCHANGE](tcn-selchange.md) notification codes to its parent window.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TCM\_GETCURFOCUS**](tcm-getcurfocus.md)
</dt> </dl>

 

 





