---
title: HDM_SETIMAGELIST message (Commctrl.h)
description: Assigns an image list to an existing header control. You can send this message explicitly or use the Header\_SetImageList or Header\_SetStateImageList macro.
ms.assetid: 1d7f07fa-f6f4-422a-949c-97d0388343e3
keywords:
- HDM_SETIMAGELIST message Windows Controls
topic_type:
- apiref
api_name:
- HDM_SETIMAGELIST
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# HDM\_SETIMAGELIST message

Assigns an image list to an existing header control. You can send this message explicitly or use the [**Header\_SetImageList**](/windows/desktop/api/Commctrl/nf-commctrl-header_setimagelist) or [**Header\_SetStateImageList**](/windows/desktop/api/Commctrl/nf-commctrl-header_setstateimagelist) macro.

## Parameters

<dl> <dt>*wParam* </dt> <dd>One of the following values:

| Value                                                                                                                                                      | Meaning                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| <span id="HDSIL_NORMAL"></span><span id="hdsil_normal"></span><dl> <dt>**HDSIL\_NORMAL**</dt> </dl> | Indicates that this is a normal image list.<br/> |
| <span id="HDSIL_STATE"></span><span id="hdsil_state"></span><dl> <dt>**HDSIL\_STATE**</dt> </dl>    | Indicates that this is a state image list.<br/>  |



 

</dd> <dt>

*lParam* 
</dt> <dd>

A handle to an image list.

</dd> </dl>

## Return value

Returns the handle to the image list previously associated with the control. Returns **NULL** upon failure or if no image list was set previously.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





