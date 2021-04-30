---
title: LVM_GETIMAGELIST message (Commctrl.h)
description: Retrieves the handle to an image list used for drawing list-view items. You can send this message explicitly or by using the ListView\_GetImageList macro.
ms.assetid: dd48d8b5-6dbd-48ab-95c3-0fcf1e8c24f0
keywords:
- LVM_GETIMAGELIST message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETIMAGELIST
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETIMAGELIST message

Retrieves the handle to an image list used for drawing list-view items. You can send this message explicitly or by using the [**ListView\_GetImageList**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getimagelist) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Image list to retrieve. This parameter can be one of the following values:



| Value                                                                                                                                                                     | Meaning                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| <span id="LVSIL_NORMAL"></span><span id="lvsil_normal"></span><dl> <dt>**LVSIL\_NORMAL**</dt> </dl>                | Image list with large icons.<br/>  |
| <span id="LVSIL_SMALL"></span><span id="lvsil_small"></span><dl> <dt>**LVSIL\_SMALL**</dt> </dl>                   | Image list with small icons.<br/>  |
| <span id="LVSIL_STATE"></span><span id="lvsil_state"></span><dl> <dt>**LVSIL\_STATE**</dt> </dl>                   | Image list with state images.<br/> |
| <span id="LVSIL_GROUPHEADER"></span><span id="lvsil_groupheader"></span><dl> <dt>**LVSIL\_GROUPHEADER**</dt> </dl> | Image list for group header.<br/>  |



 

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the handle to the specified image list if successful, or **NULL** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





