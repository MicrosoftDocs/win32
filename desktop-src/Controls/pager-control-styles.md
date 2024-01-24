---
title: Pager Control Styles (CommCtrl.h)
description: This section lists the window styles used when creating pager controls.
ms.assetid: 619fd8cc-e231-41af-8744-a29d14f2c6f8
topic_type:
- apiref
api_name:
- PGS_AUTOSCROLL
- PGS_DRAGNDROP
- PGS_HORZ
- PGS_VERT
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Pager Control Styles

This section lists the window styles used when creating pager controls.



| Constant                                                                                                                                                         | Description                                                                                                                                                                                                                 |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PGS_AUTOSCROLL"></span><span id="pgs_autoscroll"></span><dl> <dt>**PGS\_AUTOSCROLL**</dt> </dl> | The pager control will scroll when the user hovers the mouse over one of the scroll buttons.<br/>                                                                                                                     |
| <span id="PGS_DRAGNDROP"></span><span id="pgs_dragndrop"></span><dl> <dt>**PGS\_DRAGNDROP**</dt> </dl>    | The contained window can be a drag-and-drop target. The pager control will automatically scroll if an item is dragged from outside the pager over one of the scroll buttons.<br/>                                     |
| <span id="PGS_HORZ"></span><span id="pgs_horz"></span><dl> <dt>**PGS\_HORZ**</dt> </dl>                   | Creates a pager control that can be scrolled horizontally. This style and the **PGS\_VERT** style are mutually exclusive and cannot be combined.<br/>                                                                 |
| <span id="PGS_VERT"></span><span id="pgs_vert"></span><dl> <dt>**PGS\_VERT**</dt> </dl>                   | Creates a pager control that can be scrolled vertically. This is the default direction if no direction style is specified. This style and the **PGS\_HORZ** style are mutually exclusive and cannot be combined.<br/> |



## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



 

 





