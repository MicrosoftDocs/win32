---
title: LVM_SETIMAGELIST message (Commctrl.h)
description: Assigns an image list to a list-view control. You can send this message explicitly or by using the ListView\_SetImageList macro.
ms.assetid: 5241065b-85e4-412e-9868-fd5b15ff7c17
keywords:
- LVM_SETIMAGELIST message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETIMAGELIST
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_SETIMAGELIST message

Assigns an image list to a list-view control. You can send this message explicitly or by using the [**ListView\_SetImageList**](/windows/desktop/api/Commctrl/nf-commctrl-listview_setimagelist) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Type of image list. This parameter can be one of the following values:



| Value                                                                                                                                                                     | Meaning                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| <span id="LVSIL_NORMAL"></span><span id="lvsil_normal"></span><dl> <dt>**LVSIL\_NORMAL**</dt> </dl>                | Image list with large icons.<br/>  |
| <span id="LVSIL_SMALL"></span><span id="lvsil_small"></span><dl> <dt>**LVSIL\_SMALL**</dt> </dl>                   | Image list with small icons.<br/>  |
| <span id="LVSIL_STATE"></span><span id="lvsil_state"></span><dl> <dt>**LVSIL\_STATE**</dt> </dl>                   | Image list with state images.<br/> |
| <span id="LVSIL_GROUPHEADER"></span><span id="lvsil_groupheader"></span><dl> <dt>**LVSIL\_GROUPHEADER**</dt> </dl> | Image list for group header.<br/>  |



 

</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the image list to assign.

</dd> </dl>

## Return value

Returns the handle to the image list previously associated with the control if successful, or **NULL** otherwise.

## Remarks

The current image list will be destroyed when the list-view control is destroyed unless the [**LVS\_SHAREIMAGELISTS**](list-view-window-styles.md) style is set. If you use this message to replace one image list with another, your application must explicitly destroy all image lists other than the current one.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





