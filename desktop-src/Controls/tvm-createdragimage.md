---
title: TVM_CREATEDRAGIMAGE message (Commctrl.h)
description: Creates a dragging bitmap for the specified item in a tree-view control.
ms.assetid: fbe97921-c9d3-473c-933c-d6bc0599e24d
keywords:
- TVM_CREATEDRAGIMAGE message Windows Controls
topic_type:
- apiref
api_name:
- TVM_CREATEDRAGIMAGE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_CREATEDRAGIMAGE message

Creates a dragging bitmap for the specified item in a tree-view control. The message also creates an image list for the bitmap and adds the bitmap to the image list. An application can display the image when dragging the item by using the image list functions. You can send this message explicitly or by using the [**TreeView\_CreateDragImage**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_createdragimage) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the item that receives the new dragging bitmap.

</dd> </dl>

## Return value

Returns the handle to the image list to which the dragging bitmap was added if successful, or **NULL** otherwise.

## Remarks

If you create a tree-view control without an associated image list, you cannot use the **TVM\_CREATEDRAGIMAGE** message to create the image to display during a drag operation. You must implement your own method of creating a drag cursor.

Your application is responsible for destroying the image list when it is no longer needed.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





