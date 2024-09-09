---
title: TCM_GETITEMRECT message (Commctrl.h)
description: Retrieves the bounding rectangle for a tab in a tab control. You can send this message explicitly or by using the TabCtrl\_GetItemRect macro.
ms.assetid: 6abd8cdf-5f19-4b7e-800e-970097bc891b
keywords:
- TCM_GETITEMRECT message Windows Controls
topic_type:
- apiref
api_name:
- TCM_GETITEMRECT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TCM\_GETITEMRECT message

Retrieves the bounding rectangle for a tab in a tab control. You can send this message explicitly or by using the [**TabCtrl\_GetItemRect**](/windows/desktop/api/Commctrl/nf-commctrl-tabctrl_getitemrect) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Index of the tab.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**RECT**](/windows/win32/api/windef/ns-windef-rect) structure that receives the bounding rectangle of the tab, in viewport coordinates.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

