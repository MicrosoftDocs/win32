---
title: TCM_GETEXTENDEDSTYLE message (Commctrl.h)
description: Retrieves the extended styles that are currently in use for the tab control. You can send this message explicitly or by using the TabCtrl\_GetExtendedStyle macro.
ms.assetid: 983ffcbe-0d8d-4686-83de-fc564744390f
keywords:
- TCM_GETEXTENDEDSTYLE message Windows Controls
topic_type:
- apiref
api_name:
- TCM_GETEXTENDEDSTYLE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TCM\_GETEXTENDEDSTYLE message

Retrieves the extended styles that are currently in use for the tab control. You can send this message explicitly or by using the [**TabCtrl\_GetExtendedStyle**](/windows/desktop/api/Commctrl/nf-commctrl-tabctrl_getextendedstyle) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns a **DWORD** value that represents the extended styles currently in use for the tab control. This value is a combination of tab control [extended styles](tab-control-extended-styles.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TCM\_SETEXTENDEDSTYLE**](tcm-setextendedstyle.md)
</dt> </dl>

 

 





