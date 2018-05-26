---
title: LVM\_HITTEST message
description: Determines which list-view item, if any, is at a specified position. You can send this message explicitly or by using the ListView\_HitTest macro.
ms.assetid: 81df4ed1-30bd-4b63-9cb9-5163cb7cf52c
keywords:
- LVM_HITTEST message Windows Controls
topic_type:
- apiref
api_name:
- LVM_HITTEST
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

# LVM\_HITTEST message

Determines which list-view item, if any, is at a specified position. You can send this message explicitly or by using the [**ListView\_HitTest**](/windows/win32/Commctrl/nf-commctrl-listview_hittest?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be 0. **Windows Vista.** Should be -1 if the **iGroup** and **iSubItem** members of the *lParam* structure are to be retrieved.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**LVHITTESTINFO**](/windows/win32/Commctrl/ns-commctrl-taglvhittestinfo?branch=master) structure that contains the position to hit test and receives information about the results of the hit test.

</dd> </dl>

## Return value

Returns the index of the item at the specified position, if any, or -1 otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





