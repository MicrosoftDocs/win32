---
title: LVM\_GETGROUPSTATE message
description: Gets the state for a specified group. Send this message explicitly or by using the ListView\_GetGroupState macro.
ms.assetid: f087d17f-9066-44fb-b21b-ac7ceb56eb45
keywords:
- LVM_GETGROUPSTATE message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETGROUPSTATE
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

# LVM\_GETGROUPSTATE message

Gets the state for a specified group. Send this message explicitly or by using the [**ListView\_GetGroupState**](/windows/win32/Commctrl/nf-commctrl-listview_getgroupstate?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

Specifies the group by **iGroupId** (see [**LVGROUP**](/windows/win32/Commctrl/ns-commctrl-taglvgroup?branch=master) structure).

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

Specifies the state values to retrieve. This is a combination of the flags listed for the **state** member of [**LVGROUP**](/windows/win32/Commctrl/ns-commctrl-taglvgroup?branch=master).

</dd> </dl>

## Return value

Returns the combination of state values that are set. For example, if *lParam* is LVGS\_COLLAPSED and the value returned is zero, the LVGS\_COLLAPSED state is not set. Zero is returned if the group is not found.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





