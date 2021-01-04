---
title: LVM_CREATEDRAGIMAGE message (Commctrl.h)
description: Creates a drag image list for the specified item. You can send this message explicitly or by using the ListView\_CreateDragImage macro.
ms.assetid: face4c8f-01ff-4f5a-a468-e306a50dae35
keywords:
- LVM_CREATEDRAGIMAGE message Windows Controls
topic_type:
- apiref
api_name:
- LVM_CREATEDRAGIMAGE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_CREATEDRAGIMAGE message

Creates a drag image list for the specified item. You can send this message explicitly or by using the [**ListView\_CreateDragImage**](/windows/desktop/api/Commctrl/nf-commctrl-listview_createdragimage) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The index of the item.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**POINT**](/previous-versions//dd162805(v=vs.85)) structure that receives the initial location of the upper-left corner of the image, in view coordinates.

</dd> </dl>

## Return value

Returns the handle to the drag image list if successful, or **NULL** otherwise.

## Remarks

Your application is responsible for destroying the image list when it is no longer needed.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

