---
title: LVM\_DELETEALLITEMS message
description: Removes all items from a list-view control. You can send this message explicitly or by using the ListView\_DeleteAllItems macro.
ms.assetid: 816bf565-79e9-4f5d-b5b4-5cdecce8a61c
keywords:
- LVM_DELETEALLITEMS message Windows Controls
topic_type:
- apiref
api_name:
- LVM_DELETEALLITEMS
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

# LVM\_DELETEALLITEMS message

Removes all items from a list-view control. You can send this message explicitly or by using the [**ListView\_DeleteAllItems**](/windows/win32/Commctrl/nf-commctrl-listview_deleteallitems?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

When a list-view control receives the **LVM\_DELETEALLITEMS** message, it sends the [**LVN\_DELETEALLITEMS**](lvn-deleteallitems.md) notification code to its parent window.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





