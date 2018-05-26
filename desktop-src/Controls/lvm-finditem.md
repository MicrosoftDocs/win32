---
title: LVM\_FINDITEM message
description: Searches for a list-view item with the specified characteristics. You can send this message explicitly or by using the ListView\_FindItem macro.
ms.assetid: 3b18c8ad-97e6-4f4d-bf89-afb95f925ed1
keywords:
- LVM_FINDITEM message Windows Controls
topic_type:
- apiref
api_name:
- LVM_FINDITEM
- LVM_FINDITEMA
- LVM_FINDITEMW
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

# LVM\_FINDITEM message

Searches for a list-view item with the specified characteristics. You can send this message explicitly or by using the [**ListView\_FindItem**](/windows/win32/Commctrl/nf-commctrl-listview_finditem?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The index of the item to begin the search with or -1 to start from the beginning. The specified item is itself excluded from the search.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**LVFINDINFO**](/windows/win32/Commctrl/ns-commctrl-taglvfindinfoa?branch=master) structure that contains information about what to search for.

</dd> </dl>

## Return value

Returns the index of the item if successful, or -1 otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **LVM\_FINDITEMW** (Unicode) and **LVM\_FINDITEMA** (ANSI)<br/>                 |



 

 





