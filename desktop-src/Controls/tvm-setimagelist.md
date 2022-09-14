---
title: TVM_SETIMAGELIST message (Commctrl.h)
description: Sets the normal or state image list for a tree-view control and redraws the control using the new images. You can send this message explicitly or by using the TreeView\_SetImageList macro.
ms.assetid: 1a7bf2f8-c7db-44a8-b234-0ffc498e9000
keywords:
- TVM_SETIMAGELIST message Windows Controls
topic_type:
- apiref
api_name:
- TVM_SETIMAGELIST
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_SETIMAGELIST message

Sets the normal or state image list for a tree-view control and redraws the control using the new images. You can send this message explicitly or by using the [**TreeView\_SetImageList**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_setimagelist) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Type of image list to set. This parameter can be one of the following values:



| Value                                                                                                                                                      | Meaning                                                                                                                                                                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TVSIL_NORMAL"></span><span id="tvsil_normal"></span><dl> <dt>**TVSIL\_NORMAL**</dt> </dl> | Indicates the normal image list, which contains selected, nonselected, and overlay images for the items of a tree-view control.<br/>                                                          |
| <span id="TVSIL_STATE"></span><span id="tvsil_state"></span><dl> <dt>**TVSIL\_STATE**</dt> </dl>    | Indicates the state image list. You can use state images to indicate application-defined item states. A state image is displayed to the left of an item's selected or nonselected image.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the image list. If *lParam* is **NULL**, the message removes the specified image list from the tree-view control.

</dd> </dl>

## Return value

Returns the handle to the previous image list, if any, or **NULL** otherwise.

## Remarks

The tree-view control will not destroy the image list specified with this message. Your application must destroy the image list when it is no longer needed.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TVM\_GETIMAGELIST**](tvm-getimagelist.md)
</dt> </dl>

 

 





