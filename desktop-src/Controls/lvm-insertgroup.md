---
title: LVM\_INSERTGROUP message
description: Inserts a group into a list-view control.
ms.assetid: d43e21bc-e212-42dd-af88-48813d40cd50
keywords:
- LVM_INSERTGROUP message Windows Controls
topic_type:
- apiref
api_name:
- LVM_INSERTGROUP
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

# LVM\_INSERTGROUP message

Inserts a group into a list-view control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Index where the group is to be added. If this is -1, the group is added at the end of the list.</dd> <dt>

*lParam* 
</dt> <dd>Pointer to a [**LVGROUP**](/windows/win32/Commctrl/ns-commctrl-taglvgroup?branch=master) structure that contains the group to add.</dd> </dl>

## Return value

Returns the index of the item that the group was added to, or -1 if the operation failed.

## Remarks

To turn on group mode, call [**LVM\_ENABLEGROUPVIEW**](lvm-enablegroupview.md) or [**ListView\_EnableGroupView**](/windows/win32/Commctrl/nf-commctrl-listview_enablegroupview?branch=master).

A group cannot be inserted into an empty list-view control.

Be sure to set the **iGroupId** in the item(s) the group was added to. Otherwise after [**LVM\_ENABLEGROUPVIEW**](lvm-enablegroupview.md) message processing with **TRUE** the listview control will not show any items.

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32 version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





