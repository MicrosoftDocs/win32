---
title: LVM_GETGROUPRECT message (Commctrl.h)
description: Gets the rectangle for a specified group. Send this message explicitly or by using the ListView\_GetGroupRect macro.
ms.assetid: 9441a6c5-11d8-4f52-80dd-1b60befd9b9d
keywords:
- LVM_GETGROUPRECT message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETGROUPRECT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETGROUPRECT message

Gets the rectangle for a specified group. Send this message explicitly or by using the [**ListView\_GetGroupRect**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getgrouprect) macro.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

Specifies the group by **iGroupId** (see [**LVGROUP**](/windows/win32/api/commctrl/ns-commctrl-lvgroup) structure).

</dd> <dt>

*lParam* \[in, out\]
</dt> <dd>

A pointer to a [**RECT**](/previous-versions//dd162897(v=vs.85)) structure to receive information on the group specified by *wParam*. The message receiver is responsible for setting the structure members with information for the group specified by *wParam*.

The calling process is responsible for allocating memory for the structure. Set the **top** member of the [**RECT**](/previous-versions//dd162897(v=vs.85)) to one of the following flags to specify the coordinates of the rectangle to get.



| Value                                                                                                                                                                  | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="LVGGR_GROUP"></span><span id="lvggr_group"></span><dl> <dt>**LVGGR\_GROUP**</dt> </dl>                | Coordinates of the entire expanded group.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <span id="LVGGR_HEADER"></span><span id="lvggr_header"></span><dl> <dt>**LVGGR\_HEADER**</dt> </dl>             | Coordinates of the header only (collapsed group).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <span id="LVGGR_LABEL"></span><span id="lvggr_label"></span><dl> <dt>**LVGGR\_LABEL**</dt> </dl>                | Coordinates of the label only.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <span id="LVGGR_SUBSETLINK"></span><span id="lvggr_subsetlink"></span><dl> <dt>**LVGGR\_SUBSETLINK**</dt> </dl> | Coordinates of the subset link only (markup subset). A list-view control can limit the number of visible items displayed in each group. A link is presented to the user to allow the user to expand the group. This flag will return the bounding rectangle of the subset link if the group is a subset (group state of LVGS\_SUBSETED, see structure [**LVGROUP**](/windows/win32/api/commctrl/ns-commctrl-lvgroup), member **state**). This flag is provided so that accessibility applications can located the link.<br/> |



 

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

