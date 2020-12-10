---
title: LVM_GETFOOTERITEM message (Commctrl.h)
description: Gets information on a footer item in a list-view control. Send this message explicitly or by using the ListView\_GetFooterItem macro.
ms.assetid: 92f55719-c265-433f-84fc-a673680c7ad9
keywords:
- LVM_GETFOOTERITEM message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETFOOTERITEM
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETFOOTERITEM message

Gets information on a footer item in a list-view control. Send this message explicitly or by using the [**ListView\_GetFooterItem**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getfooteritem) macro.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

The index of the item.

</dd> <dt>

*lParam* \[in, out\]
</dt> <dd>

A pointer to a [**LVFOOTERITEM**](/windows/win32/api/commctrl/ns-commctrl-lvfooteritem) structure to receive a value for the **state** and/or **pszText** members according to the value of the **mask** member. The calling process is responsible for allocating this structure and setting its members to indicate to the receiver what information to return. For more information, see **LVFOOTERITEM**.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





