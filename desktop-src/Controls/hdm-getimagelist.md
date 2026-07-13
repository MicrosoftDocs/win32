---
title: HDM_GETIMAGELIST message (Commctrl.h)
description: Gets the handle to the image list that has been set for an existing header control. You can send this message explicitly or use the Header\_GetImageList or Header\_GetStateImageList macro.
ms.assetid: 3e1a979c-60c5-4538-bd4d-16238829062e
keywords:
- HDM_GETIMAGELIST message Windows Controls
topic_type:
- apiref
api_name:
- HDM_GETIMAGELIST
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# HDM_GETIMAGELIST message

Gets the handle to the image list that has been set for an existing header control. You can send this message explicitly or use the [**Header\_GetImageList**](/windows/desktop/api/Commctrl/nf-commctrl-header_getimagelist) or [**Header\_GetStateImageList**](/windows/desktop/api/Commctrl/nf-commctrl-header_getstateimagelist) macro.

## Parameters

*wParam*

One of the following values:

| Value                                                                                                                                                      | Meaning                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| <span id="HDSIL_NORMAL"></span><span id="hdsil_normal"></span><dl> <dt>**HDSIL\_NORMAL**</dt> </dl> | Indicates that this is a normal image list.<br/> |
| <span id="HDSIL_STATE"></span><span id="hdsil_state"></span><dl> <dt>**HDSIL\_STATE**</dt> </dl>    | Indicates that this is a state image list.<br/>  |

*lParam*

Must be zero.

## Return value

Returns a handle to the image list set for the header control.

## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
