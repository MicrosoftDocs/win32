---
title: TVM_GETINSERTMARKCOLOR message (Commctrl.h)
description: Retrieves the color used to draw the insertion mark for the tree view. You can send this message explicitly or by using the TreeView\_GetInsertMarkColor macro.
ms.assetid: d1fba4bb-1bdb-44e0-8083-b564cdafc055
keywords:
- TVM_GETINSERTMARKCOLOR message Windows Controls
topic_type:
- apiref
api_name:
- TVM_GETINSERTMARKCOLOR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_GETINSERTMARKCOLOR message

Retrieves the color used to draw the insertion mark for the tree view. You can send this message explicitly or by using the [**TreeView\_GetInsertMarkColor**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getinsertmarkcolor) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns a [**COLORREF**](/windows/desktop/gdi/colorref) value that contains the current insertion mark color.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TVM\_SETINSERTMARKCOLOR**](tvm-setinsertmarkcolor.md)
</dt> </dl>

 

