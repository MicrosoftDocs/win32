---
title: MCM\_SETCURSEL message
description: Sets the currently selected date for a month calendar control. If the specified date is not in view, the control updates the display to bring it into view. You can send this message explicitly or by using the MonthCal\_SetCurSel macro.
ms.assetid: 2a9f82a1-66d9-44dd-b60f-b588b4688316
keywords:
- MCM_SETCURSEL message Windows Controls
topic_type:
- apiref
api_name:
- MCM_SETCURSEL
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MCM\_SETCURSEL message

Sets the currently selected date for a month calendar control. If the specified date is not in view, the control updates the display to bring it into view. You can send this message explicitly or by using the [**MonthCal\_SetCurSel**](/windows/win32/Commctrl/nf-commctrl-monthcal_setcursel?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**SYSTEMTIME**](https://msdn.microsoft.com/library/windows/desktop/ms724950) structure that contains the date to be set as the current selection.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise. This message will fail if applied to a month calendar control that uses the [**MCS\_MULTISELECT**](month-calendar-control-styles.md#mcs-multiselect) style.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[Times in the Month Calendar Control](month-calendar-controls.md#times-in-the-month-calendar-control)
</dt> </dl>

 

 





