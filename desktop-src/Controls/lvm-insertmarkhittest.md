---
title: LVM_INSERTMARKHITTEST message (Commctrl.h)
description: Retrieves the insertion point closest to a specified point.
ms.assetid: 901bb770-a36d-4d9f-a53b-d497b4df39e5
keywords:
- LVM_INSERTMARKHITTEST message Windows Controls
topic_type:
- apiref
api_name:
- LVM_INSERTMARKHITTEST
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_INSERTMARKHITTEST message

Retrieves the insertion point closest to a specified point.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Pointer to a **POINT** structure that contains the hit test coordinates.</dd> <dt>

*lParam* 
</dt> <dd>Pointer to an <a href="/windows/desktop/api/Commctrl/ns-commctrl-lvinsertmark">LVINSERTMARK</a> structure that specifies the insertion point closest to the coordinates defined by the *wParam* parameter.</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise. **FALSE** is returned if the size in the **cbSize** member of the [**LVINSERTMARK**](/windows/desktop/api/Commctrl/ns-commctrl-lvinsertmark) structure does not equal the actual size of the structure, or when an insertion point does not apply in the current view.

## Remarks

An insertion point can only appear if the list-view control is in icon view, small icon view, or tile view and is not in group-view mode.

If insertion points do not apply for the view, the [**LVINSERTMARK**](/windows/desktop/api/Commctrl/ns-commctrl-lvinsertmark) structure contains a -1 in the **iItem** member.

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





