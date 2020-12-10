---
title: LVM_GETGROUPINFOBYINDEX message (Commctrl.h)
description: Gets information on a specified group. Send this message explicitly or by using the ListView\_GetGroupInfoByIndex macro.
ms.assetid: 'vs|controls|~\controls\listview\messages\lvm_getgroupinfobyindex.htm'
keywords:
- LVM_GETGROUPINFOBYINDEX message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETGROUPINFOBYINDEX
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETGROUPINFOBYINDEX message

Gets information on a specified group. Send this message explicitly or by using the [**ListView\_GetGroupInfoByIndex**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getgroupinfobyindex) macro.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

The index of the group.

</dd> <dt>

*lParam* \[in, out\]
</dt> <dd>

A pointer to an [**LVGROUP**](/windows/win32/api/commctrl/ns-commctrl-lvgroup) structure to receive information on the group specified by *wParam*. The calling process is responsible for allocating memory for the structure and any buffers in the structure, such as the one pointed to by the **pszHeader** member. Set any contingent members of the structure, such as **cchHeader** the size of the buffer pointed to by **pszHeader** in **WCHARs** including the terminating **NULL**. Set **cbSize** to sizeof(LVGROUP).

The message receiver is responsible for setting the structure members with information for the group specified by *wParam*.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





