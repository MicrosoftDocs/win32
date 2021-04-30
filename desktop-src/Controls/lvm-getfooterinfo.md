---
title: LVM_GETFOOTERINFO message (Commctrl.h)
description: Gets information about the footer of a list-view control. Send this message explicitly or by using the ListView\_GetFooterInfo macro.
ms.assetid: 5734e151-50c0-46df-8f2c-220c4910a590
keywords:
- LVM_GETFOOTERINFO message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETFOOTERINFO
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETFOOTERINFO message

Gets information about the footer of a list-view control. Send this message explicitly or by using the [**ListView\_GetFooterInfo**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getfooterinfo) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used. Must be 0.

</dd> <dt>

*lParam* \[in, out\]
</dt> <dd>

A pointer to a [**LVFOOTERINFO**](/windows/win32/api/commctrl/ns-commctrl-lvfooterinfo) structure to receive information depending on the value of the **mask** member. The calling process is responsible for allocating this structure and setting the **mask** member.

</dd> </dl>

## Return value

Returns **TRUE**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





