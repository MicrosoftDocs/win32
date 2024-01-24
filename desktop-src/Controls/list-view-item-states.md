---
title: List-View Item States (CommCtrl.h)
description: An item's state value consists of the item's state, an optional overlay mask index, and an optional state image mask index.
ms.assetid: 21827f4a-f133-489b-bbd2-6979d1928b40
topic_type:
- apiref
api_name:
- LVIS_ACTIVATING
- LVIS_CUT
- LVIS_DROPHILITED
- LVIS_FOCUSED
- LVIS_OVERLAYMASK
- LVIS_SELECTED
- LVIS_STATEIMAGEMASK
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# List-View Item States

An item's state value consists of the item's state, an optional overlay mask index, and an optional state image mask index.

An item's state determines its appearance and functionality. The state can be zero or one or more of the following values:



| Constant                                                                                                                                                                        | Description                                                                                                                                                          |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="LVIS_ACTIVATING"></span><span id="lvis_activating"></span><dl> <dt>**LVIS\_ACTIVATING**</dt> </dl>             | Not currently supported.<br/>                                                                                                                                  |
| <span id="LVIS_CUT"></span><span id="lvis_cut"></span><dl> <dt>**LVIS\_CUT**</dt> </dl>                                  | The item is marked for a cut-and-paste operation.<br/>                                                                                                         |
| <span id="LVIS_DROPHILITED"></span><span id="lvis_drophilited"></span><dl> <dt>**LVIS\_DROPHILITED**</dt> </dl>          | The item is highlighted as a drag-and-drop target.<br/>                                                                                                        |
| <span id="LVIS_FOCUSED"></span><span id="lvis_focused"></span><dl> <dt>**LVIS\_FOCUSED**</dt> </dl>                      | The item has the focus, so it is surrounded by a standard focus rectangle. Although more than one item may be selected, only one item can have the focus.<br/> |
| <span id="LVIS_OVERLAYMASK"></span><span id="lvis_overlaymask"></span><dl> <dt>**LVIS\_OVERLAYMASK**</dt> </dl>          | The item's overlay image index is retrieved by a mask.<br/>                                                                                                    |
| <span id="LVIS_SELECTED"></span><span id="lvis_selected"></span><dl> <dt>**LVIS\_SELECTED**</dt> </dl>                   | The item is selected. The appearance of a selected item depends on whether it has the focus and also on the system colors used for selection.<br/>             |
| <span id="LVIS_STATEIMAGEMASK"></span><span id="lvis_stateimagemask"></span><dl> <dt>**LVIS\_STATEIMAGEMASK**</dt> </dl> | The item's state image index is retrieved by a mask.<br/>                                                                                                      |



## Remarks

You can use the **LVIS\_OVERLAYMASK** mask to isolate the one-based index of the overlay image. You can use the **LVIS\_STATEIMAGEMASK** mask to isolate the one-based index of the state image.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



 

 





