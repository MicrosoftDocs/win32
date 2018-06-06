---
title: MCM\_GETCURSEL message
description: Retrieves the currently selected date. You can send this message explicitly or by using the MonthCal\_GetCurSel macro.
ms.assetid: d4edc9ed-7c92-4ec8-bfa1-8ae597826b3f
keywords:
- MCM_GETCURSEL message Windows Controls
topic_type:
- apiref
api_name:
- MCM_GETCURSEL
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MCM\_GETCURSEL message

Retrieves the currently selected date. You can send this message explicitly or by using the [**MonthCal\_GetCurSel**](/windows/desktop/api/Commctrl/nf-commctrl-monthcal_getcursel) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**SYSTEMTIME**](https://msdn.microsoft.com/library/windows/desktop/ms724950) structure that will receive the currently selected date information. This parameter must be a valid address and cannot be **NULL**.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise. This message will always fail when applied to month calendar controls set to the [**MCS\_MULTISELECT**](month-calendar-control-styles.md#mcs-multiselect) style.

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

 

 





