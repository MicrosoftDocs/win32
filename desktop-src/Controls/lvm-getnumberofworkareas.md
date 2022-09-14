---
title: LVM_GETNUMBEROFWORKAREAS message (Commctrl.h)
description: Retrieves the number of working areas in a list-view control. You can send this message explicitly or use the ListView\_GetNumberOfWorkAreas macro.
ms.assetid: ce0bcccd-62a2-45a4-959e-9959c9ca0c46
keywords:
- LVM_GETNUMBEROFWORKAREAS message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETNUMBEROFWORKAREAS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETNUMBEROFWORKAREAS message

Retrieves the number of working areas in a list-view control. You can send this message explicitly or use the [**ListView\_GetNumberOfWorkAreas**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getnumberofworkareas) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a UINT value that receives the number of working areas in the list-view control. If zero is placed in this variable, then no working areas are currently set. This value cannot be **NULL**.

</dd> </dl>

## Return value

The return value for this message is not used.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[Using List-View Controls](using-list-view-controls.md)
</dt> </dl>

 

 





