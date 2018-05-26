---
title: TVM\_GETITEMHEIGHT message
description: Retrieves the current height of the each tree-view item. You can send this message explicitly or by using the TreeView\_GetItemHeight macro.
ms.assetid: 017476a3-1929-4a31-97a7-0f66175d47ea
keywords:
- TVM_GETITEMHEIGHT message Windows Controls
topic_type:
- apiref
api_name:
- TVM_GETITEMHEIGHT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TVM\_GETITEMHEIGHT message

Retrieves the current height of the each tree-view item. You can send this message explicitly or by using the [**TreeView\_GetItemHeight**](/windows/win32/Commctrl/nf-commctrl-treeview_getitemheight?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the height of each item, in pixels.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TVM\_SETITEMHEIGHT**](tvm-setitemheight.md)
</dt> </dl>

 

 





