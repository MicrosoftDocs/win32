---
title: TVM_SETINSERTMARKCOLOR message (Commctrl.h)
description: Sets the color used to draw the insertion mark for the tree view. You can send this message explicitly or by using the TreeView\_SetInsertMarkColor macro.
ms.assetid: c82304a8-3726-42c0-81e7-90d8f8205ead
keywords:
- TVM_SETINSERTMARKCOLOR message Windows Controls
topic_type:
- apiref
api_name:
- TVM_SETINSERTMARKCOLOR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_SETINSERTMARKCOLOR message

Sets the color used to draw the insertion mark for the tree view. You can send this message explicitly or by using the [**TreeView\_SetInsertMarkColor**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_setinsertmarkcolor) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

[**COLORREF**](/windows/desktop/gdi/colorref) value that contains the new insertion mark color.

</dd> </dl>

## Return value

Returns a **COLORREF** value that contains the previous insertion mark color.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TVM\_GETINSERTMARKCOLOR**](tvm-getinsertmarkcolor.md)
</dt> </dl>

 

