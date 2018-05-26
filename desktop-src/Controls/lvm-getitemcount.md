---
title: LVM\_GETITEMCOUNT message
description: Retrieves the number of items in a list-view control. You can send this message explicitly or by using the ListView\_GetItemCount macro.
ms.assetid: 7c639d69-e42c-41b5-9fdd-4943166752a2
keywords:
- LVM_GETITEMCOUNT message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETITEMCOUNT
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

# LVM\_GETITEMCOUNT message

Retrieves the number of items in a list-view control. You can send this message explicitly or by using the [**ListView\_GetItemCount**](/windows/win32/Commctrl/nf-commctrl-listview_getitemcount?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the number of items.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





