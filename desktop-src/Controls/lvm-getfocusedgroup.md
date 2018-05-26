---
title: LVM\_GETFOCUSEDGROUP message
description: Gets the group that has the focus. Send this message explicitly or by using the ListView\_GetFocusedGroup macro.
ms.assetid: c1902f35-84b7-4f46-89a6-e48148f06172
keywords:
- LVM_GETFOCUSEDGROUP message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETFOCUSEDGROUP
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

# LVM\_GETFOCUSEDGROUP message

Gets the group that has the focus. Send this message explicitly or by using the [**ListView\_GetFocusedGroup**](/windows/win32/Commctrl/nf-commctrl-listview_getfocusedgroup?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the index of the group with state of LVGS\_FOCUSED, or -1 if there is no group with state of LVGS\_FOCUSED.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





