---
title: TVM\_GETIMAGELIST message
description: Retrieves the handle to the normal or state image list associated with a tree-view control. You can send this message explicitly or by using the TreeView\_GetImageList macro.
ms.assetid: bcf5eac8-cb07-4cf8-ad93-47319fc915a5
keywords:
- TVM_GETIMAGELIST message Windows Controls
topic_type:
- apiref
api_name:
- TVM_GETIMAGELIST
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

# TVM\_GETIMAGELIST message

Retrieves the handle to the normal or state image list associated with a tree-view control. You can send this message explicitly or by using the [**TreeView\_GetImageList**](/windows/win32/Commctrl/nf-commctrl-treeview_getimagelist?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Type of image list to retrieve. This parameter can be one of the following values:



| Value                                                                                                                                                      | Meaning                                                                                                                                                                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TVSIL_NORMAL"></span><span id="tvsil_normal"></span><dl> <dt>**TVSIL\_NORMAL**</dt> </dl> | Indicates the normal image list, which contains selected, nonselected, and overlay images for the items of a tree-view control.<br/>                                                          |
| <span id="TVSIL_STATE"></span><span id="tvsil_state"></span><dl> <dt>**TVSIL\_STATE**</dt> </dl>    | Indicates the state image list. You can use state images to indicate application-defined item states. A state image is displayed to the left of an item's selected or nonselected image.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns an HIMAGELIST handle to the specified image list.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TVM\_SETIMAGELIST**](tvm-setimagelist.md)
</dt> </dl>

 

 





