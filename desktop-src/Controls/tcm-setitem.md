---
title: TCM\_SETITEM message
description: Sets some or all of a tab's attributes. You can send this message explicitly or by using the TabCtrl\_SetItem macro.
ms.assetid: '1d9c6607-d8ec-4644-a714-22bc2677aa78'
keywords: ["TCM_SETITEM message Windows Controls"]
topic_type:
- apiref
api_name:
- TCM_SETITEM
- TCM_SETITEMA
- TCM_SETITEMW
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# TCM\_SETITEM message

Sets some or all of a tab's attributes. You can send this message explicitly or by using the [**TabCtrl\_SetItem**](tabctrl-setitem.md) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Index of the item.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TCITEM**](tcitem.md) structure that contains the new item attributes. The **mask** member specifies which attributes to set. If the **mask** member specifies the TCIF\_TEXT value, the **pszText** member is the address of a null-terminated string and the **cchTextMax** member is ignored.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TCM\_SETITEMW** (Unicode) and **TCM\_SETITEMA** (ANSI)<br/>                   |



 

 





