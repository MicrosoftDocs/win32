---
title: TVM_SETBKCOLOR message (Commctrl.h)
description: Sets the background color of the control. You can send this message explicitly or by using the TreeView\_SetBkColor macro.
ms.assetid: 087f5e0b-ac73-4db4-b82e-15c7641b681c
keywords:
- TVM_SETBKCOLOR message Windows Controls
topic_type:
- apiref
api_name:
- TVM_SETBKCOLOR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_SETBKCOLOR message

Sets the background color of the control. You can send this message explicitly or by using the [**TreeView\_SetBkColor**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_setbkcolor) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

[**COLORREF**](/windows/desktop/gdi/colorref) value that contains the new background color. If this value is -1, the control will revert to using the system color for the background color.

</dd> </dl>

## Return value

Returns a [**COLORREF**](/windows/desktop/gdi/colorref) value that represents the previous background color. If this value is -1, the control was using the system color for the background color.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TVM\_GETBKCOLOR**](tvm-getbkcolor.md)
</dt> </dl>

 

