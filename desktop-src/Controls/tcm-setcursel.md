---
title: TCM\_SETCURSEL message
description: Selects a tab in a tab control. You can send this message explicitly or by using the TabCtrl\_SetCurSel macro.
ms.assetid: 'cf709d8c-c522-47c8-8ff3-463dc8e924b5'
keywords: ["TCM_SETCURSEL message Windows Controls"]
topic_type:
- apiref
api_name:
- TCM_SETCURSEL
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# TCM\_SETCURSEL message

Selects a tab in a tab control. You can send this message explicitly or by using the [**TabCtrl\_SetCurSel**](tabctrl-setcursel.md) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Index of the tab to select.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the index of the previously selected tab if successful, or -1 otherwise.

## Remarks

A tab control does not send a [TCN\_SELCHANGING](tcn-selchanging.md) or [TCN\_SELCHANGE](tcn-selchange.md) notification code when a tab is selected using this message.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





