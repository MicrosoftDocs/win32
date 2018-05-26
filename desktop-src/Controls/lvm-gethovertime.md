---
title: LVM\_GETHOVERTIME message
description: Retrieves the amount of time that the mouse cursor must hover over an item before it is selected. You can send this message explicitly or use the ListView\_GetHoverTime macro.
ms.assetid: e7646024-f868-459f-88be-b232b6b4bb2a
keywords:
- LVM_GETHOVERTIME message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETHOVERTIME
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

# LVM\_GETHOVERTIME message

Retrieves the amount of time that the mouse cursor must hover over an item before it is selected. You can send this message explicitly or use the [**ListView\_GetHoverTime**](/windows/win32/Commctrl/nf-commctrl-listview_gethovertime?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the amount of time, in milliseconds, that the mouse cursor must hover over an item before it is selected. If the return value is (**DWORD**)-1, then the hover time is the default hover time.

## Remarks

The hover time only affects list-view controls that have the [**LVS\_EX\_TRACKSELECT**](extended-list-view-styles.md#lvs-ex-trackselect), [**LVS\_EX\_ONECLICKACTIVATE**](extended-list-view-styles.md#lvs-ex-oneclickactivate), or [**LVS\_EX\_TWOCLICKACTIVATE**](extended-list-view-styles.md#lvs-ex-twoclickactivate) extended list-view style.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





