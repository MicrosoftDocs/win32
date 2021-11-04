---
title: Tree-View Control Item States (CommCtrl.h)
description: This section lists the item state flags used to indicate the state of an item in a tree-view control.
ms.assetid: 5b11d575-6dfd-47a8-b959-b19aaeeca70e
topic_type:
- apiref
api_name:
- TVIS_BOLD
- TVIS_CUT
- TVIS_DROPHILITED
- TVIS_EXPANDED
- TVIS_EXPANDEDONCE
- TVIS_EXPANDPARTIAL
- TVIS_SELECTED
- TVIS_OVERLAYMASK
- TVIS_STATEIMAGEMASK
- TVIS_USERMASK
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Tree-View Control Item States

This section lists the item state flags used to indicate the state of an item in a tree-view control.



| Constant                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TVIS_BOLD"></span><span id="tvis_bold"></span><dl> <dt>**TVIS\_BOLD**</dt> </dl>                               | The item is bold.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| <span id="TVIS_CUT"></span><span id="tvis_cut"></span><dl> <dt>**TVIS\_CUT**</dt> </dl>                                  | The item is selected as part of a cut-and-paste operation. <br/>                                                                                                                                                                                                                                                                                                                                                                                           |
| <span id="TVIS_DROPHILITED"></span><span id="tvis_drophilited"></span><dl> <dt>**TVIS\_DROPHILITED**</dt> </dl>          | The item is selected as a drag-and-drop target.<br/>                                                                                                                                                                                                                                                                                                                                                                                                       |
| <span id="TVIS_EXPANDED"></span><span id="tvis_expanded"></span><dl> <dt>**TVIS\_EXPANDED**</dt> </dl>                   | The item's list of child items is currently expanded; that is, the child items are visible. This value applies only to parent items.<br/>                                                                                                                                                                                                                                                                                                                  |
| <span id="TVIS_EXPANDEDONCE"></span><span id="tvis_expandedonce"></span><dl> <dt>**TVIS\_EXPANDEDONCE**</dt> </dl>       | The item's list of child items has been expanded at least once. The [TVN\_ITEMEXPANDING](tvn-itemexpanding.md) and [TVN\_ITEMEXPANDED](tvn-itemexpanded.md) notification codes are not generated for parent items that have this state set in response to a [**TVM\_EXPAND**](tvm-expand.md) message. Using TVE\_COLLAPSE and TVE\_COLLAPSERESET with **TVM\_EXPAND** will cause this state to be reset. This value applies only to parent items. <br/> |
| <span id="TVIS_EXPANDPARTIAL"></span><span id="tvis_expandpartial"></span><dl> <dt>**TVIS\_EXPANDPARTIAL**</dt> </dl>    | **Version 4.70**. A partially expanded tree-view item. In this state, some, but not all, of the child items are visible and the parent item's plus symbol is displayed. <br/>                                                                                                                                                                                                                                                                              |
| <span id="TVIS_SELECTED"></span><span id="tvis_selected"></span><dl> <dt>**TVIS\_SELECTED**</dt> </dl>                   | The item is selected. Its appearance depends on whether it has the focus. The item will be drawn using the system colors for selection. <br/>                                                                                                                                                                                                                                                                                                              |
| <span id="TVIS_OVERLAYMASK"></span><span id="tvis_overlaymask"></span><dl> <dt>**TVIS\_OVERLAYMASK**</dt> </dl>          | Mask for the bits used to specify the item's overlay image index.<br/>                                                                                                                                                                                                                                                                                                                                                                                     |
| <span id="TVIS_STATEIMAGEMASK"></span><span id="tvis_stateimagemask"></span><dl> <dt>**TVIS\_STATEIMAGEMASK**</dt> </dl> | Mask for the bits used to specify the item's state image index.<br/>                                                                                                                                                                                                                                                                                                                                                                                       |
| <span id="TVIS_USERMASK"></span><span id="tvis_usermask"></span><dl> <dt>**TVIS\_USERMASK**</dt> </dl>                   | Same as **TVIS\_STATEIMAGEMASK**.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                     |



## Remarks

When you set or retrieve an item's overlay image index or state image index, you must specify the following masks in the **stateMask** member of the [**TVITEM**](/windows/win32/api/commctrl/ns-commctrl-tvitema) structure:

-   **TVIS\_OVERLAYMASK**
-   **TVIS\_STATEIMAGEMASK**
-   **TVIS\_USERMASK**

These values can also be used to mask off the state bits that are not of interest.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



 

 





