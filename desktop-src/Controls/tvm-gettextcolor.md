---
title: TVM_GETTEXTCOLOR message (Commctrl.h)
description: Retrieves the current text color of the control. You can send this message explicitly or by using the TreeView\_GetTextColor macro.
ms.assetid: fe1aa2e8-fdf2-48d1-936b-6d6bc8e589f4
keywords:
- TVM_GETTEXTCOLOR message Windows Controls
topic_type:
- apiref
api_name:
- TVM_GETTEXTCOLOR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_GETTEXTCOLOR message

Retrieves the current text color of the control. You can send this message explicitly or by using the [**TreeView\_GetTextColor**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_gettextcolor) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns a [**COLORREF**](/windows/desktop/gdi/colorref) value that represents the current text color. If this value is -1, the control is using the system color for the text color.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TVM\_SETTEXTCOLOR**](tvm-settextcolor.md)
</dt> </dl>

 

