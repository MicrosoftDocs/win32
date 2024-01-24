---
title: LVM_GETNEXTITEMINDEX message (Commctrl.h)
description: Retrieves the index of an item in a specified list-view control that matches the specified properties and relationship to another item. Send this message explicitly or by using the ListView\_GetNextItemIndex macro.
ms.assetid: 'vs|controls|~\controls\listview\messages\lvm_getnextitemindex.htm'
keywords:
- LVM_GETNEXTITEMINDEX message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETNEXTITEMINDEX
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETNEXTITEMINDEX message

Retrieves the index of an item in a specified list-view control that matches the specified properties and relationship to another item. Send this message explicitly or by using the [**ListView\_GetNextItemIndex**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getnextitemindex) macro.

## Parameters

<dl> <dt>

*wParam* \[in, out\]
</dt> <dd>

A pointer to the [**LVITEMINDEX**](/windows/win32/api/commctrl/ns-commctrl-lvitemindex) structure for the item to begin the search with, or -1 to find the first item that matches the specified flags. The calling process is responsible for allocating this structure and setting its members.

</dd> <dt>

*lParam* 
</dt> <dd>

Specifies the relationship to the item listed in parameter *wParam*. This can be one or a combination of the following values:



| Value                                                                                                                                                                                                                                                             | Meaning                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt></dt> <dt>Searches by index.</dt> </dl>                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <span id="_______________LVNI_ALL"></span><span id="_______________lvni_all"></span><dl> <dt> **LVNI\_ALL**</dt> <dt></dt> </dl>                               | Searches for a subsequent item by index, the default value.<br/>                                                                                                                                                                                                                                                                                                                                            |
| <dl> <dt></dt> <dt>Searches by physical relationship to the index of the item where the search is to begin.</dt> </dl>                                         |                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <span id="_______________LVNI_ABOVE"></span><span id="_______________lvni_above"></span><dl> <dt> **LVNI\_ABOVE**</dt> <dt></dt> </dl>                         | Searches for an item that is above the specified item.<br/>                                                                                                                                                                                                                                                                                                                                                 |
| <span id="_______________LVNI_BELOW"></span><span id="_______________lvni_below"></span><dl> <dt> **LVNI\_BELOW**</dt> <dt></dt> </dl>                         | Searches for an item that is below the specified item.<br/>                                                                                                                                                                                                                                                                                                                                                 |
| <span id="_______________LVNI_TOLEFT"></span><span id="_______________lvni_toleft"></span><dl> <dt> **LVNI\_TOLEFT**</dt> <dt></dt> </dl>                      | Searches for an item to the left of the specified item.<br/>                                                                                                                                                                                                                                                                                                                                                |
| <span id="_______________LVNI_PREVIOUS"></span><span id="_______________lvni_previous"></span><dl> <dt> **LVNI\_PREVIOUS**</dt> <dt></dt> </dl>                | **Windows Vista and later:** Searches for an item that is ordered before the item specified in *wParam*. The LVNI\_PREVIOUS flag is not directional (LVNI\_ABOVE will find the item positioned above, while LVNI\_PREVIOUS will find the item ordered before.) The LVNI\_PREVIOUS flag basically reverses the logic of the search performed by the LVM\_GETNEXTITEM or LVM\_GETNEXTITEMINDEX messages.<br/> |
| <span id="_______________LVNI_TORIGHT"></span><span id="_______________lvni_toright"></span><dl> <dt> **LVNI\_TORIGHT**</dt> <dt></dt> </dl>                   | Searches for an item to the right of the specified item.<br/>                                                                                                                                                                                                                                                                                                                                               |
| <span id="_______________LVNI_DIRECTIONMASK"></span><span id="_______________lvni_directionmask"></span><dl> <dt> **LVNI\_DIRECTIONMASK**</dt> <dt></dt> </dl> | **Windows Vista and later:** A directional flag mask with value as follows: LVNI\_ABOVE \| LVNI\_BELOW \| LVNI\_TOLEFT \| LVNI\_TORIGHT.<br/>                                                                                                                                                                                                                                                               |
| <dl> <dt></dt> <dt>The state of the item to find can be specified with one or a combination of the following values:</dt> </dl>                                |                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <span id="_______________LVNI_CUT"></span><span id="_______________lvni_cut"></span><dl> <dt> **LVNI\_CUT**</dt> <dt></dt> </dl>                               | The item has the [**LVIS\_CUT**](list-view-item-states.md) state flag set.<br/>                                                                                                                                                                                                                                                                                                                   |
| <span id="_______________LVNI_DROPHILITED"></span><span id="_______________lvni_drophilited"></span><dl> <dt> **LVNI\_DROPHILITED**</dt> <dt></dt> </dl>       | The item has the [**LVIS\_DROPHILITED**](list-view-item-states.md) state flag set<br/>                                                                                                                                                                                                                                                                                                    |
| <span id="_______________LVNI_FOCUSED"></span><span id="_______________lvni_focused"></span><dl> <dt> **LVNI\_FOCUSED**</dt> <dt></dt> </dl>                   | The item has the [**LVIS\_FOCUSED**](list-view-item-states.md) state flag set.<br/>                                                                                                                                                                                                                                                                                                           |
| <span id="_______________LVNI_SELECTED"></span><span id="_______________lvni_selected"></span><dl> <dt> **LVNI\_SELECTED**</dt> <dt></dt> </dl>                | The item has the [**LVIS\_SELECTED**](list-view-item-states.md) state flag set.<br/>                                                                                                                                                                                                                                                                                                         |
| <span id="_______________LVNI_STATEMASK"></span><span id="_______________lvni_statemask"></span><dl> <dt> **LVNI\_STATEMASK**</dt> <dt></dt> </dl>             | **Windows Vista and later:** A state flag mask with value as follows: LVNI\_FOCUSED \| LVNI\_SELECTED \| LVNI\_CUT \| LVNI\_DROPHILITED.<br/>                                                                                                                                                                                                                                                               |
| <dl> <dt></dt> <dt>Searches by appearance of items or by group.</dt> </dl>                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <span id="_______________LVNI_VISIBLEORDER"></span><span id="_______________lvni_visibleorder"></span><dl> <dt> **LVNI\_VISIBLEORDER**</dt> <dt></dt> </dl>    | **Windows Vista and later:** Search the visible order.<br/>                                                                                                                                                                                                                                                                                                                                                 |
| <span id="_______________LVNI_VISIBLEONLY"></span><span id="_______________lvni_visibleonly"></span><dl> <dt> **LVNI\_VISIBLEONLY**</dt> <dt></dt> </dl>       | **Windows Vista and later:** Search the visible items.<br/>                                                                                                                                                                                                                                                                                                                                                 |
| <span id="_______________LVNI_SAMEGROUPONLY"></span><span id="_______________lvni_samegrouponly"></span><dl> <dt> **LVNI\_SAMEGROUPONLY**</dt> <dt></dt> </dl> | **Windows Vista and later:** Search the current group.<br/>                                                                                                                                                                                                                                                                                                                                                 |
| <dl> <dt></dt> <dt>If an item does not have all of the specified state flags set, the search continues with the next item.</dt> </dl>                          |                                                                                                                                                                                                                                                                                                                                                                                                                   |



 

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

Note that the following flags, for use only with Windows Vista, are mutually exclusive of any other flags in use: LVNI\_PREVIOUS, LVNI\_VISIBLEONLY, LVNI\_SAMEGROUPONLY, LVNI\_VISIBLEORDER, LVNI\_DIRECTIONMASK, and LVNI\_STATEMASK.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**LVM\_GETNEXTITEM**](lvm-getnextitem.md)
</dt> </dl>

 

 





