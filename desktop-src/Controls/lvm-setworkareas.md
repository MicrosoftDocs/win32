---
title: LVM_SETWORKAREAS message (Commctrl.h)
description: Sets the working areas within a list-view control. You can send this message explicitly or use the ListView\_SetWorkAreas macro.
ms.assetid: 87ac192d-f481-43ac-b8a5-c754cf33e487
keywords:
- LVM_SETWORKAREAS message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETWORKAREAS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_SETWORKAREAS message

Sets the working areas within a list-view control. You can send this message explicitly or use the [**ListView\_SetWorkAreas**](/windows/desktop/api/Commctrl/nf-commctrl-listview_setworkareas) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The number of structures in the array at *lprc*. The maximum number of working areas allowed is defined by the LV\_MAX\_WORKAREAS value.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an array of [**RECT**](/windows/win32/api/windef/ns-windef-rect) structures that contain the new working areas of the list-view control. Values in these structures are in client coordinates. If this parameter is **NULL**, the working area will be set to the client area of the control. *wParam* specifies the number of structures in this array.

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

 

