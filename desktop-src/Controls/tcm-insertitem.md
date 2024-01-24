---
title: TCM_INSERTITEM message (Commctrl.h)
description: Inserts a new tab in a tab control. You can send this message explicitly or by using the TabCtrl\_InsertItem macro.
ms.assetid: e547c49a-699c-4137-8680-20391d138d54
keywords:
- TCM_INSERTITEM message Windows Controls
topic_type:
- apiref
api_name:
- TCM_INSERTITEM
- TCM_INSERTITEMA
- TCM_INSERTITEMW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TCM\_INSERTITEM message

Inserts a new tab in a tab control. You can send this message explicitly or by using the [**TabCtrl\_InsertItem**](/windows/desktop/api/Commctrl/nf-commctrl-tabctrl_insertitem) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Index of the new tab.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TCITEM**](/windows/win32/api/commctrl/ns-commctrl-tcitema) structure that specifies the attributes of the tab. The **dwState** and **dwStateMask** members of this structure are ignored by this message.

</dd> </dl>

## Return value

Returns the index of the new tab if successful, or -1 otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TCM\_INSERTITEMW** (Unicode) and **TCM\_INSERTITEMA** (ANSI)<br/>             |



 

 





