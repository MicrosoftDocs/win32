---
title: LVM_GETITEMRECT message (Commctrl.h)
description: Retrieves the bounding rectangle for all or part of an item in the current view. You can send this message explicitly or by using the ListView\_GetItemRect macro.
ms.assetid: 7ce74b65-3360-42b4-9889-d90aefe2d284
keywords:
- LVM_GETITEMRECT message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETITEMRECT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETITEMRECT message

Retrieves the bounding rectangle for all or part of an item in the current view. You can send this message explicitly or by using the [**ListView\_GetItemRect**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getitemrect) macro.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

Index of the list-view item.

</dd> <dt>

*lParam* \[in, out\]
</dt> <dd>

Pointer to a [**RECT**](/windows/win32/api/windef/ns-windef-rect) structure that receives the bounding rectangle. When the message is sent, the **left** member of this structure is used to specify the portion of the list-view item from which to retrieve the bounding rectangle. It must be set to one of the following values:



| Value                                                                                                                                                                     | Meaning                                                                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| <span id="LVIR_BOUNDS"></span><span id="lvir_bounds"></span><dl> <dt>**LVIR\_BOUNDS**</dt> </dl>                   | Returns the bounding rectangle of the entire item, including the icon and label.<br/>                     |
| <span id="LVIR_ICON"></span><span id="lvir_icon"></span><dl> <dt>**LVIR\_ICON**</dt> </dl>                         | Returns the bounding rectangle of the icon or small icon.<br/>                                            |
| <span id="LVIR_LABEL"></span><span id="lvir_label"></span><dl> <dt>**LVIR\_LABEL**</dt> </dl>                      | Returns the bounding rectangle of the item text.<br/>                                                     |
| <span id="LVIR_SELECTBOUNDS"></span><span id="lvir_selectbounds"></span><dl> <dt>**LVIR\_SELECTBOUNDS**</dt> </dl> | Returns the union of the LVIR\_ICON and LVIR\_LABEL rectangles, but excludes columns in report view.<br/> |



 

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

