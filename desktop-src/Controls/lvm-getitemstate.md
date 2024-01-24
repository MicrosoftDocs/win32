---
title: LVM_GETITEMSTATE message (Commctrl.h)
description: Retrieves the state of a list-view item. You can send this message explicitly or by using the ListView\_GetItemState macro.
ms.assetid: 862960ed-a64a-4d66-b384-9228932eae6f
keywords:
- LVM_GETITEMSTATE message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETITEMSTATE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETITEMSTATE message

Retrieves the state of a list-view item. You can send this message explicitly or by using the [**ListView\_GetItemState**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getitemstate) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Index of the list-view item.

</dd> <dt>

*lParam* 
</dt> <dd>

State information to retrieve. This parameter can be a combination of the following values:



| Value                                                                                                                                                                           | Meaning                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="LVIS_CUT"></span><span id="lvis_cut"></span><dl> <dt>**LVIS\_CUT**</dt> </dl>                                  | The item is marked for a cut-and-paste operation.<br/>                                                                                                         |
| <span id="LVIS_DROPHILITED"></span><span id="lvis_drophilited"></span><dl> <dt>**LVIS\_DROPHILITED**</dt> </dl>          | The item is highlighted as a drag-and-drop target.<br/>                                                                                                        |
| <span id="LVIS_FOCUSED"></span><span id="lvis_focused"></span><dl> <dt>**LVIS\_FOCUSED**</dt> </dl>                      | The item has the focus, so it is surrounded by a standard focus rectangle. Although more than one item may be selected, only one item can have the focus.<br/> |
| <span id="LVIS_SELECTED"></span><span id="lvis_selected"></span><dl> <dt>**LVIS\_SELECTED**</dt> </dl>                   | The item is selected. The appearance of a selected item depends on whether it has the focus and also on the system colors used for selection.<br/>             |
| <span id="LVIS_OVERLAYMASK"></span><span id="lvis_overlaymask"></span><dl> <dt>**LVIS\_OVERLAYMASK**</dt> </dl>          | Use this mask to retrieve the item's overlay image index.<br/>                                                                                                 |
| <span id="LVIS_STATEIMAGEMASK"></span><span id="lvis_stateimagemask"></span><dl> <dt>**LVIS\_STATEIMAGEMASK**</dt> </dl> | Use this mask to retrieve the item's state image index.<br/>                                                                                                   |



 

</dd> </dl>

## Return value

Returns the current state for the specified item. The only valid bits in the return value are those that correspond to the bits set in the *lParam* parameter.

## Remarks

An item's state information includes a set of bit flags as well as image list indexes that indicate the item's state image and overlay image.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**LVM\_SETITEMSTATE**](lvm-setitemstate.md)
</dt> </dl>

 

 





