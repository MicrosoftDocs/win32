---
title: LVM_SETGROUPINFO message (Commctrl.h)
description: Sets group information.
ms.assetid: f79bd235-e2de-4055-be3e-76eb2744e1ee
keywords:
- LVM_SETGROUPINFO message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETGROUPINFO
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_SETGROUPINFO message

Sets group information. Send this message explicitly or by using the [**ListView\_SetGroupInfo**](/windows/desktop/api/Commctrl/nf-commctrl-listview_setgroupinfo) macro.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>ID that specifies the group whose information is to be set.</dd> <dt>

*lParam* \[in, out\]
</dt> <dd>Pointer to a [**LVGROUP**](windows/win32/api/commctrl/ns-commctrl-lvgroup) structure that contains the information to set.</dd> </dl>

## Return value

Returns the ID of the group if successful, or -1 otherwise.

## Remarks

To change a group ID of an existing group add <b>LVGF_GROUPID</b> to <b>LVGROUP.mask</b> and set <b>LVGROUP.iGroupId</b> to the new ID. The call will fail if <b>LVGROUP.iGroupId</b> contains ID of an existing group.

To update other properties of an existing group (e.g. update an alignment of the header or footer text for the group, <b>uAlign</b>) <b>LVGROUP.mask</b> must not contain <b>LVGF_GROUPID</b>, else the update will fail.

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





