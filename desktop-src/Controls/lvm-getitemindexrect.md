---
title: LVM_GETITEMINDEXRECT message (Commctrl.h)
description: Retrieves the bounding rectangle for all or part of a subitem in the current view of a list-view control. Send this message explicitly or by using the ListView\_GetItemIndexRect macro.
ms.assetid: 17704d24-c029-4d41-b198-04d1e78698e0
keywords:
- LVM_GETITEMINDEXRECT message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETITEMINDEXRECT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETITEMINDEXRECT message

Retrieves the bounding rectangle for all or part of a subitem in the current view of a list-view control. Send this message explicitly or by using the [**ListView\_GetItemIndexRect**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getitemindexrect) macro.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

A pointer to a [**LVITEMINDEX**](/windows/win32/api/commctrl/ns-commctrl-lvitemindex) structure for the parent item of the subitem. The calling process is responsible for allocating this structure and setting its members. *wParam* must not be **NULL**.

</dd> <dt>

*lParam* \[in, out\]
</dt> <dd>

A pointer to a [**RECT**](/previous-versions//dd162897(v=vs.85)) structure to receive the coordinates. The calling process is responsible for allocating this structure. *lParam* must not be **NULL**. Set the **top** member to the index of the subitem. Set the **left** member to one of the following values, indicating the part of the subitem for which the bounding rectangle is to be retrieved.



| Value                                                                                                                                                   | Meaning                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| <span id="LVIR_BOUNDS"></span><span id="lvir_bounds"></span><dl> <dt>**LVIR\_BOUNDS**</dt> </dl> | Returns the bounding rectangle of the entire subitem, including the icon and label.<br/> |
| <span id="LVIR_ICON"></span><span id="lvir_icon"></span><dl> <dt>**LVIR\_ICON**</dt> </dl>       | Returns the bounding rectangle of the icon or small icon of the subitem.<br/>            |
| <span id="LVIR_LABEL"></span><span id="lvir_label"></span><dl> <dt>**LVIR\_LABEL**</dt> </dl>    | Returns the bounding rectangle of the subitem text.<br/>                                 |



 

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

